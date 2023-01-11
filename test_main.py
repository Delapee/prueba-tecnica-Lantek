import pytest
from unittest.mock import patch
from requests import Response

from main import make_requests, parse_data

API_URL = "https://app-academy-neu-codechallenge.azurewebsites.net/api/2d/cut"
USER = "lantekacademy"
PASS = ":cPIi<kyF(=5OXc"

def test_make_request_wrong_credentials():
    res = make_requests(API_URL, "wrong_user", "wrong_pass")

    assert res.status_code == 401
    assert type(res) == Response

def test_make_request_correct_credentials():
    res = make_requests(API_URL, USER, PASS)

    assert res.status_code == 200
    assert type(res) == Response

def test_parse_data_not_200():
    res = make_requests(API_URL, "wrong_user", "wrong_pass")
    machines = parse_data(res)

    assert len(machines) == 0
    assert type(machines) == list

def test_parse_data_200():
    res = make_requests(API_URL, USER, PASS)
    machines = parse_data(res)

    # I'm not checking if the id parameter exists because it's not used in the application
    assert all("name" and "manufacturer" in machine for machine in machines)
    assert type(machines) == list
