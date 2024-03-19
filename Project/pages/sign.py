import flet
from flet import *


class Sign(UserControl):
    
    def __init__(self, page : Page):
        super().__init__()
        self.page = page
    
    def pasw_check(self,e):
        if self.key.value != self.key_confirm.value:
            self.key_confirm.error_text = 'Password does not match'
        else:
            self.key_confirm.error_text = ''


    def build(self):

        self.username =  TextField(label='USERNAME',hint_text='USERNAME', border_color=colors.PURPLE_100)
        self.key =TextField(label='PASSWORD',hint_text='PASSWORD', border_color=colors.PURPLE_100)
        self.email = TextField(label='EMAIL',hint_text='EMAIL', border_color=colors.PURPLE_100)
        self.key_confirm = TextField(label='CONFIRM PASSWORD',hint_text='CONFIRM PASSWORD', border_color=colors.PURPLE_100, on_change=self.pasw_check)


        self.buttons = Container(content=Row(controls=[
            FilledTonalButton('LOGIN',icons.ARROW_FORWARD_IOS_ROUNDED, on_click = self.pasw_check),
            FilledTonalButton('SIGN UP', icon =icons.PERSON_ADD_ALT_ROUNDED, on_click = self.pasw_check)
            ],
            alignment=MainAxisAlignment.CENTER, 
            vertical_alignment=CrossAxisAlignment.CENTER),
            margin=20
            )
        

        self.column = Column(controls=[
            Icon(icons.PERSON_ADD_ROUNDED, size = 60),
            Text('SIGN UP', size=30, color=colors.PURPLE_100),
            self.username,
            self.email,
            self.key,
            self.key_confirm,
            self.buttons

        ],alignment=MainAxisAlignment.CENTER,
        horizontal_alignment= CrossAxisAlignment.CENTER,
        spacing=20)

        return Column(controls=[Card(
            content=Container(
                content=self.column,
                margin= margin.symmetric(20,20),
                ),
            ),],
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            spacing= 30)