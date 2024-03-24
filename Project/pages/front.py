import flet
from flet import *


class Front(UserControl):

    def __init__(self):

        super().__init__(
        )
        self.page = Page

        self.size = 30

        self.welcome = Container(content=Text('Welcome to Billy', size=self.size), padding= padding.symmetric(5))
        self.title1 = Container(content=Text('Automatic Bill', size=self.size), padding= padding.symmetric(5))
        self.title2 = Container(content=Text('Generator', size=self.size), padding= padding.symmetric(5))
        self.login_button = FilledTonalButton(" Login ", icon=icons.PERSON_ADD,on_click= lambda _: self.page.go("/login"))
        self.sign_button = FilledTonalButton("Sign Up", icon=icons.ADD, on_click= lambda _: self.page.go("/sign"))


    def build(self):
        return  SafeArea(
                        content= Card(content=Column(
                            controls=[
                                Container(Column(controls = [Icon(icons.PAYMENT, size= self.size*1.2),
                                self.welcome,
                                self.title1,
                                self.title2,
                                Container(Column(controls=[self.login_button,
                                self.sign_button], horizontal_alignment=CrossAxisAlignment.CENTER, spacing=20), padding=padding.only(top=35), scale=1.1)], alignment=MainAxisAlignment.CENTER, horizontal_alignment= CrossAxisAlignment.CENTER),height= 450),
                                Container(content=Text("App by Preetham Prasad", color= colors.GREY_600,),padding=padding.only(top=20, right=20, left=20))
                                ],
                            spacing = 20,
                            scale= 1.1,
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment= CrossAxisAlignment.CENTER),
                            height = 650,
                            width=360,
                            color="colors.GREY_600")
                    )