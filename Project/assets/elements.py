from flet import *
import flet

class MyField(TextField):
    
    def __init__(self, text):
        
        super().__init__(
            border_color = "#31133b",
            focused_border_color= colors.PURPLE_100
        )
        
        self.hint_text = text
        self.label = text


        self.final = TextField(
            hint_text= self.hint_text,
            border_color = self.border_color,
            label = self.label,
        )
    
    def build (self):
        return self.final

class MyPass(TextField):
    
    def __init__(self, text):
        
        super().__init__(
            border_color = colors.PURPLE_100,
            password= True,
            can_reveal_password= True
            
        )
        
        self.hint_text = text
        self.label = text

        self.final = TextField(
            hint_text= self.hint_text,
            border_color = self.border_color,
            label = self.label,
        )
    
    def build (self):
        return self.final