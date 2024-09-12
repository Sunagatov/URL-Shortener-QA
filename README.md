# URL-Shortener-QA
URL-Shortener-QA



## Report
(!) BE SURE TO INSTALL ALLURE -> https://allurereport.org/docs/gettingstarted/installation/

To get the Allure report on the local computer, follow these steps in root directory:
```bash
python3 -m pytest  API/TEST --alluredir=allure_report --clean-alluredir
allure serve allure_report
```
