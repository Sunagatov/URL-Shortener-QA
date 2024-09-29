# URL-Shortener-QA

## Automated tests for URL-Shortener Project

### Structure of the project

## Report
(!) BE SURE TO INSTALL ALLURE -> https://allurereport.org/docs/gettingstarted/installation/

To get the Allure report on the local computer, follow these steps in root directory:
```bash
pytest 
allure generate ./allure-results --clean -o ./allure-report
allure serve ./allure-results
```
or you can manually open index.html from folder allure-report