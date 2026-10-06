import os
import sys

import pytest

from bitpay.utils.secret_file import write_secret_file

# POSIX permissions do not apply on Windows.
posix_only = pytest.mark.skipif(
    sys.platform == "win32", reason="POSIX permissions do not apply on Windows"
)


@pytest.mark.unit
@posix_only
def test_creates_file_readable_only_by_owner(tmp_path):  # type: ignore
    file = tmp_path / "private_key.pem"

    write_secret_file(str(file), "abc")

    assert os.stat(file).st_mode & 0o777 == 0o600
    assert file.read_text() == "abc"


@pytest.mark.unit
@posix_only
def test_tightens_existing_file_with_wider_permissions(tmp_path):  # type: ignore
    file = tmp_path / "bitpay.config.json"
    file.write_text("old content that is longer")
    os.chmod(file, 0o644)

    write_secret_file(str(file), "new")

    assert os.stat(file).st_mode & 0o777 == 0o600
    assert file.read_text() == "new"


@pytest.mark.unit
@posix_only
def test_ignores_permissive_umask(tmp_path):  # type: ignore
    file = tmp_path / "private_key.pem"
    old_umask = os.umask(0)
    try:
        write_secret_file(str(file), "abc")
    finally:
        os.umask(old_umask)

    assert os.stat(file).st_mode & 0o777 == 0o600
