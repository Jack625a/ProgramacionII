import asyncio
import flet as ft

async def ir_a_pantalla_principal(page: ft.Page):
    await asyncio.sleep(3)  # Espera 3 segundos
    page.clean()  # Limpia la pantalla
    # Agrega contenido de la pantalla principal
    page.add(ft.Text("¡Bienvenido a la aplicación!", size=30, weight=ft.FontWeight.BOLD))

def main(page: ft.Page):
    # Configuración de la pantalla de inicio
    page.add(
        ft.Lottie(
            src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
            repeat=False,
            animate=True
        )
    )
    # Inicia la función para ir a la pantalla principal
    page.on_view_pop = lambda _: asyncio.create_task(ir_a_pantalla_principal(page))

ft.app(main)
