from kahoot import KahootClient
import asyncio
import logging 
import io
import sys
import re
import resources_rc
import time
from kahoot.packets.impl.respond import RespondPacket
from kahoot.packets.server.game_over import GameOverPacket
from kahoot.packets.server.game_start import GameStartPacket
from kahoot.packets.server.question_end import QuestionEndPacket
from kahoot.packets.server.question_ready import QuestionReadyPacket
from kahoot.packets.server.question_start import QuestionStartPacket
from kahoot.util.solver import solve_challenge
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QGraphicsOpacityEffect

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 583)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 7, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 168, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 151, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 181, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 118, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 7, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 136, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 168, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 151, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 53, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 181, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 181, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 168, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 136, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 168, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 151, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 168, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 168, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 181, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 89, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setWindowOpacity(0.9)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 851, 581))
        self.frame.setStyleSheet("background-color: rgb(197, 174, 255);border: 2px solid rgb(119, 99, 143);border-radius: 25px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.header = QtWidgets.QLabel(self.frame)
        self.header.setGeometry(QtCore.QRect(0, 0, 851, 30))
        self.header.setObjectName("header")
        self.header.setText("")
        self.header.setStyleSheet("background-color: #916cff;\n border-radius: 5px;")
        self.header.mouseMoveEvent = self.mouseMoveEvent
        self.exitbuten = QtWidgets.QPushButton(self.frame)
        self.exitbuten.setGeometry(QtCore.QRect(780, 10, 15, 15))
        self.exitbuten.setStyleSheet("color: rgba(255, 255, 255, 0);\n"
"background-color: rgb(95, 0, 0);\n"
"border-radius: 5px;")
        self.minimiz = QtWidgets.QPushButton(self.frame)
        self.minimiz.setGeometry(QtCore.QRect(760, 10, 15, 15))
        self.minimiz.setStyleSheet("color: rgba(255, 255, 255, 0);\n"
"background-color: #ffda46;\n"
"border-radius: 5px;")
        
        self.graphicsView = QtWidgets.QLabel(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(30, 50, 791, 471))
        self.graphicsView.setText("")
        self.graphicsView.setObjectName("graphicsView")
        #pixmap = QtGui.QPixmap(":/Hakoot.png")
        #scaled_pixmap = pixmap.scaled(900, 600, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        #self.graphicsView.setPixmap(scaled_pixmap)
        self.graphicsView.setStyleSheet("""                                                                                                                 
        border-image: url(:/Hakoot.png);                                                                                                      
        background-color: black;                                                                                                          
        border-radius: 50%;                                                                                                                 
        """)
        #self.graphicsView.setStyleSheet("border: 2px solid rgb(170, 160, 212);border-radius: 50px;")
        self.TitleLabel = QtWidgets.QLabel(self.frame)
        self.TitleLabel.setGeometry(QtCore.QRect(70, 50, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        font.setUnderline(True)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.TitleLabel.setAttribute(Qt.WA_TranslucentBackground)
        self.TitleLabel.setStyleSheet("color: rgb(0,0,0)")
        self.CreditLabel = QtWidgets.QLabel(self.frame)
        self.CreditLabel.setGeometry(QtCore.QRect(640, 525, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.CreditLabel.setFont(font)
        self.CreditLabel.setObjectName("CreditLabel")
        self.CreditLabel.setStyleSheet("color: rgb(0,0,0)")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(420, 130, 381, 371))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("color: rgb(0,0,0); background-color: rgb(211, 196, 255);border: 2px solid rgb(154, 137, 190);border-radius: 20px;")
        self.opacity_effect = QGraphicsOpacityEffect() 
  
        # setting opacity level 
        self.opacity_effect.setOpacity(0.6) 
  
        # adding opacity effect to the label 
        self.textBrowser.setGraphicsEffect(self.opacity_effect)
        self.gamepinlabel = QtWidgets.QLabel(self.frame)
        self.gamepinlabel.setGeometry(QtCore.QRect(430, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.gamepinlabel.setFont(font)
        self.gamepinlabel.setObjectName("gamepinlabel")
        self.gamepinlabel.setAttribute(Qt.WA_TranslucentBackground)
        self.gamepinlabel.setStyleSheet("color: rgb(0,0,0)")
        self.gamepinchange = QtWidgets.QLabel(self.frame)
        self.gamepinchange.setGeometry(QtCore.QRect(520, 103, 201, 26))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.gamepinchange.setFont(font)
        self.gamepinchange.setObjectName("gamepinchange")
        self.gamepinchange.setAttribute(Qt.WA_TranslucentBackground)
        self.gamepinchange.setStyleSheet("color: rgb(0,0,0)")
        self.Gamepin_LineEdit = QtWidgets.QLineEdit(self.frame)
        self.Gamepin_LineEdit.setGeometry(QtCore.QRect(250, 300, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Gamepin_LineEdit.setFont(font)
        self.Gamepin_LineEdit.setObjectName("Gamepin_LineEdit")
        self.Gamepin_LineEdit.setStyleSheet("color: rgb(0,0,0); background-color: #f0f0f0;border: 2px solid #8f8f91;border-radius: 10px;")
        self.Name_LineEdit = QtWidgets.QLineEdit(self.frame)
        self.Name_LineEdit.setGeometry(QtCore.QRect(250, 339, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Name_LineEdit.setFont(font)
        self.Name_LineEdit.setObjectName("Name_LineEdit")
        self.Name_LineEdit.setStyleSheet("color: rgb(0,0,0); background-color: #f0f0f0;border: 2px solid #8f8f91;border-radius: 10px;")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 300, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelOpacity = QGraphicsOpacityEffect()
        self.labelOpacity.setOpacity(0.9)
        self.label.setGraphicsEffect(self.labelOpacity)
        self.label.setStyleSheet("color: rgb(0,0,0); border: 2px solid #8f8f91;border-radius: 10px;")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 340, 111, 20))
        self.label_2Opacity = QGraphicsOpacityEffect()
        self.label_2Opacity.setOpacity(0.9)
        self.label_2.setGraphicsEffect(self.label_2Opacity)
        self.label_2.setStyleSheet("color: rgb(0,0,0); border: 2px solid #8f8f91;border-radius: 10px;")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(160, 390, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("color: rgb(0,0,0); background-color: #f0f0f0;border: 2px solid #8f8f91;border-radius: 10px;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.exitbuten.clicked.connect(sys.exit)
        self.minimiz.clicked.connect(MainWindow.showMinimized)
        self.pushButton.clicked.connect(self.run_async_task)

        self.worker = AsyncWorker(self)
        self.worker.finished.connect(self.on_finished)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HAKOOT"))
        self.TitleLabel.setText(_translate("MainWindow", "KAHOOT BOT DEMON TIME "))
        self.CreditLabel.setText(_translate("MainWindow", "Made by Jett Routh"))
        self.gamepinlabel.setText(_translate("MainWindow", "Game Pin: "))
        self.gamepinchange.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Enter Game Pin"))
        self.label_2.setText(_translate("MainWindow", "Enter Name"))
        self.pushButton.setText(_translate("MainWindow", "OK"))

    def run_async_task(self):
        #self.textBrowser.append("Button Pressed!")
        self.worker.start()
        #asyncio.create_task(self.main())
    
    def on_finished(self):
        print("async task finished")

    

    logging.basicConfig(level=logging.DEBUG)
    


#JOIN_TIMEOUT = 30  
class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        
    def mousePressEvent(self, event):                                
        self.dragPos = event.globalPos()
       
    def mouseMoveEvent(self, event):                                  
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

        
#async def joinHandle(username):
   # print(f"bot: {username} has joined")
httpcore_log_buffer = io.StringIO()
httpcore_handler = logging.StreamHandler(httpcore_log_buffer)
httpcore_handler.setLevel(logging.DEBUG)

httpcore_logger = logging.getLogger("httpcore")
httpcore_logger.setLevel(logging.DEBUG)
httpcore_logger.addHandler(httpcore_handler)
httpcore_logger.propagate = False
class AsyncWorker(QtCore.QThread):
    game_started = False
    finished = QtCore.pyqtSignal()
    def __init__(self, Ui_MainWindow):
        super().__init__()
        self.Ui_MainWindow = Ui_MainWindow
        self.bot_client: KahootClient = KahootClient()

    def run(self):
        # Set the event loop for this thread
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.main())
        self.finished.emit()

    async def game_start(self, packet: GameStartPacket):
        print(f"Game started: {packet}")
        self.Ui_MainWindow.textBrowser.append(f"Game started: Amount of Questions: {packet.game_block_count}")

    async def game_over(self, packet: GameOverPacket):
        print(f"Game over: {packet}")
        self.Ui_MainWindow.textBrowser.append(f"Game Ended: ended with rank: {packet.rank} in {packet.quiz_title}")

    async def question_start(self, packet: QuestionStartPacket):
        print(f"Question started: {packet}")
        #self.Ui_MainWindow.textBrowser.append(f"Question started: {packet}")
        self.Ui_MainWindow.textBrowser.append(f"Question Number {packet.game_block_index}/{packet.total_game_block_count} Started")
        question_number: int = packet.game_block_index
        await self.bot_client.send_packet(RespondPacket(self.bot_client.game_pin, 1, question_number))

    async def question_end(self, packet: QuestionEndPacket):
        print(f"Question ended: {packet}")
        self.Ui_MainWindow.textBrowser.append(f"Question ended: Answer is Correct: {packet.is_correct}\nTotal Score: {packet.total_score}")
    async def question_ready(self, packet: QuestionReadyPacket):
        print(f"Question ready: {packet}")
        self.Ui_MainWindow.textBrowser.append(f"Question Number {packet.game_block_index}/{packet.total_game_block_count} ready")
        #self.Ui_MainWindow.textBrowser.append(f"Question ready: {packet}")
    async def getSessionId(self):
        #log_contents = httpcore_log_buffer.getvalue()
        #print(f"Captured Log Contents: {log_contents}")
        #self.Ui_MainWindow.textBrowser.append(f"Captured Log Contents: {log_contents}")
        #match = re.search(r"\(b'x-kahoot-session-token', b'([^']+)'\)", log_contents)
        #if match: 
        #    solve_challenge(match.group(1), )
        r = self.bot_client.http_client.get(
                f"https://kahoot.it/reserve/session/{self.bot_client.game_pin}/?{int(time.time())}"
            )
        session_token = r.headers['x-kahoot-session-token']
        #logger.debug(f"Session token: {session_token}, Solving challenge...")
        self.Ui_MainWindow.textBrowser.append(f"Session token: {session_token}")
        session_id = solve_challenge(session_token, r.json()["challenge"])
        #logger.debug(f"Session ID: {session_id}")
        self.Ui_MainWindow.textBrowser.append(f"Session id: {session_id}")
        
    async def main(self):
        join_status = {}
        #self.Ui_MainWindow.textBrowser.append("fasfafafafsafafasfa")
        print(f"{self.Ui_MainWindow.Gamepin_LineEdit.text()}")
        if self.Ui_MainWindow.Gamepin_LineEdit.text().isnumeric():
            newpin = self.Ui_MainWindow.Gamepin_LineEdit.text()
            pin: int = int(newpin)
        else:
            self.Ui_MainWindow.textBrowser.append("Game Pin Not Entered/Valid")
            return
        if self.Ui_MainWindow.Name_LineEdit.text() != "":
            newname = self.Ui_MainWindow.Name_LineEdit.text()
            name: str = newname
        else:
            self.Ui_MainWindow.textBrowser.append("No Valid Name Entered")
            return
        #limit: int = int(input("How many bots do you want in your game: "))
        self.Ui_MainWindow.pushButton.setDisabled(True)
        self.Ui_MainWindow.gamepinchange.setText(f"{newpin}")
        self.bot_client.on("game_start", self.game_start)
        self.bot_client.on("game_over", self.game_over)
        self.bot_client.on('question_start', self.question_start)
        self.bot_client.on("question_end", self.question_end)
        self.bot_client.on("question_ready", self.question_ready)
        #for i in range(limit):
        #bot_client: KahootClient = KahootClient()
        username = f"{name}"
        join_status[username] = False  
        self.Ui_MainWindow.textBrowser.append(f"Attempting to join game with bot: {username}")

        await asyncio.gather(self.bot_client.join_game(pin, username),self.getSessionId())
        #join_status[username] = True

        #print("\nFinal Join Statuses:")
        #for username, status in join_status.items():
        #    print(f"{username}: {'Joined' if status else 'Not Joined'}")
        #input("press anything to exit")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("HAKOOT")
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    w = MyWin()
    w.show()
    sys.exit(app.exec_())
    
    
