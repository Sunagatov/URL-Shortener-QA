# URL Shortener QA

Python API tests for URL shortening, redirects, expiration, authentication and MongoDB persistence.

<p>
  <a href="https://buymeacoffee.com/lucky_1uck">
    <img src="https://img.shields.io/badge/Support_the_project-FFDD00?style=for-the-badge&amp;logo=buymeacoffee&amp;logoColor=black" alt="Support the project" width="260" height="40">
  </a>
</p>

## Test areas

- Creating short URLs and rejecting invalid inputs.
- Redirecting to original URLs and handling redirect loops.
- Expiration and short-link uniqueness.
- Positive and negative sign-in/sign-up cases.
- Database assertions and cleanup of created records.

**Stack:** Python · pytest · Requests · PyMongo · PyHamcrest · Allure

## Install

Use a virtual environment with a Python version supported by the pinned
dependencies, then install from [requirements.txt](requirements.txt):

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell instead: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Configure

Use a dedicated API and MongoDB test environment: fixtures create accounts and
short links, then delete records during cleanup.

| Setting | Location | Purpose |
| --- | --- | --- |
| `HOST` | `configs.py` | Backend API base URL |
| `MONGODB_DATABASE` | `configs.py` | Test database name |
| `MONGODB_COLLECTION_URL` | `configs.py` | URL collection |
| `MONGODB_COLLECTION_USER` | `configs.py` | User collection |
| `MONGODB_URI` | Environment or local `.env` | MongoDB connection string |

The fixtures load `.env` using python-dotenv and require `MONGODB_URI` during
test collection. The API and database must describe the same test deployment.
Keep credentials out of commits.

## Run

From the repository root:

```bash
python -m pytest API/TEST
```

[pytest.ini](pytest.ini) configures Allure output in `allure-results`, two retries
and a five-second retry delay. For a smaller run, pass a test file or use `-k`.

## View results

Install the [Allure CLI](https://allurereport.org/docs/gettingstarted/installation/)
separately, then serve the existing result directory:

```bash
allure serve allure-results
```

## Structure

- [API/TEST](API/TEST): test cases and data-cleanup fixtures.
- [API/FRAMEWORK](API/FRAMEWORK): endpoint clients, assertions, MongoDB access and tools.
- [API/DATA](API/DATA): positive and negative test inputs.

This is a separate QA suite. Compare its endpoint clients with the target
[URL-Shortener](https://github.com/Sunagatov/URL-Shortener) version when APIs change.

## ☕ Support the project

If this project helps you learn or build, you can support its development.

<p>
  <a href="https://buymeacoffee.com/lucky_1uck">
    <img src="https://img.shields.io/badge/Support_the_project-FFDD00?style=for-the-badge&amp;logo=buymeacoffee&amp;logoColor=black" alt="Support the project" width="260" height="40">
  </a>
</p>
