import csv
import sys

with open("./quizy.csv", newline="") as fle:
    quizy = list(csv.DictReader(fle, delimiter=";", quotechar='"'))

if not len(sys.argv) > 1:
    print("Podaj uid quizu")
    exit()

quiz_uid = sys.argv[1]

quiz_data = [row for row in quizy if row["uid"] == quiz_uid]

for row in quiz_data:
    print(row["question"])
