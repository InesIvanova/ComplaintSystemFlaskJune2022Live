import base64


def decode_file(path, encoded_file):
    with open(path, "wb") as f:
        f.write(base64.b64decode(encoded_file.encode("utf-8")))