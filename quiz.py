import csv
import sys

with open("./quizy.csv", newline="") as fle:
    quizy = list(csv.DictReader(fle, delimiter=";", quotechar='"'))

if not len(sys.argv) > 1:
    print("Podaj uid quizu")
    exit()

quiz_uid = sys.argv[1]

quiz_data = [row for row in quizy if row["uid"] == quiz_uid]

questions = {}
for row in quiz_data:
    if not row["question"] in questions:
        questions[row["question"]] = []
    questions[row["question"]].append(row["answer"])

for question, answers in questions.items():
    print(f"Pytanie: { question }")
    for i, answer in enumerate(answers):
        print(f"\t{i + 1} - {answer}")
    user_answer = input("Podaj odpowiedź: ")
    if not user_answer.isdigit():
        print("Nie podałeś liczby!!!")
        continue

    answer_text = answers[int(user_answer) - 1]

    for a in quiz_data:
        if a["answer"] == answer_text:
            if int(a["is_true"]):
                print("****** Dobra odpowiedź *******")
            else:
                print("!!!!!! Zła odpowiedź !!!!!!")
