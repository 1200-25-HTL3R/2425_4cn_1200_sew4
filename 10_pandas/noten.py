#!/bin/python

import argparse

__author__ = "Benedikt Theuretzbachner"

parser = argparse.ArgumentParser(
    description="noten.py by Benedikt Theuretzbachner / HTL Rennweg"
)


def add_args() -> None:
    parser.add_argument("outfile", help="Ausgabedatei (z.B. result.csv)")

    parser.add_argument("-n", help="csv-Datei mit den Noten")
    parser.add_argument("-s", help="xml-Datei mit den Schülerdaten")
    parser.add_argument(
        "-m", help="Name der Spalte, die zu verknüpfen ist (default = Nummer)"
    )
    parser.add_argument("-f", help="Name des zu filternden Gegenstandes (z.B. SEW)")

    output = parser.add_mutually_exclusive_group()
    output.add_argument(
        "-v", "--verbose", action="store_true", help="Gibt die Daten Kommandozeile aus"
    )
    output.add_argument("-q", "--quiet", action="store_true", help="keine Textausgabe")


if __name__ == "__main__":
    add_args()

    parser.parse_args()
