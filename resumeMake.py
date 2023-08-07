# This script is supposed to take job description and make a resume according to it.
import openai
import sys
import pandas as pd
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtWidgets import QApplication, QDialog, QFormLayout
from PyQt6.QtWidgets import (QPushButton, QLineEdit, QPlainTextEdit)
from PyQt6.QtCore import QObject, QUrl, pyqtSignal, pyqtSlot, QThread



# Your OPENAI_API_KEY
openai.api_key = "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"
prompt_text = pd.read_csv("prompt.csv", encoding="cp1252")
# job_text["prompt1"][0] - first part of prompt
# job_text["prompt2"][0] - second part of prompt
PROMPT1 = prompt_text["prompt1"][0]
PROMPT2 = prompt_text["prompt2"][0]
# class worker(QObject):
#     finished = pyqtSignal()
#     progress = pyqtSignal(int)

#     def run(self):
#         "Long running tasks"


class Form(QDialog):
    
    
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.le = QPlainTextEdit()
        self.le.setObjectName("host")
        # self.le.setText("Host")

        self.pb = QPushButton()
        self.pb.setObjectName("connect")
        self.pb.setText("GENERATE RESUME")
        self.pb.clicked.connect(self.button_click)

        layout = QFormLayout()
        layout.addWidget(self.le)
        layout.addWidget(self.pb)
        self.setLayout(layout)
        self.setGeometry(100, 50, 800, 800)
        self.setWindowTitle("Resume AI")
    
    def get_gpt_response(self, message):
        prompt=[
            {"role": "system", "content": "You are a professional technical resume writer",
             "role": "user", "content":message}]
        response = openai.ChatCompletion.create(
          model = "gpt-4",
          messages = prompt,
          temperature=1,
          max_tokens=5000,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
        )
        return response.choices[0].message.content

    def make_resume(self, jd):
        # This function takes job description and makes a resume according to it.
        # jd - job description
        # resume - resume
        prompt = PROMPT1 + jd + PROMPT2
        resume = self.get_gpt_response(prompt)
        self.le.setPlainText(resume)

    def button_click(self):
        # jd(job description) is a QString object
        jd = self.le.toPlainText()
        self.make_resume(jd)

    
if __name__ == '__main__':
    QQuickWindow.setSceneGraphBackend('software')
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec()
    engine = QQmlApplicationEngine()
