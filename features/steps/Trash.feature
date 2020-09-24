Feature: Get trash day
  A user can get the trash day for a certain week.

  Scenario: default trash day
    Given a date with no holidays during the week
    When getting the trash day for that week
    Then the default trash day is returned

  Scenario Outline: default trash day
    Given a <date> with a holiday during the week
    When getting the trash day for that week
    Then the <holiday> trash schedule is returned

    Examples:
    | date       | holiday        |
    | 2020-01-01 | New Year's Day |
    | 2020-12-20 | Christmas Day  |
    | 2020-09-07 | Labor Day      |
    | 2020-11-25 | Thanksgiving   |