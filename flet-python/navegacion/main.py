import flet as ft


def main(page: ft.Page):
    
    page.title="Navegacion"
    #page.scroll=True
    page.appbar=ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.MENU,color="white"),
        middle=ft.Text(value="AppBar - Navegacion",color="white"),
        bgcolor=ft.colors.TEAL_800,
        trailing=ft.Icon(ft.icons.SHOPPING_CART, color="white")
    )
    page.navigation_bar=ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(label="Inicio", icon=ft.icons.HOME, selected_icon=ft.icons.HOME_FILLED,bgcolor="red"),
            ft.NavigationDestination(label="Productos", icon=ft.icons.STORE),
            ft.NavigationDestination(label="Carrito",icon=ft.icons.SHOPPING_CART_CHECKOUT),
            ft.NavigationDestination(label="Perfil", icon=ft.icons.PERSON)
        ]
        
    )
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    deslizador=ft.NavigationDrawer(
        controls=[
            ft.Container(height=15),
            ft.NavigationDrawerDestination(
                label="Opcion 1",
                icon=ft.icons.PETS
            ),
            ft.NavigationDrawerDestination(
                label="Opcion 2",
                icon=ft.icons.COLOR_LENS
            ),
            ft.NavigationDrawerDestination(
                label="Opcion 3",
                icon=ft.icons.RESTORE_FROM_TRASH
            ),
            ft.NavigationDrawerDestination(
                label="Opcion 4",
                icon=ft.icons.FACE_SHARP
            )
        ],
    )

    
    navegacionLateral=ft.NavigationRail(
        leading=ft.Image(src="f/imagenes/logo.png",width=100,height=100),
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.HOME,label="Inicio",padding=10),
            ft.NavigationRailDestination(icon=ft.icons.FACEBOOK,label="Facebook",padding=10),
            ft.NavigationRailDestination(icon=ft.icons.SHOPPING_CART_CHECKOUT_OUTLINED,label="Carrito",padding=10),
            ft.NavigationRailDestination(icon=ft.icons.TIKTOK, label="TikTok",padding=10)
        ]
        
        
        )
    

    
    page.add(
        #ft.CupertinoFilledButton(text="Boton",on_click=lambda e:page.show_drawer_async(drawer=deslizador)),
        ft.Row(
            [
                
                navegacionLateral,
                ft.VerticalDivider(width=1),
                ft.Column([
                    ft.Text(value="Pantalla Inicio"),
                    ft.Lottie(src="https://lottie.host/36e15193-f40e-4c5f-ab73-d217405a49f6/HPJY6kG8E6.json",width=200),
                    ft.Lottie(src="https://lottie.host/d379657e-17ba-411c-a0d4-7343e8a236bb/WttSjAgvuB.json",width=200)
                ],alignment=ft.MainAxisAlignment.START,
                expand=True),

            ],
            expand=True,
        )
    )


ft.app(main,assets_dir="assets")
