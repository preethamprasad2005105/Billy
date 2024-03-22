import flet
from flet import *

class Invoice(UserControl):

    def __init__(self):
        super().__init__()
        self.data = Row(controls=[Column(controls=[
            Text("Invoice",size= 30),
            Text("Amazon PVT",size= 20),
        ]), FloatingActionButton(icon=icons.REMOVE, on_click=self.end)], alignment = MainAxisAlignment.SPACE_BETWEEN)
        self.invoice = Card(content=Container(content=self.data, padding=padding.all(20),width=500))

    def end(self, e):
        print(e.value)

    def build(self):
        return self.invoice


class Home(UserControl):

    def __init__(self):
        super().__init__()

        self.page = Page

        self.temp_text = Text('To add a new invoice ', size = 18, color=colors.GREY_800)
        self.temp_icon = Icon(icons.ADD_BOX, color=colors.GREY_800)

        self.temp = Container(content= Row(controls=[
                self.temp_text,
                self.temp_icon
            ],height=560,alignment=MainAxisAlignment.CENTER,)
            )

        self.final = Column(controls=[
            self.temp
            ], horizontal_alignment=CrossAxisAlignment.END)


    def new(self, e):
        self.page.go('/add')
        self.temp.visible = False
        self.final.controls.append(Invoice())
        self.update()




    def build(self):
    
        return SafeArea(content=self.final)


        