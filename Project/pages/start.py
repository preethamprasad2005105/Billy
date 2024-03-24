import flet
from flet import *


class Start(UserControl):

    def __init__(self, page : Page):

        super().__init__(
        )
        self.page = page
    
    def ses_check(self, e):
        if True:
            self.page.go('/front')
        else:
            self.page.go('/home')


    def build(self):
        return  SafeArea(
                        content= Card(content=Column(
                            controls=[
                                Icon(icons.PAYMENT, scale = 2 ),
                                Container(content=Text('Billy', scale= 2), padding= padding.symmetric(5)),
                                FilledTonalButton(" Continue ", icon=icons.ARROW_CIRCLE_RIGHT_OUTLINED,on_click= self.ses_check),
                                Container(content=Text("App by Preetham Prasad", color= colors.GREY_600,),padding=padding.only(top=20, right=20, left=20))
                                ],
                            spacing = 20,
                            scale= 1.1,
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment= CrossAxisAlignment.CENTER
                            
                        ),height = 650,
                          width=350,
                          color="colors.GREY_600")
                    )
