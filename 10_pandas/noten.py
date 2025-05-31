#!/bin/python

import argparse
import re
import pandas as pd

__author__ = "Benedikt Theuretzbachner"

parser = argparse.ArgumentParser(
    description="noten.py by Benedikt Theuretzbachner / HTL Rennweg"
)


def add_args() -> None:
    parser.add_argument("outfile", help="Ausgabedatei (z.B. result.csv)")

    parser.add_argument("-n", required=True, help="csv-Datei mit den Noten")
    parser.add_argument("-s", required=True, help="xml-Datei mit den Schülerdaten")
    parser.add_argument(
        "-m", help="Name der Spalte, die zu verknüpfen ist (default = Nummer)"
    )
    parser.add_argument("-f", help="Name des zu filternden Gegenstandes (z.B. SEW)")

    output = parser.add_mutually_exclusive_group()
    output.add_argument(
        "-v", "--verbose", action="store_true", help="Gibt die Daten Kommandozeile aus"
    )
    output.add_argument("-q", "--quiet", action="store_true", help="keine Textausgabe")


def read_xml(filename: str) -> pd.DataFrame:
    with open(filename) as f:
        content = f.read()

    result = []

    student_pattern = re.compile(r"<Schueler>.*?</Schueler>", flags=re.DOTALL)
    students = re.findall(student_pattern, content)

    student_data_pattern = re.compile(
        r"<(Nummer|Anrede|Vorname|Nachname|Geburtsdatum)>(.*)</\1>"
    )
    for s in students:
        student_data = map(lambda t: t[1], re.findall(student_data_pattern, s))
        result.append(student_data)

    df = pd.DataFrame(
        result,
        columns=["Nummer", "Anrede", "Vorname", "Nachname", "Geburtsdatum"],
        dtype=str,
    )

    return df


if __name__ == "__main__":
    add_args()

    args = parser.parse_args()

    df_grades = pd.read_csv(args.n, sep=";").astype(str)
    df_grades.set_index("Nummer", inplace=True)
    df_students = read_xml(args.s).astype(str)
    df_students.set_index("Nummer", inplace=True)

    df_joined = df_grades.join(df_students, how="outer", on="Nummer")
    print(df_joined)
