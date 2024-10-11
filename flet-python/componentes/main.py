import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Row(
            [
            ft.Container(content=
            
            ft.Text(value="Texto en el contenedor", size=25),bgcolor=ft.colors.GREEN_700,padding=30,width=500,alignment=ft.alignment.center,height=100,border_radius=ft.border_radius.all(50),
            ),
            ft.Container(content=ft.TextField(label="Ingrese una url",keyboard_type=ft.KeyboardType.URL)
                         )
            ],alignment=ft.MainAxisAlignment.CENTER,scroll=ft.ScrollMode.AUTO
        ),
       
        ft.Text(value="Prueba Flet - BOTONES",size=30,color=ft.colors.ERROR,font_family='Roboto',weight=ft.FontWeight.BOLD),
        ft.CupertinoButton(text='Cupertino Boton',icon=ft.icons.DEVELOPER_MODE_ROUNDED,bgcolor=ft.colors.PINK_900,color=ft.colors.LIME_800,icon_color=ft.colors.LIME_800),
        ft.CupertinoFilledButton(text='Cupertino Filled Boton',icon=ft.icons.ADD_A_PHOTO),
        ft.FilledButton(text='Boton Filled',icon=ft.icons.TAG_FACES_ROUNDED,icon_color=ft.colors.AMBER_900,on_click=click),
        ft.FloatingActionButton(icon=ft.icons.LOCAL_GROCERY_STORE_SHARP,bgcolor=ft.colors.LIME_ACCENT_200),
        ft.IconButton(icon=ft.icons.PETS,icon_color=ft.colors.PINK_800),
        ft.OutlinedButton(text='Boton OutLined'),
        ft.Text(value="Prueba Flet - ENTRADAS DE TEXTO",size=30,color=ft.colors.ERROR,font_family='Roboto',weight=ft.FontWeight.BOLD),
        ft.TextField(label="Ingrese su nombre"),
        ft.TextField(label="Ingrese su contraseña",password=True),
        ft.TextField(label="Ingrese su celular",keyboard_type=ft.KeyboardType.PHONE),
        ft.TextField(label="Ingrese su Correo", keyboard_type=ft.KeyboardType.EMAIL),
        ft.TextField(label="Ingrese una url",keyboard_type=ft.KeyboardType.URL)

    )
def click():
    print('Se hizo click en el boton')

ft.app(main)
