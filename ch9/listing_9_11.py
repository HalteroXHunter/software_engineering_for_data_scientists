import keyring

keyring.set_password("database_credentials",
    "secret_username",
    "secret_password")

print(keyring.get_password("database_credentials",
    "secret_username"))