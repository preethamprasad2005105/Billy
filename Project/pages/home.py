import flet
from flet import *


class Invoice(UserControl):

    def __init__(self, company_name , description, home):
        super().__init__()

        self.home = home

        self.company_name = company_name
        self.description = description

        self.data = Row(controls=[Column(controls=[
            Text(self.company_name,size= 30),
            Text(self.description,size= 20),
        ]), FloatingActionButton(icon=icons.REMOVE, on_click=self.del_invoice)], alignment = MainAxisAlignment.SPACE_BETWEEN)

    def build(self):

        self.result = Container(
                content=self.data,
                padding=padding.all(20),
                border_radius=border_radius.all(20),
                bgcolor= "#331834",
                width=500,
                on_click=lambda _: print('hello there sweety'),
            )
        
        return self.result
    
    def del_invoice(self, e):
        if (len(self.home.final.controls) == 2):
            self.home.temp.visible = True
        self.home.final.controls.remove(self)
        self.home.final.update()

class Home(UserControl):
    

    def __init__(self):
        super().__init__()

        self.test = Invoice
        self.page = Page

        self.temp_text = Text('To add a new invoice ', size = 18, color=colors.GREY_800)
        self.temp_icon = Icon(icons.ADD_BOX, color=colors.GREY_800)

        self.temp = Container(content= Row(controls=[
                self.temp_text,
                self.temp_icon,

            ],height=560,alignment=MainAxisAlignment.CENTER,)
            )

        self.final = Column(controls=[
            self.temp
            ], horizontal_alignment=CrossAxisAlignment.END)


    def new(self, e):

        
        print('Blan function')
        
        
    def build(self):
    
        return SafeArea(content=self.final)


        
