import flet as ft
import asyncio

async def main(page: ft.Page):
    page.title = "Ashraf Flash"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # استدعاء الإضافات
    from flet_flashlight import Flashlight
    from flet_permission_handler import PermissionHandler, Permission
    
    flash = Flashlight()
    ph = PermissionHandler()
    page.overlay.extend([flash, ph])

    async def toggle_on(e):
        # طلب الإذن والانتظار
        status = await ph.request_permission(Permission.CAMERA)
        if status == "granted":
            await flash.turn_on()
        page.update()

    async def toggle_off(e):
        await flash.turn_off()
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
    await page.update_async()

if __name__ == "__main__":
    ft.app(target=main)
