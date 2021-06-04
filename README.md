# SaaS-in-a-Flask

[![codecov](https://codecov.io/gh/navanchauhan/SaaS-in-a-Flask/branch/master/graph/badge.svg?token=ULbtVCRrrY)](https://codecov.io/gh/navanchauhan/SaaS-in-a-Flask)
[![Flask Tests](https://github.com/navanchauhan/SaaS-in-a-Flask/actions/workflows/Flask-Tests.yaml/badge.svg)](https://github.com/navanchauhan/SaaS-in-a-Flask/actions/workflows/Flask-Tests.yaml)

In the wise words of @alectrocute:

> I've noticed SaaS bootstraps/boilerplates being sold upwards of $1,000 per year and I think that's fucking ridiculous.

## Features

- [x] **Landing Page:** Written in Bootstrap 5, compatible with [Bootswatch Themes](https://bootswatch.com)
- [ ] Database Management
- **Authentication:** Using Flask-Login 
	- [x] Sign Up
	- [x] Sign In
	- [ ] OAuth2
	- [ ] LDAP
	- [ ] Forgot Password
	- [ ] Confirm Email
	- [x] **Password Hashing:** Using Bcrypt (Flask-Bcrypt)
- [x] **Form Handling:** With Flask-WTF using WTForms
- [x] Dashboard
- [x] GitHub Workflows
- [ ] Admin Pages
- [ ] Role Support
- [ ] Team Management
- Error Handling
	- [ ] Sentry Support
	- [ ] Error Code Handling
	- [ ] Custom Exceptions
	- [x] 404,500,401 e.t.c
- [ ] Async AJAX Calls 
- [x] **Tests:** Using PyTest
- [x] **Code Coverage:** Using CodeCov
- [ ] Delayed Jobs
- [ ] Logging
- [ ] FastAPI Support
- Billing Handling
	- [ ] Stripe
- [ ] GDPR Compliance / Data Export
- [ ] Docker Images

## Quick How-Tos

### Makefile

#### Install Dependencies using pip

```
make install
```

#### Initialise Database

```
make db

```

#### Run Development Server

```
make dev

```

### Running Tests

You need to be in the base directory of the repo to run tests.

#### Using Pipenv

```
pipenv run tests
```

#### Manually

```
python -m pytest
```

#### GitHub Workflow

The GitHub Workflow automatically installs all dependencies in the requirements.txt file and runs pytest on different Python 3 versions (3.7, 3.8 ,3.9). To generate the requirements.txt file from pipenv use `pipenv lock --dev -r > requirements.txt`

### Code Coverage

[Codecov](https://codecov.io) is used to automatically generate reports and upload to their website using a GitHub Action. Make sure to set up `CODECOV_TOKEN` secret in your repo to use the workflow.