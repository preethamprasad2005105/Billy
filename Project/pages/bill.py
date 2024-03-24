import flet
from flet import *
from assets.elements import MyField
from pages.home import Home


class Bill(UserControl):

    def __init__(self, home : Home):
        super().__init__()
        self.page = Page
        self.home = home

        self.company = MyField(text="Company Name")
        self.item = MyField(text="Item")
        self.count = MyField(text="Number Of Items")
        self.price = MyField(text="Price")
        self.date = MyField(text="Date")
        self.total_price = MyField(text="Total Including GST")

        self.buttons = Row(controls=[
            FilledTonalButton(content=Text("SUBMIT"), on_click= self.home.new),
            FilledTonalButton("SUBMIT", on_click= lambda _: self.page.go('/home')),
        ], alignment=MainAxisAlignment.SPACE_BETWEEN)

        self.final = SafeArea(Column(
            controls=[
                Text("Billing Station", size=30),
                self.company,
                self.item,
                self.count,
                self.price,
                self.date,
                self.total_price,
                self.buttons,
            ],
            spacing= 20,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ))

   
    
    def build(self):
        return self.final