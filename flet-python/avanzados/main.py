import flet as ft

#Utilitarios
#Audio - Video


def main(page: ft.Page):
    
    musica=ft.Audio(src="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=True)
    
    page.overlay.append(musica)

    video=ft.Video(playlist=[
        ft.VideoMedia(resource="https://user-images.githubusercontent.com/28951144/229373720-14d69157-1a56-4a78-a2f4-d7a134d7c3e9.mp4")
    ],
    title="Reproductor",expand=True,)
    
    page.add(
        ft.CupertinoFilledButton(text="Play", on_click=lambda _:musica.play()),
        ft.CupertinoFilledButton(text="Pausar", on_click=lambda _: musica.pause()),
        video

    )


ft.app(main)
