Feature: Get trash day
  A user can get the trash day for a certain week.

  Scenario: trash day is the regular trash day
    Given a date with no holidays during the week
    When getting the trash day for that week
    Then the default trash day is returned

  Scenario Outline: trash day is on a holiday
    Given a <date> with a holiday during the week
    When getting the trash day for that week
    Then the <holiday> trash schedule is returned

    Examples:
    | date       | holiday        |
    | 2020-12-28 | New Year's Day |
    | 2020-12-20 | Christmas Day  |
    | 2020-09-07 | Labor Day      |
    | 2020-11-24 | Thanksgiving   |