import flet
from flet import *
from data.data_handler import sign_up_process


class Sign(UserControl):
    
    def __init__(self, page : Page):
        super().__init__()
        self.page = page

        self.checked = bool()
    

    def build(self):

        self.username =  TextField(label='USERNAME',hint_text='USERNAME', border_color=colors.PURPLE_100)
        self.key =TextField(label='PASSWORD',hint_text='PASSWORD', border_color=colors.PURPLE_100, password= True, can_reveal_password= True)
        self.email = TextField(label='EMAIL',hint_text='EMAIL', border_color=colors.PURPLE_100)
        self.key_confirm = TextField(
            label='CONFIRM PASSWORD',
            hint_text='CONFIRM PASSWORD' ,
            border_color=colors.PURPLE_100, 
            password= True, 
            can_reveal_password= True ,
             on_change=lambda _:self.pasw_check())


        self.buttons = Container(content=Column(controls=[

            FilledTonalButton("SIGN UP", icon=icons.ARROW_FORWARD_IOS_ROUNDED, on_click = self.checked_go,),
            FilledTonalButton(" LOGIN ", icon=icons.PERSON, on_click = lambda _: self.page.go('/login'))
            ],
            alignment=MainAxisAlignment.CENTER, 
            horizontal_alignment=CrossAxisAlignment.CENTER),
            scale=1.1
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
            height=650),],
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            spacing= 30)
    
    def pasw_check(self):
        if(self.key.value != self.key_confirm.value):
            self.key_confirm.error_text = 'Password doesnt match'
            self.checked = False
        else:
            self.key_confirm.error_text = ''
            self.checked = True

        self.key_confirm.update()
    
    def checked_go(self, e):
        if self.checked == True:
            if sign_up_process(username=self.username.value, password=self.key.value):
                self.page.go('/home')