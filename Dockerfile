FROM python:3.9.6-buster

# Install tini.
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini"]

# Install OS dependencies.
RUN apt-get update -qqy \
  && apt-get -qqy install graphviz

# Install browsers.
# Chrome
# ARG CHROME_VERSION="google-chrome-stable=92.0.4515.107"
ARG CHROME_VERSION="google-chrome-stable"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable}

# TODO: add firefox

# Install python dependencies.
WORKDIR /chrome-test
COPY ./requirements.txt /chrome-test
RUN pip install -r requirements.txt

# Copy test drives.
WORKDIR /chrome-test/bin/linux
COPY ./bin/linux .
ENV PATH="/:${PATH}"
ENV PATH="/chrome-test/bin/linux:${PATH}"

# Copy test source code.
WORKDIR /chrome-test/tests
COPY tests/consts/* consts/
COPY tests/features/linux_platform/* features/linux_platform/
COPY tests/pages/* pages/
COPY tests/step_defs/* step_defs/
COPY tests/__init__.py .
COPY tests/conftest.py .
COPY tests/pytest.ini .
COPY tests/run_tests.sh .

#RUN echo $(ls -laR /chrome-test/tests/)

# Reports.
# VOLUME [ "/chrome-test/html_reports" ]

# Run the test command.
CMD ["/chrome-test/tests/run_tests.sh"]
