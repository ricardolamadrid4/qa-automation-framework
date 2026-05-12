# QA Automation Framework with Selenium, Python and Behave

This project is a test automation framework developed using Python, Selenium WebDriver and Behave, following a Page Object Model (POM) structure and BDD approach with Gherkin.

## Features

- Automated login validation using SauceDemo
- Framework structure based on Page Object Model (POM)
- Reusable interactions layer for web actions
- Task and Assertions design pattern
- Test scenarios implemented with Gherkin and Behave
- Centralized test data through constants
- Hooks configuration using environment.py

## Project Structure

```text
features/        -> Gherkin scenarios and test cases
page_ui/         -> Page locators and UI elements
tasks/           -> Test flow and business actions
interactions/    -> Reusable Selenium interactions
assertions/      -> Test validations and assertions
constants/       -> Centralized test data and environment variables

## Tech Stack

- Python
- Selenium WebDriver
- Behave
- Gherkin

## Run Tests

```bash
behave
```

## Current Automated Scenarios

- Successful login validation
- Add product to cart
- Remove product from cart
- Sort products by name Z to A
- Complete checkout process