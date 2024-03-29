from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
import json
from dialog import Dialog
from kivymd.uix.menu import MDDropdownMenu

class Notes(Screen):
    note1 = ObjectProperty()
    note2 = ObjectProperty()
    note3 = ObjectProperty()
    zag1 = StringProperty()
    text1 = StringProperty()
    zag2 = StringProperty()
    text2 = StringProperty()
    zag3 = StringProperty()
    text3 = StringProperty()
    data = None

    def __init__(self, **kwargs):
        super(Notes, self).__init__(**kwargs)

        self.menu1 = MDDropdownMenu(
            caller=self.note1,
            items=[
                 {'viewclass':'MDItemMenu',
                  'text':'y',
                  'callback':self.call()}],
            width_mult=4,
        )

        self.menu2 = MDDropdownMenu(
            caller=self.note2,
            items=[
                {'viewclass':'MDItemMenu',
                'text':'y',
                'callback':self.call()}],
            width_mult=4,
        )

        self.menu3 = MDDropdownMenu(
            caller=self.note3,
            items=[
                {'viewclass':'MDItemMenu',
                'text':'y',
                'callback':self.call()}],
            width_mult=4,
        )

    def entering(self):
        with open('notes.json') as file:
            data = json.load(file)

        if data[0]["zag"] == None and data[0]["text"] == None:
            self.note1.opacity = 0
        else:
            self.note1.opacity = 1
            self.zag1 = data[0]["zag"]
            self.text1 = data[0]["text"]
        
        if data[1]["zag"] == None and data[1]["text"] == None:
            self.note2.opacity = 0
        else:
            self.note2.opacity = 1
            self.zag2 = data[1]["zag"]
            self.text2 = data[1]["text"]

        if data[2]["zag"] == None and data[2]["text"] == None:
            self.note3.opacity = 0
        else:
            self.note3.opacity = 1
            self.zag3 = data[2]["zag"]
            self.text3 = data[2]["text"]

    def add_note(self):
        flag = False
        data = None
        with open('notes.json') as file:
            data = json.load(file)
        
        if data[0]["zag"] == None and data[0]["text"] == None:
            flag = True
        elif data[1]["zag"] == None and data[1]["text"] == None:
            flag = True
        elif data[2]["zag"] == None and data[2]["text"] == None:
            flag = True
        if flag:
            self.parent.current = 'AddNote'
        else:
            Dialog('К сожалению доступно только 3 заметки', 'Внимание!')

    def open_menu1(self):
        print('open1')
        self.menu1.open()

    def open_menu2(self):
        self.menu2.open()

    def open_menu3(self):
        self.menu3.open()

    def call(self):
        print('call')
