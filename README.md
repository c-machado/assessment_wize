# How to set up?
This project has been built using Python and Pytest-BDD. All the expected behaviours
have been documented using the Gherkin language.


## What do you need?
In order to set up this project you required: 

1. An up-to-date version of Python 3
1. pipenv and virtualenv, to manage the dependencies and the virtual environment   
1. Install python with pyenv, so you can manage the installed versions
1. Install dependencies store in the pipfile.

If you're unsure which Python version you have in your machine, please run the following command in your terminal:
```
$ python --version
```

## How to install python with pyenv?
1. Check if pyenv is installed
```
$ pyenv --version
```
If you do not have it, then click [here](https://github.com/pyenv/pyenv#readme) and follow the instructions. 

2. Check all versions of python installed
```
$ pyenv versions
```
3. Check list of versions of python available 
```
$ pyenv install --list
```
4. Install the version needed  
```
$ pyenv install 3.9.6
```
If you are on MacOS Big Sur, you need to complete an additional configuration:

4.1. Install required dependencies
```
$ brew install zlib
$ export LDFLAGS="-L/usr/local/opt/zlib/lib" 
$ export CPPFLAGS="-I/usr/local/opt/zlib/include
$ brew install readline xz
```

4.2. Align command-line tools
```
1. Open Xcode
2. Go to Preference > Locations
3. Select the right version of command-line tools 
```

4.3. Install Python
```
$ CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix readline)/include 
-I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib 
-L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install 3.9.6
```
5. Check the version installed is on the installed versions of python 
```
$ pyenv versions
```
6. Set the installed version as the python to use by your system 
```
$ pyenv global 3.9.6
$ pyenv shell 3.9.6
```
7. Install pyenv-virtualenv to manage the virtual environment

Click [here](https://github.com/pyenv/pyenv-virtualenv) to complete pyenv-virtualenv installation. 

pip [here](https://phoenixnap.com/kb/install-pip-mac)

## How to install the dependencies?
Note: Always use a virtual environment to manage your packages and dependencies
1. Go to folder’s project
1. Create or activate an existing virtual environment.
```
$ pyenv virtualenv environment-name
```   
The environment should be activated automatically (once you added the variable pyenv-virtualenv):
```
$ pyenv versions
```
Otherwise, activate the environment manually:
```
$ pyenv shell environment-name
```
8. Install pip [here] (https://pip.pypa.io/en/stable/installation/)


9. Install pipenv, in order to manage your pipfile
``` 
pip install pipenv
```    
10. Install the environment with the modules defined in the pipfile 
```
$ pipenv install
```

## How to run tests?
1. Run tests in a specific file
```
$ pipenv run python3 -m pytest 
```
Within the test file, you need to specified the feature file and the scenario to run, e.g:
```
@scenario("../features/file_name.feature", "Download Chrome") or
@scenarios("../features/")
```
1. Run tests for a specific tag
```
$ pipenv run python3 -k pytest “env-mac”
```

## How to run tests in parallel?

1. Install pytest-xdist
```
$ pipenv install pytest-xdist
```
1. Now to run tests in parallel, you'll need to use the -n and then you provide the number of threads you want to run
```
$ pipenv run python3 -m pytest tests/step_defs/download_chrome_steps.py -n 3
```
## How to see pytest help?
```
$ pytest -h
```
## Any troubles?

If you run into any issues while trying to execute this suite, please feel 
free to contact me at **cmachado@hugeinc.com**, I'll be happy to take a look at it.   

Thank you! 
:sunglasses:
