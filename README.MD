# API Tests

Automated API tests written in Python (pytest + requests),
run against the public ReqRes test API.

## What is covered
- GET single user: status code and response body
- GET non-existing user: 404
- GET user email, first name, last name
- POST create user: status code and response body
- Negative test: empty field validation

## How to run
1. Create and activate virtual environment
2. `pip install -r requirements.txt`
3. `pytest -v`