from Model.connection import *

class Model():

    def __init__(self):
        self.choice = None
        self.choice = connection()

    def model.message(self):
        self.choice.initialize_connection()
        self.choise.cursor.execute("SELECT * FROM Messages;")
        view = self.choice.cursor.fetchall()
        self.choice.close_connection()
        return view

    def write_message(self, content, author):
        self.choice.initialize_connection()
        self.choice.cursor.execute("INSERT INTO Messages(content, publishing_date, author) VALUE (%s, NOM(), %s);", (content, author))
        self.choice.connection.commit()
        self.choice.close_connection()