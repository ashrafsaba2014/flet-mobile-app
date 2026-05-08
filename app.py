from flet import *
from flet_flashlight import Flashlight
from flet_permission_handler import PermissionHandler, Permission

def main(page: Page):
    page.title = "Ashraf Mobile Flash"
    page.theme_mode = ThemeMode.LIGHT
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    # ✅ تعريف الكشاف ومدير الصلاحيات في الـ overlay
    flashlight = Flashlight()
    ph = PermissionHandler()
    page.overlay.extend([flashlight, ph])

    def turn_on(e):
        # ✅ طلب الإذن أولاً قبل التشغيل
        status = ph.request_permission(Permission.CAMERA)
        flashlight.turn_on()
        page.snack_bar = SnackBar(content=Text("🔦 تم تشغيل الكشاف"))
        page.snack_bar.open = True
        page.update()

    def turn_off(e):
        flashlight.turn_off()
        page.snack_bar = SnackBar(content=Text("🔦 تم إيقاف الكشاف"))
        page.snack_bar.open = True
        page.update()

    def show_exit_confirm(e):
        # ✅ تصحيح إغلاق التطبيق في الأندرويد
        def close_app(e):
            page.window_close() # الطريقة الصحيحة لـ Flet

        page.dialog = AlertDialog(
            title=Text("خروج"),
            content=Text("هل تريد إغلاق التطبيق؟"),
            actions=[
                TextButton("لا", on_click=lambda _: page.close_dialog()),
                TextButton("نعم", on_click=close_app),
            ],
        )
        page.dialog.open = True
        page.update()

    # --- واجهة المستخدم (نفس تصميمك مع تعديل بسيط للأزرار) ---
    page.add(
        AppBar(
            title=Text("Flash Light"),
            bgcolor=colors.RED,
            color=colors.WHITE,
            actions=[
                PopupMenuButton(
                    items=[
                        PopupMenuItem(text="إغلاق التطبيق", on_click=show_exit_confirm),
                    ]
                )
            ]
        ),
        Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text("\nFlash Light App", size=31, weight="bold"),
                Image(src="logof.png", width=360),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ElevatedButton("ON", bgcolor=colors.GREEN, color=colors.WHITE, on_click=turn_on, width=120),
                        ElevatedButton("OFF", bgcolor=colors.RED, color=colors.WHITE, on_click=turn_off, width=120),
                    ]
                ),
                Text("\nAshraf Flash Light App 2026", size=14)
            ]
        )
    )

if __name__ == "__main__":
    run(main, assets_dir="assets")
