This app uses a kahoot library i found on the python package index, https://pypi.org/project/kahoot/ <--- heres the link for anyone interested

kahootbot.py holds all of the logic and stuff and is the main file
the rest of the files are resource files that hold images for the ui

im not sure which other libraries i used that dont come with python,
to be safe make sure you have these libraries
logging
sys
asyncio

and also install pyqt5 for the UI. 

Unfortunately, it is no longer possible to get the Quiz ID before the kahoot game ends, the quizID only being revealed after GameEnded event has triggered, which is too late. If anyone reading this is up for the task, try to incorporate some type of new way to get the quiz id or implement some type of ai to read the questions from information in the questionstart packet and get the answers from that. 
