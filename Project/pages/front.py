import flet
from flet import *


class Front(UserControl):

    def __init__(self, page : Page):

        super().__init__(
        )
        self.page = page


    def build(self):
        return  SafeArea(
                        content= Card(content=Column(
                            controls=[
                                Icon(icons.PAYMENT, scale = 2 ),
                                Container(content=Text('Welcome to Billy', scale= 2), padding= padding.symmetric(5)),
                                Container(content=Text('Automatic Bill Generator', scale= 1.8), padding= padding.symmetric(5)),
                                FilledTonalButton(" Login ", icon=icons.PERSON_ADD,on_click= lambda _: self.page.go("/login")),
                                FilledTonalButton("Sign Up", icon=icons.ADD, on_click= lambda _: self.page.go("/sign")),
                                Container(content=Text("App by Preetham Prasad", color= colors.GREY_600,),padding=padding.only(top=20, right=20, left=20))
                                ],
                            spacing = 20,
                            scale= 1.1,
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment= CrossAxisAlignment.CENTER
                            
                        ),height = 620,
                          width=360,
                          color="colors.GREY_600")
                    )