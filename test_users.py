# Regres API request

import requests
import json
import pytest
import time

@pytest.fixture(autouse=True)
def slow_down_tests():
    time.sleep(1)  # Introduce a 1-second delay before each test to avoid hitting the API too quickly
    

BASE_URL = "https://reqres.in/api"

userFound = "2"
userNotFound = "23"

# Test case for getting a user that exists, expecting a 200 OK response
def test_get_user_return200():
    response = requests.get(f"{BASE_URL}/users/"+userFound)
    #print(json.dumps(response.json(), indent=2))    
    #with open("output.json", "w") as f:
    #    json.dump(response.json(), f, indent=2)
    assert response.status_code == 200


# Test case for getting a user that does not exist, expecting a 404 Not Found response
def test_get_user_return404():
    response = requests.get(f"{BASE_URL}/users/"+userNotFound)
    assert response.status_code == 404

# Test case for getting a user and verifying the email, first name, and last name in the response body
def test_get_user_has_correct_email():
    response = requests.get(f"{BASE_URL}/users/{userFound}")
    body = response.json()
    assert body["data"]["email"] == "janet.weaver@reqres.in"
    assert body["data"]["first_name"] == "Janet"
    assert body["data"]["last_name"] == "Weaver"

#   Test case for creating a user with valid data, expecting a 201 Created response
def test_create_user_return201():
    payLoad ={
        "name" : "Ana",
        "job" : "QA"
    }
    response = requests.post(f"{BASE_URL}/users", json=payLoad)
    body = response.json()
    assert response.status_code == 201
    assert body["name"] == "Ana"
    assert body["job"] == "QA"
    assert "id" in body

# Negative test case for creating a user with an empty job field, expecting a 400 Bad Request response. Known bug: API currently accepts empty job field, so this test is marked as expected to fail (xfail).
@pytest.mark.xfail(reason="API accepts empty job field (known bug)")
def test_create_user_with_empty_job_return400():
    payLoad ={
        "name" : "Jovan",
        "job" : ""
    }
    response = requests.post(f"{BASE_URL}/users", json=payLoad)
    assert response.status_code == 400


# Parameterized test for multiple user IDs and expected status codes
@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.mark.parametrize("user_id, expected_status", [
    (1,200),
    (2,200),
    (23,404),
    (999,404)   
])
def test_get_user_status_codes_parameterized(base_url,user_id, expected_status):
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == expected_status



