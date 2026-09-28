# Regres API request

import requests
import json

BASE_URL = "https://reqres.in/api"

userFound = "2"

def test_get_user_return200():
    response = requests.get(f"{BASE_URL}/users/"+userFound)
    #print(json.dumps(response.json(), indent=2))    
    #with open("output.json", "w") as f:
    #    json.dump(response.json(), f, indent=2)
    assert response.status_code == 200

userNotFound = "23"

def test_get_user_return404():
    response = requests.get(f"{BASE_URL}/users/"+userNotFound)
    assert response.status_code == 404

def test_get_user_has_correct_email():
    response = requests.get(f"{BASE_URL}/users/{userFound}")
    body = response.json()
    assert body["data"]["email"] == "janet.weaver@reqres.in"
    assert body["data"]["first_name"] == "Janet"
    assert body["data"]["last_name"] == "Weaver"

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

def test_create_user_with_empty_job_return400():
    payLoad ={
        "name" : "Jovan",
        "job" : ""
    }
    response = requests.post(f"{BASE_URL}/users", json=payLoad)
    assert response.status_code == 400
  