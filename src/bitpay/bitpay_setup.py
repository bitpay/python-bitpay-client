import os
import json
from typing import Optional

import requests

from utils.key_utils import *
from exceptions.bitpay_exception import BitPayException

# Will be set to Test otherwise
private_key_name = "private_key.pem"  # Add here the name for your Private key
private_key_path: Optional[str] = os.path.join(
    os.path.abspath(os.curdir), private_key_name
)
plain_private_key = None
proxy = None
api_url = None
environment = None
merchant_token = None
payout_token = None


def select_env() -> None:
    global environment
    try:
        print("Select target environment: ")
        target_environment = input("Press T for testing or P for production: \n")

        if target_environment.lower() == "t":
            environment = "Test"
        elif target_environment.lower() == "p":
            environment = "Prod"
        else:
            select_env()

        set_environment(environment)  # type: ignore
        select_create_key()
    except BitPayException as exe:
        print(exe)


def set_environment(env: str) -> None:
    global api_url
    if env == "Test":
        api_url = "https://test.bitpay.com"
    else:
        api_url = "https://bitpay.com"


def select_create_key() -> None:
    try:
        input_value = input(
            "Press enter to generate a brand new key or enter your private key location:"
        )
        if input_value == "":
            create_new_key()
        else:
            load_key(input_value)
    except BitPayException as exe:
        print(exe)


def create_new_key() -> None:
    try:
        private_key = generate_pem()  # type: ignore
        store_key(private_key)
    except BitPayException as exe:
        print(exe)


def store_key(private_key: str) -> None:
    global plain_private_key, private_key_path
    try:
        print("Select the way you want to store your private key:")
        input_value = input(
            "Press F for storing in a pem file or T for plain text in your config file: "
        )

        if input_value.lower() == "f":
            with open(str(private_key_path), "wb") as f:
                f.write(private_key.encode())
            plain_private_key = None
            print("Private key saved at path:", private_key_path)
            select_tokens(private_key)
        elif input_value.lower() == "t":
            plain_private_key = private_key
            private_key_path = None
            print("Saving private key... \n")
            select_tokens(private_key)
        else:
            store_key(private_key)
    except BitPayException as exe:
        print(exe)


def select_tokens(private_key: str) -> None:
    try:
        print("Select the tokens that you would like to request:")
        input_value = input("Press M for merchant, P for payout, or B for both: \n")
        if input_value.lower() in ["m", "p", "b"]:
            print("Requesting Tokens... \n")
            request_tokens(input_value.lower(), private_key)
        else:
            select_tokens(private_key)
    except BitPayException as exe:
        print(exe)


def request_tokens(token_type: str, private_key: str) -> None:
    global merchant_token
    global payout_token

    try:
        sin = get_sin_from_pem(private_key)  # type: ignore
        url = "%s/tokens" % api_url
        headers = {"content-type": "application/json", "X-accept-version": "2.0.0"}

        if token_type in ["m", "b"]:
            print("Requesting Merchant token... \n")
            facade = "merchant"
            payload = {"id": sin, "facade": facade}

            response = requests.post(
                url, verify=True, data=json.dumps(payload), headers=headers
            )
            if response.ok:
                merchant_token = response.json()["data"][0]["token"]
                print("Merchant Token: ", response.json()["data"][0]["token"])
                print(
                    "Merchant Token Pairing Code: ",
                    response.json()["data"][0]["pairingCode"] + "\n",
                )

        if token_type in ["p", "b"]:
            print("Requesting Payout token... \n")
            facade = "payout"
            payload = {"id": sin, "facade": facade}

            response = requests.post(
                url, verify=True, data=json.dumps(payload), headers=headers
            )
            if response.ok:
                payout_token = response.json()["data"][0]["token"]
                print("Payout Token: ", response.json()["data"][0]["token"])
                print(
                    "Payout Token Pairing Code: ",
                    response.json()["data"][0]["pairingCode"] + "\n",
                )

        update_config_file()
    except BitPayException as exe:
        print(exe)


def update_config_file() -> None:
    try:
        config = {
            "BitPayConfiguration": {
                "Environment": environment,
                "EnvConfig": {
                    environment: {
                        "PrivateKeyPath": private_key_path,
                        "PrivateKey": plain_private_key,
                        "ApiTokens": {
                            "merchant": merchant_token,
                            "payout": payout_token,
                        },
                        "proxy": proxy,
                    }
                },
            }
        }

        with open(os.path.abspath("bitpay.config.json"), "w") as outfile:
            json.dump(config, outfile, indent=2)
            print(
                "Generated configuration file at path: ",
                os.path.abspath("bitpay.config.json"),
            )

        print("Configuration generated successfully! \n")
        print(
            "\r\nPlease, copy the above pairing code/s and approve on your BitPay Account at the following link:\r\n"
        )
        print(f"{api_url}/dashboard/merchant/api-tokens\r\n")
        print(
            "\r\nOnce you have this Pairing Code/s approved you can move the generated files to a secure location "
            "and start using the Client.\r\n"
        )
    except BitPayException as exe:
        print(exe)


def load_key(path: str) -> None:
    global private_key_path

    private_key_path = path
    if not os.path.exists(private_key_path):
        print("Please set correct private key path! \n")
        pass

    with open(os.path.abspath(private_key_path), "r") as private_key:
        select_tokens(private_key.read())


if __name__ == "__main__":
    select_env()
