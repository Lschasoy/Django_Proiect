Feature: Creacion de usuarios

Scenario: A new user
    Given I see the Username ""
    And I see the Email ""
    When I check it is correct
    Then I create the user
