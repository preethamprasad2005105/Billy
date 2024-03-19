import flet
from flet import *


class Home(UserControl):

    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.final = TextButton(text='hello', on_click= lambda _: self.page.go('/'))
    
    def build(self):
        return SafeArea(content=self.final)