from pathlib import Path

__author__ = "Benedikt theuretzbachner"


p = Path(input("Enter filepath > "))
if not p.parent.exists():
    print("Parent directory does not exist!")
    exit(1)

print(f"name: {p.name}")
print(f"stem: {p.stem}")
print(f"suffix: {p.suffix}")
print(f"anchor: {p.anchor}")
print(f"parent: {p.parent}")
