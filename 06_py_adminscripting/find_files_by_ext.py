from pathlib import Path

__author__ = "Benedikt theuretzbachner"


path = Path(input("[filepath]> "))
if not path.is_dir():
    raise Exception("Path must be an existing directory")

suffix = input("[file-extension]> ")
if not suffix.startswith("."):
    suffix = "." + suffix


for file_path in path.rglob(f"*{suffix}"):
    print(file_path)
