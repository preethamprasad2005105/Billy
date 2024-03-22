import flet
from flet import *
from assets.elements import *
import json


class Login(UserControl):
    
    def __init__(self, url = '/home'):
        super().__init__()
        self.page = Page
        self.url = url


    def build(self):

        self.username =  MyField('USERNAME')
        self.key = MyPass('PASSWORD')


        self.buttons = Container(content=Row(controls=[
            FilledTonalButton('LOGIN',icon = icons.ARROW_FORWARD_IOS_ROUNDED,on_click=lambda _: self.page.go(self.url)),
            FilledTonalButton('SIGN UP', icon=icons.PERSON_ADD_ALT_ROUNDED)
            ],
            alignment=MainAxisAlignment.CENTER, 
            vertical_alignment=CrossAxisAlignment.CENTER),
            margin=20,
            scale=1.1
            )
        

        self.column = Column(controls=[
            Icon(icons.ACCOUNT_CIRCLE_ROUNDED, size = 60),
            Text('LOGIN', size=30, color=colors.PURPLE_100),
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
                ),
            )],
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            spacing= 30)