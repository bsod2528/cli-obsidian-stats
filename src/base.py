import os
import hashlib

MVOG_DIR: str = ".mvog"


def hash_object(data, type_="blob"):
    obj = type_.encode() + b"\x00" + data
    oid = hashlib.sha1(obj).hexdigest()

    with open(f"{os.getcwd()}/{MVOG_DIR}/blobs/{oid}", "wb") as out:
        out.write(obj)

    return oid
