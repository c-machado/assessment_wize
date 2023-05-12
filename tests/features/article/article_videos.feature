# Created by machadoca at 4/03/22
@videos
Feature: As a user, I want to be able to interact with videos shown in the content's article


    Scenario Outline: Test a user can interact with a video in the hero's article
        Given a user is at the <keyword> site
        And the user clicks to play the <video_type>
        Then the user can interact with the video controls

     Examples:
      | keyword                                                                          | video_type |
      | /inside-google/googlers/ask-a-techspert/messages-rcs/                            | hero       |
      | /intl/en-in/company-news/technology/empowering-women-speak-solutions/            | hero       |
      | /intl/en-ca/products/devices-services/speaking-our-language-importance-mandarin-pixel-6-ad-simu-liu/  | hero  |
      | /intl/es-419/actualizaciones-de-producto/informacion/como-funcionan-las-billeteras-digitales/  | hero       |
      | /intl/de-de/produkte/android-chrome-mehr/google-pay-app-wird-google-wallet/      | hero       |
      | /intl/pt-br/novidades/por-dentro-do-google/google-for-brasil-2022/               | hero       |
      | /intl/fr-ca/nouvelles/impact-initiatives/semaine-de-la-fierte-5-createurs-quebecois-lgbtq-a-decouvrir-sur-youtube/  | hero       |
      | /intl/fr-fr/nouveautes-produits/explorez-obtenez-des-reponses/de-nouvelles-fonctionnalites-rendent-google-traduction-plus-accessible-a-ses-1-milliard-dutilisateurs/    | hero       |
      | /intl/en-africa/en-africa/company-news/outreach-and-initiatives/africa-online-safety-fund-2023/   | hero       |

    Scenario Outline: Test a user can interact with a video in the body's article
        Given a user is at the <keyword> site
        And the user clicks to play the <video_type>
        Then the user can interact with the video controls

     Examples:
      | keyword                                                                          | video_type |
      | /intl/de-de/produkte/suchen-entdecken/das-neue-google-earth/                     | body       |
      | /intl/en-in/company-news/outreach-initiatives/celebrating-75-years-of-independent-india/       | body       |
      | /intl/en-ca/products/inside-youtube/youtube-music-and-youtube-premium_18/        | body       |
      | /intl/en-au/company-news/outreach-initiatives/protecting-our-reef-with-csiro/    | body       |
      | /intl/fr-ca/nouvelles/technologie/voici-topaz-le-premier-cable-sous-marin-relier-le-canada-lasie/ | body   |
      | /outreach-initiatives/google-news-initiative/demystifying-process-launching-news-business/        | body   |
      | /outreach-initiatives/education/learning-with-google-chromebook/                 | body   |
      | /intl/es-419/noticias-de-la-empresa/iniciativas/google-arts-and-culture-y-naciones-unidas-muestran-el-impacto-del-cambio-climatico-con-el-latido-de-la-tierra/        | body   |
      | /intl/it-it/prodotti/youtube/uno-sguardo-al-2022-youtube/                        | body   |
      | /intl/fr-ca/produits/appareils-services/la-star-canadienne-du-tennis-leylah-fernandez-rejoint-teampixel/ |body|
      | /intl/pt-br/o-seu-feed-do-google/                                                |body|
      | /intl/fr-fr/nouveautes-produits/appareils-services/google-pixel-watch-lingeniosite-de-google-le-suivi-sante-de-fitbit/        |body|
      | /intl/en africa/company-news/inside-google/celebrating-africa-day-virtually/       |body|

