import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass


def get_credentials() -> tuple:
    print("Please introduce your credentials")

    user = input("Username: ")
    password = getpass()

    return user, password


def make_requests(url: str, user: str, password: str) -> requests.Response:
    basic_auth = HTTPBasicAuth(user, password)

    return requests.get(url, auth=basic_auth)


def parse_data(res: requests.Response) -> list:
    if res.status_code == 200:
        return res.json()

    return []


def display_machines(machines: list) -> None:
    print("\nList of cutting machines:\n")

    for machine in machines:
        print(f"Name: {machine['name']} - Manufacturer: {machine['manufacturer']}")


if __name__ == "__main__":
    API_URL = "https://app-academy-neu-codechallenge.azurewebsites.net/api/2d/cut"

    print("Welcome to the cutting machines display program.\n")

    while True:
        user, password = get_credentials()

        res = make_requests(API_URL, user, password)

        machines = parse_data(res)

        if machines:
            display_machines(machines)
            break
