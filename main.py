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
              [gui.Radio(answers[0], 0, key=1)],
              [gui.Radio(answers[1], 0, key=2)],
              [gui.Radio(answers[2], 0, key=3)],
              [gui.Radio(answers[3], 0, key=4)],
              [gui.Button("Check")]
              ]


else:
    layout = [
        [gui.Text(questionText)],
        [gui.Radio(answers[0], 0, key=1)],
        [gui.Radio(answers[1], 0, key=2)],
        [gui.Button("Check")]
    ]

mainWindow.close()
mainWindow = gui.Window("PopQuiz!", layout=layout)
print("SHOULD SHOW")


selectedIndex = -1
while True:
    events, values = mainWindow.read()
    if events == "Check":

        for i in range(1, len(values)):
            if values[i]:
                selectedIndex = i
                break
    if correctAns == answers[selectedIndex]:
        print("CORRECT")
    else:
        print("Incorrect, answer is", correctAns)
    mainWindow[selectedIndex].update(text_color='red')
    if events == gui.WIN_CLOSED or events == 'Exit':
        break

mainWindow.close()
