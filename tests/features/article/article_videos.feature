# Created by machadoca at 4/03/22
Feature: As a user, I want to be able to interact with videos shown in the content's article


    @article
    Scenario Outline: Test a user can interact with a video in the hero's article
        Given a user is at the <keyword> site
        And the user clicks to play the <video_type>
        Then the user can interact with the video controls

     Examples:
      | keyword                                                                          | video_type |
      | /outreach-initiatives/accessibility/ml-making-sign-language-more-accessible/     | hero       |
      | /intl/en-in/company-news/technology/empowering-women-speak-solutions/            | hero       |
      | /intl/en-ca/products/devices-services/speaking-our-language-importance-mandarin-pixel-6-ad-simu-liu/  | hero  |
      | /technology/ai/discover-ai-in-daily-life/                                        | hero       |
      | /outreach-initiatives/diversity/international-womens-day-2022/                   | hero       |

    @article
    Scenario Outline: Test a user can interact with a video in the body's article
        Given a user is at the <keyword> site
        And the user clicks to play the <video_type>
        Then the user can interact with the video controls

     Examples:
      | keyword                                                                     | video_type |
      | /intl/de-de/unternehmen/engagement/heartbeat-of-the-earth-2022/             | body       |
      | /intl/en-in/company-news/technology/empowering-women-speak-solutions/       | body       |
      | /intl/en-ca/company-news/technology/introducing-topaz/                      | body       |
      | /intl/en-au/company-news/outreach-initiatives/digital-future-initiative/    | body       |
      | /intl/fr-ca/nouvelles/technologie/voici-topaz-le-premier-cable-sous-marin-relier-le-canada-lasie/ | body   |
      | /outreach-initiatives/google-news-initiative/demystifying-process-launching-news-business/        | body   |
      | /intl/es-419/noticias-de-la-empresa/iniciativas/google-arts-and-culture-y-naciones-unidas-muestran-el-impacto-del-cambio-climatico-con-el-latido-de-la-tierra/        | body   |
      | /intl/it-it/prodotti/youtube/uno-sguardo-al-2022-youtube/                   | body   |
      #TODO: This video is actually not playing in the live site, because the author name contains a special character
      | /intl/fr-ca/produits/appareils-services/la-star-canadienne-du-tennis-leylah-fernandez-rejoint-teampixel/ |body|

