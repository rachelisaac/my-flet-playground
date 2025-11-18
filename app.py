import flet as ft

def main(page: ft.Page):
    count = 0

    def button_clicked(e):
        nonlocal count
        count += 1
        txt.value = f"Clicked {count} times"
        page.update()

    txt = ft.Text("Press the button")
    btn = ft.ElevatedButton("Click me", on_click=button_clicked)
    

    page.add(txt, btn)

ft.app(target=main, view=ft.WEB_BROWSER, port=8500)
