Feature: Creacion de usuarios

Scenario: Nuevo usuario
	Given I see the Username "Sergio"
	And I see the Email "sergiojgl@gmail.com"
	And I see the Password "markota"
	And I see the Password > 7
	Then I create the user

