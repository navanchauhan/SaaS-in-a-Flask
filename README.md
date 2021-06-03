# SaaS-in-a-Flask

In the wise words of @alectrocute:

> I've noticed SaaS bootstraps/boilerplates being sold upwards of $1,000 per year and I think that's fucking ridiculous.

## Development

### Generating requirements.txt for GitHub Actions

`pipenv lock --dev -r > requirements.txt`

## Features

- [x] Landing Page
- [ ] Database Management
- Authentication
	- [x] Sign Up
	- [x] Sign In
	- [ ] OAuth2
	- [ ] LDAP
	- [ ] Forgot Password
	- [ ] Confirm Email
	- [x] Password Hashing 
- [x] Form Handling
- [x] Dashboard
- [ ] GitHub Workflows
- [ ] Admin Pages
- [ ] Role Support
- [ ] Team Management
- Error Handling
	- [ ] Sentry Support
	- [ ] Error Code Handling
	- [ ] Custom Exceptions
	- [x] 404,500,401 e.t.c
- [ ] Async AJAX Calls 
- [ ] Tests
- [ ] Delayed Jobs
- [ ] Logging
- [ ] FastAPI Support
- Billing Handling
	- [ ] Stripe
- [ ] GDPR Compliance / Data Export
- [ ] Docker Images