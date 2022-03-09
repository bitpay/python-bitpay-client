# Using the BitPay Python client

This SDK provides a convenient abstraction of BitPay's [cryptographically-secure API](https://bitpay.com/api) and allows payment gateway developers to focus on payment flow/e-commerce integration rather than on the specific details of client-server interaction using the API.  This SDK optionally provides the flexibility for developers to have control over important details, including the handling of private keys needed for client-server communication.

It also implements BitPay's remote client authentication and authorization strategy.  No private or shared-secret information is ever transmitted over the wire.


- [Dependencies](GUIDE.md#dependencies)
- [Installation](GUIDE.md#installation)
  - [Handling your client private key](GUIDE.md#handling-your-client-private-key)
  - [Initializing your BitPay client](GUIDE.md#initializing-your-BitPay-client)
  - [Pair your client with BitPay](GUIDE.md#pair-your-client-with-BitPay)
- [Getting Started](GUIDE.md#getting-started)
  - [Invoice](docs/invoice.md)
  - [Bill](docs/bill.md)
  - [Ledger](docs/ledger.md)
  - [Payout Recipient](docs/payout-recipient.md)
  - [Payouts](docs/payouts.md)
  - [Payout Batch](docs/payout-batch.md)
  - [Rate](docs/rate.md)
  - [Refunds](docs/refunds.md)
  - [Settlement](docs/settlement.md)
  - [Wallet](docs/wallet.md)
  - [Errors](docs/errors.md)
- [Copyright](GUIDE.md#copyright)

## Dependencies

You must have a BitPay merchant account to use this SDK.  It's free to [sign-up for a BitPay merchant account](https://bitpay.com/start).

If you need a test account, please visit https://test.bitpay.com/dashboard/signup and register for a BitPay merchant test account. Please fill in all questions, so you get a fully working test account.
If you are looking for a testnet bitcoin wallet to test with, please visit https://bitpay.com/wallet and
create a new wallet.
If you need testnet bitcoin please visit a testnet faucet, e.g. https://testnet.coinfaucet.eu/en/ or http://tpfaucet.appspot.com/

For more information about testing, please see https://bitpay.com/docs/testing

## Installation

### Manual
1. Download the package and extract it into a local directory or clone the repo.
2. cd into the root directory where setup.py is located 
3. Enter: python setup.py install

### Using pip
pip install bitpay

### Handling your client private key

Each client paired with the BitPay server requires a ECDSA key. This key provides the security mechanism for all client interaction with the BitPay server. The public key is used to derive the specific client identity that is displayed on your BitPay dashboard. The public key is also used for securely signing all API requests from the client. See the [BitPay API](https://bitpay.com/api/) for more information.

The private key should be stored in the client environment such that it cannot be compromised. If your private key is compromised you should revoke the compromised client identity from the BitPay server and re-pair your client, see the [API tokens](https://bitpay.com/api-tokens) for more information.

To generate the configuration file required to load the SDK:

The [BitPay Config Generator](setup/bitpay_setup.py) helps to generate the private key, as well as a environment file formatted in JSON or YML which contains all configuration requirements, that should be stored in the client local file system. It is not recommended to transmit the private key over any public or unsecure networks.

The comments in this script will assist you to create the environment file which you will be able to modify it later.

Once the Config Generator has run and generated the Json/Yml correctly, read the console output and follow the instructions in order to pair your new tokens.

You can find bitpay_setup.py file at `bitpay/bitpay_setup.py` under site-packages in your system

```json

{
  "BitPayConfiguration": {
    "Environment": "",
    "EnvConfig": {
      "Test": {
        "PrivateKeyPath": "",
        "PrivateKey": "",
        "ApiTokens": {
          "merchant": "",
          "payout": ""
        },
        "proxy": "" 
      }
    }
  }
}
```

### Initializing your BitPay client

Once you have the environment file (JSON previously generated) you can initialize the client in two ways:

```python
from bitpay.client import Client

bitpay = Client(config_file_path)
```

```python
from bitpay.client import Client

bitpay = Client(None, environment, private_key_path, tokens)
```

### Pair your client with BitPay

Your client must be paired with the BitPay server. The pairing initializes authentication and authorization for your client to communicate with BitPay for your specific merchant account.

Pairing is accomplished by running the bitpay [python Setup]((setup/bitpay_setup.py)) utility request a pairing code from the BitPay server.
Meanwhile a new pairing code is generated, the python Setup utility will ask you to activate it in your BitPay account. It will also store the paired token in the environment file.

The pairing code is then entered into the BitPay merchant dashboard for the desired merchant.  Your interactive authentication at https://bitpay.com/login provides the authentication needed to create finalize the client-server pairing request.

## Copyright
Copyright (c) 2019 BitPay

See also the tests project for more examples of API calls.
