import flet as ft
import datetime


def main(page: ft.Page):

    def notificacion(evento):
        page.update()
    
    
    entradaNombre=ft.TextField(label="Ingrese su nombre: ",icon=ft.icons.PERSON_3)
    entradaNumero=ft.TextField(label="Ingrese su celular: ",keyboard_type=ft.KeyboardType.PHONE, icon=ft.icons.PHONE_ANDROID)
    entradaContraseña=ft.TextField(label="Ingrese su contraseña: ",password=True,can_reveal_password=True, icon=ft.icons.PASSWORD)
    entradaCorreo=ft.TextField(label="Ingrese su Correo: ",keyboard_type=ft.KeyboardType.EMAIL,icon=ft.icons.EMAIL_ROUNDED)
    entradaFecha=ft.TextField(label="Ingrese su fecha de nacimiento: ",icon=ft.icons.DATE_RANGE_ROUNDED, keyboard_type=ft.KeyboardType.DATETIME)
    def cambios(evento):
        page.add(ft.Text(f"Fecha Seleccionada: {evento.value.strftime('%Y-%m-%d')}"))

    entrdaFechaBoton=ft.ElevatedButton(text="Seleccionar Fecha",on_click=lambda e: page.add(
        ft.DatePicker(first_date=datetime.datetime(year=2024,month=10,day=17),on_change=cambios())
    ))
    #Casillas de verificacion
    opcion1=ft.CupertinoCheckbox (label="Opcion 1",active_color=ft.colors.ORANGE_ACCENT_200)
    opcion2=ft.Checkbox(label="Opcion 2")
    opcion3=ft.Checkbox(label="Opcion 3")
    opcion4=ft.Checkbox(label="Opcion 4")
   #Radio Botones
    opciones=ft.RadioGroup(content=ft.Column([
        ft.Radio(label="Opcion 1",value="Opcion1",fill_color=ft.colors.RED_200),
        ft.Radio(label="Opcion 2",value="Opcion2"),
        ft.Radio(label="Opcion 3",value="Opcion3"),
        ft.Radio(label="Opcion 4",value="Opcion 3")]))

    #Chips
    chip=ft.Chip(label=ft.Text("Seleccionar",color=ft.colors.RED),bgcolor=ft.colors.RED,autofocus=True,color=ft.colors.CYAN,check_color=ft.colors.CYAN,selected=True)
    #Sliders
    volumen=ft.Slider(min=0,max=100,divisions=10,label="{value}%",mouse_cursor=ft.MouseCursor.VERTICAL_TEXT)
    volumen2=ft.CupertinoSlider(min=0,max=100,divisions=10)



    page.add(entradaNombre,entradaNumero,entradaContraseña,entradaCorreo,entradaFecha,entrdaFechaBoton,opcion1,opcion2,opcion3,opcion4,opciones,chip,volumen,volumen2)




ft.app(main)
