import argparse

from cryptscripts import caesar, kasiski

__author__ = "Benedikt Theuretzbchner"

parser = argparse.ArgumentParser(
    description="cvcrypt - Caesar & Vigenere encrypter / decrypter by Benedikt / HTL Rennweg"
)


def add_positional_args():
    parser.add_argument("infile", help="Zu verschlüsselnde Datei")
    parser.add_argument("outfile", nargs="?", help="Zieldatei")


def add_options():
    parser.add_argument(
        "-c",
        "--cypher",
        type=str,
        choices=["caesar", "c", "vigenere", "v"],
        help="Zu verwendende Chiffre",
    )


if __name__ == "__main__":
    add_positional_args()
    add_options()
    args = parser.parse_args()
