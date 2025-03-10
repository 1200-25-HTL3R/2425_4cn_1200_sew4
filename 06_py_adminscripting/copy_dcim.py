#!/bin/python

import os
from pathlib import Path
import re
import shutil

__author__ = "Benedikt theuretzbachner"


src_path = Path(input("[source path]> "))
if not src_path.is_dir():
    raise Exception("Path must be an existing directory")

dest_path = Path(input("[destination path]> "))
if not dest_path.is_dir():
    raise Exception("Path must be an existing directory")

img_pattern = re.compile(r"\d{8}_\d{6}.*")
for img_path in src_path.rglob("*.jpg"):
    if img_pattern.fullmatch(img_path.stem):
        img_dest_path = Path(
            f"{dest_path}/{img_path.stem[:4]}/{img_path.stem[4:6]}/{img_path.stem[6:8]}/{img_path.name}"
        )
        os.makedirs(img_dest_path, exist_ok=True)
        shutil.copy2(img_path, img_dest_path)
        print(f"copied: {img_path} -> {img_dest_path}")
