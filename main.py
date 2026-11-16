import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#101010"

    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(on_surface="#68AB6F")
    )

    page.add(
        ft.Text("Hello, Flet!", weight=ft.FontWeight.BOLD, size=30),
        ft.Text("Este texto também fica verde."),
    )


ft.run(main)