from flet import *

def main(page: Page):
    page.title = "Ashraf Flashlight"
    page.theme_mode = ThemeMode.LIGHT
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    
    # استيراد الإضافات داخل دالة main لضمان عدم انهيار التطبيق عند الفتح
    try:
        from flet_flashlight import Flashlight
        from flet_permission_handler import PermissionHandler, Permission
        
        flash = Flashlight()
        ph = PermissionHandler()
        page.overlay.extend([flash, ph])
        HAS_EXT = True
    except:
        HAS_EXT = False

    def turn_on(e):
        if HAS_EXT:
            ph.request_permission(Permission.CAMERA)
            flash.turn_on()
            page.snack_bar = SnackBar(Text("🔦 ON"))
            page.snack_bar.open = True
        else:
            page.snack_bar = SnackBar(Text("⚠️ الإضافة غير مدمجة بشكل صحيح"))
            page.snack_bar.open = True
        page.update()

    def turn_off(e):
        if HAS_EXT:
            flash.turn_off()
        page.update()

    page.add(
        AppBar(title=Text("Flash Light"), bgcolor=colors.RED, color=colors.WHITE),
        Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text("\nFlash Light App", size=30, weight="bold"),
                Image(src="logof.png", width=300),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("ON", on_click=turn_on, bgcolor=colors.GREEN, color=colors.WHITE),
                        ElevatedButton("OFF", on_click=turn_off, bgcolor=colors.RED, color=colors.WHITE),
                    ]
                )
            ]
        )
    )

if __name__ == "__main__":
    run(main, assets_dir="assets")
