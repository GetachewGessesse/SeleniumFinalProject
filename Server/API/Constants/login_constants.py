
class LoginConstants:
    url = "https://api.demoblaze.com/login"

    valid_data = {"username" :"azuta",
                  "password" :"azuta1234"}

    invalid_data_username = {"username": "schgdhf",
                             "password": "azuta1234"}

    invalid_data_password = {"username": "azuta",
                             "password": "jaschgd"}

    invalid_both_data = {"username": "azutadjfh",
                             "password": "jaschgd"}