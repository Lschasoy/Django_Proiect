Feature: Creacion de micropost

Scenario: Nuevo micropost
	Given I see the Id_user "i" 
	And I see the Text "Mi primer Micropost"
	Then I create the post

