import flet as ft
import datetime


def main(page: ft.Page):
    
    
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
   
    
    page.add(entradaNombre,entradaNumero,entradaContraseña,entradaCorreo,entradaFecha,entrdaFechaBoton)



ft.app(main)
