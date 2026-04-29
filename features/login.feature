Feature: Login
    Scenario: Successful login
        When the user opens the login page
        And the user enters valid credentials
        Then the user should see the inventory page