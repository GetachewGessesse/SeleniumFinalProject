

class SignUpConstants:
    url = "https://api.demoblaze.com/signup"

    valid_data = {"username":"gechhh",
                  "password":"gechhh12345"}

    invalid_data_username = {"username": "",
                             "password": "aHNhZ2NkaGNzZGdm"}

    invalid_data_password = {"username": "hsgshdvvfg",
                             "password": ""}

    invalid_both_data = {"username": "",
                             "password": ""}

    invalid_existing_data = {"username": "azuta",
                             "password": "1234"}