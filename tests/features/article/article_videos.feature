# Created by machadoca at 4/03/22
Feature: As a user I want to be able to interact with videos shown in the content's article


    @article
    Scenario Outline: Test a user can interact with a video in the hero's article
        Given a user is at the <keyword> site
        And the user clicks to play the <video_type>
        Then the user can interact with the video controls

     Examples:
            | keyword                                                                       | video_type |
            | /outreach-initiatives/accessibility/ml-making-sign-language-more-accessible/  | hero       |
            | /technology/ai/discover-ai-in-daily-life/                                     | hero       |

    @article
    Scenario Outline: Test a user can interact with a video in the body's article
        Given a user is at the <keyword> site
        And the user clicks to play the <video_type>
        Then the user can interact with the video controls

     Examples: Vertical
            | keyword   | /outreach-initiatives/google-news-initiative/demystifying-process-launching-news-business/   |
            | video_type | body                                                                                        |
