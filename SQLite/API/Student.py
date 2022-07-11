import sqlite3

class STUDENT():
    def __init__(self, name, CLASS, section ):
        self.name = name
        self.CLASS = CLASS
        self.section = section
    def get_full_name(self):
        return f"Full name student is: {self.name} class {self.CLASS} section {self.section}"