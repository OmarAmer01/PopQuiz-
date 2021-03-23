import requests
import random
import json
import PySimpleGUI as gui
import time

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

score = 0
scoreText = "Score " + str(score)

layout = [[gui.Text(questionText)]]
if questionType == "multiple":
    layout = [[gui.Text(questionText)],
              [gui.Radio(answers[0], 0, key=1)],
              [gui.Radio(answers[1], 0, key=2)],
              [gui.Radio(answers[2], 0, key=3)],
              [gui.Radio(answers[3], 0, key=4)],
              [gui.Button("Check")], [gui.Text(scoreText, justification='center', key=-1)]

              ]


else:
    layout = [
        [gui.Text(questionText)],
        [gui.Radio(answers[0], 0, key=1)],
        [gui.Radio(answers[1], 0, key=2)],
        [gui.Button("Check")],
        [gui.Text(scoreText, justification='center', key=-1)]
    ]

mainWindow.close()
mainWindow = gui.Window("PopQuiz!", layout=layout)
print("SHOULD SHOW")

layout.append([gui.Text(scoreText, justification='center')])
selectedIndex = -1
ansIndex = -1
while True:
    events, values = mainWindow.read()
    if events == "Check":
        for i in range(len(answers)):
            if answers[int(i)] == correctAns:
                ansIndex = i
                break
        for i in range(1, len(values) + 1):
            if values[i]:
                selectedIndex = i
                break
        if selectedIndex != -1:
            for i in range(1, len(answers) + 1):
                mainWindow[i].update(text_color='red')
            mainWindow[ansIndex+1].update(text_color='green')

    if selectedIndex != -1:
        if correctAns == answers[selectedIndex - 1]:
            print("CORRECT")
            score += 1
            scoreText = "Score " + str(score)
            mainWindow[-1].update(scoreText)

        else:
            print("Incorrect, answer is", correctAns)

    if events == gui.WIN_CLOSED or events == 'Exit':
        break

mainWindow.close()
