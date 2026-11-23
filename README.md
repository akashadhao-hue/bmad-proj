# Base64 Tool

A small command-line utility for encoding UTF-8 text as Base64 and decoding
Base64 into its original bytes. It is managed with [uv](https://docs.astral.sh/uv/).

## Usage

```sh
uv sync
uv run base64-tool encode "hello"
# aGVsbG8=

uv run base64-tool decode aGVsbG8=
# hello
```

Decoding writes bytes directly to standard output, so binary data is preserved.
Redirect output to a file when needed:

```sh
uv run base64-tool decode <base64-value> > output.bin
```
