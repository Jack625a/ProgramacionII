import flet as ft


def main(page: ft.Page):
    page.title="Navegacion"
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

    boton=ft.CupertinoFilledButton(text="Boton")
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
        ft.Row(
            [
                navegacionLateral,
                ft.VerticalDivider(width=1),
                ft.Column([
                    ft.Text(value="Pantalla Inicio"),
                ],alignment=ft.MainAxisAlignment.START,
                expand=True),
            ],
            expand=True,
        )
    )


ft.app(main,assets_dir="assets")
