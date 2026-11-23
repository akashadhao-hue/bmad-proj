import argparse
import base64
import binascii
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description="Encode or decode Base64.")
    commands = parser.add_subparsers(dest="operation", required=True)

    encode = commands.add_parser("encode", help="Encode UTF-8 text")
    encode.add_argument("value", help="Text to encode")

    decode = commands.add_parser("decode", help="Decode Base64 to bytes")
    decode.add_argument("value", help="Base64 text to decode")

    args = parser.parse_args()

    if args.operation == "encode":
        result = base64.b64encode(args.value.encode("utf-8")).decode("ascii")
        print(result)
        return

    try:
        result = base64.b64decode(args.value, validate=True)
    except binascii.Error as error:
        parser.error(f"invalid Base64 input: {error}")

    sys.stdout.buffer.write(result)
