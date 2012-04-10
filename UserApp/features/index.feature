Feature: Creacion de usuarios

Scenario: Nuevo usuario
    Given I see the Username "Sergio"
    And I see the Email "sergiojgl@gmail.com"
    When I check it is correct
    Then I create the user
