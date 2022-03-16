# Created by machadoca at 10/03/22
Feature: As a user I want to confirm related articles tags are matching the current article

    @article-related
    Scenario Outline: Test the related articles tags are associated to the current article
        Given a user is at the <keyword> site
        When the user scrolls to the related stories section
        Then the user sees articles matching tags in current article

     Examples:
            | keyword                                                                       |
            | /outreach-initiatives/accessibility/ml-making-sign-language-more-accessible/  |
#            | /technology/ai/discover-ai-in-daily-life/                                     | hero       |
#            | /outreach-initiatives/diversity/international-womens-day-2022/                | hero       |