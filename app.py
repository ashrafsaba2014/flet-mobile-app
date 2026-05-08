import flet as ft

def main(page: ft.Page):
    # إعدادات الصفحة الأساسية
    page.title = "Ashraf Flash"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # دالة التحكم (بسيطة ومباشرة)
    def toggle_flash(e):
        import os
        status = "1" if e.control.text == "ON" else "0"
        try:
            os.system(f"cmd notification post -S flash {status}")
        except:
            pass

    # إضافة العناصر بطريقة "البناء المباشر"
    page.add(
        ft.Icon(ft.icons.FLASHLIGHT_ON, size=80, color=ft.colors.AMBER),
        ft.Text("Ashraf Flashlight", size=25, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        ft.Row(
            [
                ft.ElevatedButton("ON", on_click=toggle_flash, bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
                ft.ElevatedButton("OFF", on_click=toggle_flash, bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Text("\nAshraf App 2026", size=10)
    )

if __name__ == "__main__":
    ft.app(target=main)
