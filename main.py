from flet import * 
import flet as ft
from pages.login import Login
from pages.home import Home
from pages.front import Front
from pages.sign import Sign
from pages.bill import Bill
import json
import time
from pages.start import Start

def main(page:Page):

    page.fonts = {
        "bahnschrift": "fonts/BAHNSCHRIFT.ttf"
    }
    page.theme_mode = 'dark'
    page.vertical_alignment = MainAxisAlignment.CENTER,
    page.horizontal_alignment = CrossAxisAlignment.CENTER,
    page.theme = Theme(color_scheme_seed=colors.PURPLE, font_family='bahnschrift')

    run = True

    def route_change(route):
        page.views.clear()

        if run:
            page.views.append(
                View(
                    route='/',
                    controls=[
                        AppBar(
                        title=Text('Billy'),
                        bgcolor= '#220c24',
                        adaptive= True,
                        elevation= 3,
                        center_title = True,
                        ),
                        Start(page= Page),
                    ],
                    scroll= ScrollMode.AUTO,
                    vertical_alignment= MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,

                )
            )
        if not run:
            page.views.append(
                View(
                    route='/',
                    controls=[
                        AppBar(
                        title=Text('Billy'),
                        bgcolor= '#220c24',
                        adaptive= True,
                        elevation= 3,
                        center_title = True,

                        ),
                        Front(page= Page),
                    ],
                    scroll= ScrollMode.AUTO,
                    vertical_alignment= MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,

                )
            )
        if page.route == '/home':
            page.views.append(
                View(
                    route='/home',
                    controls=[
                        Home(page = Page)
                    ],
                    vertical_alignment= MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    appbar=AppBar(
                        title=Text('Billy'),
                        bgcolor= '#220c24',
                        adaptive= True,
                        elevation= 3,
                        center_title = True,
                        ),
                    floating_action_button= FloatingActionButton(
                        icon=icons.ADD
                    )
                )
            )



        if page.route == "/login":
            page.views.append(
                View(
                    route="/login",
                controls=[
                    AppBar(
                    title=Text('Billy'),
                    bgcolor= '#220c24',
                    adaptive= True,
                    elevation= 10
                    ),
                    SafeArea(
                        content=Login(page = Page)
                    ),
                ],
                vertical_alignment= MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == '/sign':
            page.views.append(
                View(
                    route='/sign',
                    controls=[
                        SafeArea(
                            content=Sign(page= Page)
                        )
                    ],
                    vertical_alignment= MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    appbar=AppBar(
                    title=Text('Billy'),
                    bgcolor= '#220c24',
                    adaptive= True,
                    elevation= 3,
                    center_title = True
                    
                    )
                    
                )
            )
        
        if page.route == '/add':
            page.views.append(
                View(
                    route='/add',
                    controls=[
                        AppBar(
                    title=Text('Billy'),
                    bgcolor= '#220c24',
                    adaptive= True,
                    elevation= 3),
                        Bill()
                    ],
                    vertical_alignment= MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    scroll= ScrollMode.HIDDEN,
                    padding= padding.all(20)
                    
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)



ft.app(target=main,assets_dir='assets')