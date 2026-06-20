import os
import json
from abc import ABC, abstractmethod
path = r"C:\Users\Zinte\source\repos\Course-Manager\Course-Manager\datastorage\data.json"
data = ""

contenderList = []
courseList = []

class MenuItem(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    @abstractmethod
    def execute(self) -> None:
        pass

class AddContender(MenuItem):
    @property
    def name(self):
        return "Teilnehmer Anlegen"
    def execute(self):
        print("\n--- Teilnehmer Erstellung ---")
        CreateContender()

class AddCourse(MenuItem):
    @property
    def name(self):
        return "Kurs Anleger"
    def execute(self):
        print("\n--- Kurs Erstellung ---")
        CreateContender()

class SearchContender(MenuItem):
    @property
    def name(self):
        return "Teilnehmer Suchen"
    def execute(self):
        print("\n--- Wird ausgeführt ---")

class ShowCourses(MenuItem):
    @property
    def name(self):
        return "Kurse Anzeigen"
    def execute(self):
        print("\n--- Wird ausgeführt ---")

class PerformBooking(MenuItem):
    @property
    def name(self):
        return "Anmelden"
    def execute(self):
        print("\n--- Wird ausgeführt ---")

class CancelBooking(MenuItem):
    @property
    def name(self):
        return "Kurs Stornieren"
    def execute(self):
        print("\n--- Wird ausgeführt ---")

class SaveAndQuit(MenuItem):
    @property
    def name(self):
        return "Speichern & Beenden"
    def execute(self):
        print("\n--- Wird ausgeführt ---")
        try:
            WriteData(path, "Contender")
            for contender in Contender.GetAllContender():
                print(contender.to_dict())
                WriteData(path, contender.to_dict())
            print("\n Teilnehmer wurden erfolgreich gespeichert")
        except Exception as e:
            print("\n Fehler beim Speichern der Teilnehmer")
            print(e)

        try:
            WriteData(path, "Course")
            for course in Course.GetAllCourses():
                print(course)
                WriteData(path, course)
            print("\n Kurse wurden erfolgreich gespeichert")
        except Exception as e:
            print("\n Fehler beim Speichern der Kurse")
            print(e)
        print("\n--- Programm wird beendet ---")
        os.abort()

class ConsoleMenu:
    def __init__(self):
        self._menu_items = {}

    def register_tool(self, key: str, tool: MenuItem):
        self._menu_items[key] = tool

    def display(self):
        while True:
            print("\n==== Menü ====")
            for key, tool in self._menu_items.items():
                print(f"{key}{tool.name}")
            print("verlassen [Q]")
            print("=============")
            choice = input("Wählen Sie eine Tätigkeit aus: ").upper()

            if choice == 'Q':
                print("Wird beendet...")
                break

            tool = self._menu_items.get(choice)
            if tool:
                tool.execute()
                input("Drücken Sie [Enter], um ins Menü zurückzukehren")
            else:
                print("Option war Invalide. Bitte um Wiederholung")

def DataStorageCheck(path):
    if os.path.exists(path):
        print("Eine Datenspeicherung existiert bereits")
        ReadData(path)
    else:
        print("Keine bereitstehende Speicherung von Daten gefunden")
 
def ReadData(path):
    data_store = open(path, "r")
    print("Vorhandene Daten:")
    with data_store as file:
        line = file.readline()
        print(line)
    data_store.close()

def WriteData(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

class Contender:
    contenderList = []
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
        Contender.contenderList.append(self)

    def to_dict(self):
        return {
            "name" : self.name,
            "mail" : self.mail
        }

    @classmethod
    def GetAllContender(cls):
        return cls.contenderList

    def SearchContender(self, searchParameter):
        #search Algo missing
        print("user") 
    
    def SignToCourse(self, course_id):
        if (Count(contenderList[course_id]) != courseList[course_id].capacity):
            Contender.Courses(course_id)
            print("angemeldet")
        else:
            if Course.waitlist(course_id, contender_id) < 1:
                Course[course_id].waitlist.append(contender_id)
                print("warteliste")
            else:
                print("bereits vorhanden")

class Course:
    courseList = [];
    def __init__(self, title, capacity):
        self.title = title
        self.capacity = capacity
        Course.courseList.append(self)

    def __str__(self):
        return json.dumps({
            "title" : self.title,
            "capacity" : self.capacity
        }, indent=4)
    
    @classmethod
    def GetAllCourses(cls):
       return cls.courseList

class Meta:
    def __init__(self, naechste_id_teilnehmer, naechste_id_kurs):
        self.naechste_id_teilnehmer = naechste_id_teilnehmer
        self.naechste_id_kurs = naechste_id_kurs


def CreateContender():
    name = input("Bitte Namen angeben:")
    mail = input("Bitte E-Mail angeben:")
    #Validation missing
    Contender(name, mail)
 
def CreateCourse():
    title = input("Bitte Titel angeben:")
    capacity = input("Bitte Kapazität angeben:")
    #Validation missing
    Course(title, capacity)

def StartUpSystem():
    menu = ConsoleMenu()
    menu.register_tool("1", AddContender())
    menu.register_tool("2", AddCourse())
    menu.register_tool("3", SearchContender())
    menu.register_tool("4", ShowCourses())
    menu.register_tool("5", PerformBooking())
    menu.register_tool("6", CancelBooking())
    menu.register_tool("7", SaveAndQuit())

    menu.display()

if __name__ == "__main__":
    DataStorageCheck(path)
    StartUpSystem()
