Feature: Get trash day
  A user can get the trash day for a certain week.

  Scenario: default trash day
    Given a date with no holidays during the week
    When getting the trash day for that week
    Then the default trash day is returned