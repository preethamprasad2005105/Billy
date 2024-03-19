import flet
from flet import *
from assets.elements import MyField


class Bill(UserControl):

    def __init__(self):
        super().__init__()
        self.page = Page

        self.company = MyField(text="Company Name")
        self.gstin = MyField(text="GSTIN")
        self.item = MyField(text="Task Done/Item")
        self.count = MyField(text="Number Of Items/Taskes")
        self.price = MyField(text="Price")
        self.date = MyField(text="Date")
        self.total_price = MyField(text="Total Including GST")

        self.buttons = Row(controls=[
            FilledTonalButton(content=Text('Submit', scale=1.1), height=50, width=100),
            FilledTonalButton(content=Text('Exit', scale=1.1), height=50, width=100, on_click= lambda _: self.page.go('/')),
        ], alignment=MainAxisAlignment.SPACE_BETWEEN)

        self.final = SafeArea(Column(
            controls=[
                Text("Billing Station", size=30),
                self.company,
                self.gstin,
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