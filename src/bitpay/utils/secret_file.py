import os

SECRET_FILE_MODE = 0o600


def write_secret_file(path: str, content: str) -> None:
    """
    Writes a file that holds secrets (private key, API tokens) so only the owner
    can read and write it.

    The mode given to os.open only applies when the file is created. If the file
    already exists, for example from an older setup run, its permissions are
    tightened before and after writing. On Windows, chmod only controls the
    read-only flag, so this has no effect there.
    """
    if os.path.exists(path):
        os.chmod(path, SECRET_FILE_MODE)

    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | getattr(os, "O_BINARY", 0)
    fd = os.open(path, flags, SECRET_FILE_MODE)
    with os.fdopen(fd, "wb") as file:
        file.write(content.encode("utf-8"))

    os.chmod(path, SECRET_FILE_MODE)
