import flet as ft

def main(page: ft.Page):
    page.title = "Ashraf Flash"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # محاولة استيراد الإضافة داخلياً
    try:
        from flet_flashlight import Flashlight
        flash = Flashlight()
        page.overlay.append(flash)
        has_flash = True
    except:
        has_flash = False

    def toggle_on(e):
        if has_flash:
            flash.turn_on()
            page.snack_bar = ft.SnackBar(ft.Text("🔦 ON"))
            page.snack_bar.open = True
            page.update()

    def toggle_off(e):
        if has_flash:
            flash.turn_off()
            page.update()

    page.add(
        ft.Icon(ft.icons.FLASHLIGHT_ON, size=80, color=ft.colors.AMBER),
        ft.Text("Ashraf Flashlight", size=25, weight="bold"),
        ft.Row(
            [
                ft.ElevatedButton("ON", on_click=toggle_on, bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
                ft.ElevatedButton("OFF", on_click=toggle_off, bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
