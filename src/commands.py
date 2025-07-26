import os
import time

import base

MVOG_DIR: str = ".mvog"


def _init() -> None:
    """Initialises mvog repository."""

    try:
        os.makedirs(f"{os.getcwd()}/{MVOG_DIR}")
        os.makedirs(f"{os.getcwd()}/{MVOG_DIR}/blobs")
        os.makedirs(f"{os.getcwd()}/{MVOG_DIR}/trees")

        with open(f"{MVOG_DIR}/config", "w") as config_file:
            config_file.write(f"created_at: {time.time()}\nroot_dir: {os.getcwd()}")

        with open(".mvogignore", "w") as mvog_ignore:
            mvog_ignore.write("")

        return print(f"Created a MVOG repository stored at: {os.getcwd()}/{MVOG_DIR}")
    except FileExistsError:
        return print(f"MVOG repository present at: {os.getcwd()}/{MVOG_DIR}")


def _commit() -> None:
    """Commit changes made to your repository."""

    paths: list[str] = os.listdir("./")
    ignored: list[str] = []

    with open(".mvogignore", "r") as ignored_content:
        for content in ignored_content:
            ignored.append(content.strip())

    for root, dirs, files in os.walk("."):
        dirs[:] = [x for x in dirs if x not in ignored]

        if any(ignored_dir in root for ignored_dir in ignored):
            continue

        for file in files:
            file_path = os.path.join(root, file)
            if any(ignored_file in file_path for ignored_file in ignored):
                continue
            base.hash_object(file)

_commit()
