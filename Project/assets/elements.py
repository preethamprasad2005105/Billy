from flet import *
import flet

class MyField(TextField):
    
    def __init__(self, text, on_click = None):
        
        super().__init__(
            border_color= colors.DEEP_PURPLE_100,
            focused_border_color= colors.PURPLE_100
        )

        self.on_click = on_click
        
        self.hint_text = text
        self.label = text


        self.final = TextField(
            hint_text= self.hint_text,
            border_color = self.border_color,
            label = self.label,
            on_focus= self.on_click
        )
    
    def build (self):
        return self.final

class MyPass(TextField):
    
    def __init__(self, text, on_click = None):
        
        super().__init__(
            password= True,
            border_color = colors.DEEP_PURPLE_100,
            can_reveal_password= True
            
        )

        self.on_click = on_click
        
        self.hint_text = text
        self.label = text

        self.final = TextField(
            hint_text= self.hint_text,
            label = self.label,
            on_focus= self.on_click
        )
    
    def build (self):
        return self.final
