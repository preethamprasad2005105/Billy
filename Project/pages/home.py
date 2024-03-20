import flet
from flet import *


class Home(UserControl):

    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.warn = Text('To add invoice press', 
        color=colors.GREY_700)
        self.final = Row(controls=[self.warn, 
        Icon(icons.ADD_CIRCLE_ROUNDED,color=colors.GREY_700)
        ], alignment= MainAxisAlignment.CENTER)


    def build(self):
        return SafeArea(content=self.final)
        