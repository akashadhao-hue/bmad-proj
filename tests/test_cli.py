import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [sys.executable, "-c", "from base64_tool.cli import main; main()", *args],
        capture_output=True,
        check=False,
    )


def test_encode_utf8_text():
    result = run_cli("encode", "héllo")

    assert result.returncode == 0
    assert result.stdout == b"aMOpbGxv\n"


def test_decode_to_bytes():
    result = run_cli("decode", "/wAB")

    assert result.returncode == 0
    assert result.stdout == b"\xff\x00\x01"


def test_decode_rejects_invalid_base64():
    result = run_cli("decode", "not base64!")

    assert result.returncode != 0
    assert b"invalid Base64 input" in result.stderr
