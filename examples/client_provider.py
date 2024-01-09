from bitpay.client import Client


class ClientProvider:

    @staticmethod
    def create() -> Client:
        return Client.create_client_by_config_file_path("some/path")
