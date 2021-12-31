import os
import sys
import json
import requests

# TODO: Need to remove below 2 lines
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(root_dir))

from src.bitpay_sdk.utils.key_utils import *
from src.bitpay_sdk.exceptions.bitpay_exception import BitPayException

is_prod = False  # Set to true if the environment for which the configuration file will be generated is Production.
# Will be set to Test otherwise

private_key_name = 'private_key.pem'  # Add here the name for your Private key
generate_merchant_token = True  # Set to true to generate a token for the Merchant facade
generate_payout_token = True  # Set to true to generate a token for the Payout facade
your_master_password = 'YourMasterPassword'  # Will be used to encrypt your PrivateKey
proxy = None
base_url = 'https://bitpay.com' if is_prod else 'https://test.bitpay.com'
env = 'Prod' if is_prod else 'Test'
merchant_token = None
payout_token = None

root_path = os.path.abspath(os.curdir)

try:
    private_key = generate_pem()
    with open(os.path.join(root_path, private_key_name), "wb") as f:
        f.write(private_key.encode())
except BitPayException as e:
    print(e)

# Generate the public key from the private key every time (no need to store the public key).
try:
    public_key = get_compressed_public_key_from_pem(private_key)
except BitPayException as e:
    print(e)

try:
    sin = get_sin_from_pem(private_key)
except BitPayException as e:
    print(e)

try:
    if generate_merchant_token:
        facade = 'merchant'
        payload = {'id': sin, 'facade': facade}

        url = base_url + "/tokens"
        headers = {"content-type": "application/json", "X-accept-version": "2.0.0"}
        response = requests.post(url, verify=True, data=json.dumps(payload), headers=headers)

        if response.ok:
            merchant_token = response.json()['data'][0]['token']
            print("Merchant Token: ", response.json()['data'][0]['token'])
            print("Merchant Token Pairing Code: ", response.json()['data'][0]['pairingCode'])

    if generate_payout_token:
        facade = 'payout'
        payload = {'id': sin, 'facade': facade}

        url = base_url + "/tokens"
        headers = {"content-type": "application/json", "X-accept-version": "2.0.0"}
        response = requests.post(url, verify=True, data=json.dumps(payload), headers=headers)

        if response.ok:
            payout_token = response.json()['data'][0]['token']
            print("Payout Token: ", response.json()['data'][0]['token'])
            print("Payout Token Pairing Code: ", response.json()['data'][0]['pairingCode'])

except BitPayException as e:
    print(e)

print("\r\nPlease, copy the above pairing code/s and approve on your BitPay Account at the following link:\r\n")
print(f"{base_url}/dashboard/merchant/api-tokens\r\n")
print("\r\nOnce you have this Pairing Code/s approved you can move the generated files to a secure location and start "
      "using the Client.\r\n")

# Generate config file
config = {
    "BitPayConfiguration": {
        "Environment": env,
        "EnvConfig": {
            "Test": {
                "PrivateKeyPath": None if is_prod else os.path.abspath("private_key.pem"),
                "PrivateKeySecret": None if is_prod else your_master_password,
                "ApiTokens": {
                    "merchant": None if is_prod else merchant_token,
                    "payout": None if is_prod else payout_token
                },
                "proxy": proxy
            },
            "Prod": {
                "PrivateKeyPath": os.path.abspath("private.pem") if is_prod else None,
                "PrivateKeySecret": your_master_password if is_prod else None,
                "ApiTokens": {
                    "merchant": merchant_token if is_prod else None,
                    "payout": payout_token if is_prod else None
                },
                "proxy": proxy
            }
        }
    }
}

try:
    with open(os.path.abspath("bitpay.config.json"), 'w') as outfile:
        json.dump(config, outfile)
except BitPayException as e:
    print(e)
