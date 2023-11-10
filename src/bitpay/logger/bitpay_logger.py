class BitPayLogger:
    def log_request(self, method: str, endpoint: str, json: dict) -> None:
        pass

    def log_response(self, method: str, endpoint: str, json: dict) -> None:
        pass

    def log_error(self, message: str) -> None:
        pass
