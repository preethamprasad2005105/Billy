import flet
from flet import *

class Invoice(Card):

    def __init__(self):
        super().__init__()
        self.data = Column(controls=[
            Text("Invoice",size= 30),
            Text("Amazon PVT",size= 20),
        ])
        self.invoice = Card(content=Container(content=self.data, padding=padding.all(20),width=500))
    
    def build(self):
        return self.invoice


class Home(UserControl):

    code = True

    def __init__(self):
        super().__init__()

        self.empty = True

        self.temp_text = Text('To add a new invoice ', size = 18, color=colors.GREY_800)
        self.temp_icon = Icon(icons.ADD_BOX, color=colors.GREY_800)

        self.temp = Container(content= Row(controls=[
                self.temp_text,
                self.temp_icon
            ],height=560,alignment=MainAxisAlignment.CENTER,),
            )

        self.final = Column(controls=[
            self.temp,
            ], horizontal_alignment=CrossAxisAlignment.END)

    def new(self, e):
        self.final.controls.clear()
        self.page.go("/add")
    
    def add(self):
        self.final.controls.append(Text('hello'))


    def build(self):
    
        return SafeArea(content=self.final)


        