import requests
import random
import json
import PySimpleGUI as gui
welcomeLayout = [
    [gui.Text("Loading Question...", font=("Arial", 48))]
]
mainWindow = gui.Window("Pop Quiz!", welcomeLayout)
mainWindow.finalize()
print("CALLING")
req = requests.get("https://opentdb.com/api.php?amount=1")
print("GOT THIS FAR")

question = json.loads(req.text)
questionType = question["results"][0]["type"]
questionText = question["results"][0]["question"]

answers = question["results"][0]["incorrect_answers"]
answers.append(question["results"][0]["correct_answer"])
random.shuffle(answers)
correctAns = question["results"][0]["correct_answer"]

layout = [[gui.Text(questionText)]]
if questionType == "multiple":
    layout = [[gui.Text(questionText)],
              [gui.Radio(answers[0], 0)],
              [gui.Radio(answers[1], 0)],
              [gui.Radio(answers[2], 0)],
              [gui.Radio(answers[3], 0)],
              [gui.Button("Check")]
              ]


else:
    layout = [
        [gui.Text(questionText)],
        [gui.Radio(answers[0], 0)],
        [gui.Radio(answers[1], 0)],
        [gui.Button("Check")]
    ]

mainWindow.close()
mainWindow = gui.Window("PopQuiz!", layout=layout)
print("SHOULD SHOW")


while True:
    events, values = mainWindow.read()
    print(events, values)
    print(type(events))
    if events == gui.WIN_CLOSED or events == 'Exit':
        break

mainWindow.close()
