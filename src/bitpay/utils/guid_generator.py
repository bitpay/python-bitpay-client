from uuid import uuid4


class GuidGenerator:
    def execute(self) -> str:
        return str(uuid4())
