Feature:To check the login scenarios of the web page
Scenario:To check login successful
Given I am on the webpage
When I would enter valid credentials
Then I click on login Button 

Scenario:To check invalid email and invalid password
Given I am on the webpage
When I would enter invalid emil and invalid password
Then i should get error message 

Scenario:To check valid email and invalid password
Given I am on the webpage
When I would enter valid email and invalid password
Then I should get error message stating invalid password

Scenario:To check invalid email and valid password
Given I am on the webpage
When I would enter invalid email and valid password
Then I should get error message stating invalid email

Scenario:To check when email field kept blank and valid password is entered
Given I am on the webpage
When I would keep email field empty and enter valid password
Then I should get error message stating please enter your email

Scenario:To check when valid email-id is entered and password field is kept empty
Given I am on the webpage
When I would enter valid email and keep password field empty
Then I should get an error message stating please enter password

Scenario:To check when I would keep both the email field and password fiel empty
Given I am on the webpage 
When I would not enter email id and password and hit on login button
Then I should get an error stating please enter email id and password
