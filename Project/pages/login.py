import flet
from flet import *
from assets.elements import *
from data.data_handler import *
import json
from time import *


class Login(UserControl):

    
    def __init__(self):
        super().__init__()
        self.page = Page


    def login_check(self, e):
        self.success = login_up_process(self.username.value,self.key.value)
        try:
            if not self.success:
                self.error.visible = True
                self.error.update()
            else:
                self.page.go('/home')
        except AssertionError:
            print('fuck off')
    
    def login_check_off(self, e):
        try:
            self.error.visible = False
            self.error.update()
        except AssertionError:
            pass
        

    def build(self):

        self.username =  TextField(label='USERNAME',hint_text='USERNAME', border_color=colors.PURPLE_100, on_focus= self.login_check_off)
        self.key = TextField(label='PASSWORD',hint_text='PASSWORD', border_color=colors.PURPLE_100, password= True, can_reveal_password= True, on_focus=self.login_check_off)
        self.error = Text('Username or Password is incorrect', color= colors.RED, visible= False)


        self.buttons = Container(content=Column(controls=[
            FilledTonalButton(' LOGIN',icon = icons.ARROW_FORWARD_IOS_ROUNDED,on_click= self.login_check),
            FilledTonalButton('SIGN UP', icon=icons.PERSON_ADD_ALT_ROUNDED,on_click=lambda _: self.page.go("/sign"))
            ],
            alignment=MainAxisAlignment.END, 
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing= 20),
            height= 150,
            scale=1.2
            )
        

        self.column = Column(controls=[
            Icon(icons.PERSON, size = 60),
            Text('LOGIN', size=30, color=colors.PURPLE_100),
            Row(controls=[self.error]),
            self.username,
            self.key,
            self.buttons


        ],alignment=MainAxisAlignment.CENTER,
        horizontal_alignment= CrossAxisAlignment.CENTER,
        spacing=20)

        return Column(controls=[Card(
            content=Container(
                content=self.column,
                margin= margin.symmetric(20,20),
                height=600
                ),
            )],
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            spacing= 30)