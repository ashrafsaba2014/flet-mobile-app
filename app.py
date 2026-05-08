import flet as ft

def main(page: ft.Page):
    page.title = "Ashraf Flash"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Safe import for the native extensions
    try:
        from flet_flashlight import Flashlight
        from flet_permission_handler import PermissionHandler, Permission
        
        flash = Flashlight()
        ph = PermissionHandler()
        page.overlay.extend([flash, ph])
        has_ext = True
    except:
        has_ext = False

    def toggle_on(e):
        if has_ext:
            # Explicitly request permission before turning on
            status = ph.request_permission(Permission.CAMERA)
            flash.turn_on()
            page.snack_bar = ft.SnackBar(ft.Text("🔦 Flashlight ON"))
            page.snack_bar.open = True
        else:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Extension Missing"))
            page.snack_bar.open = True
        page.update()

    def toggle_off(e):
        if has_ext:
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
