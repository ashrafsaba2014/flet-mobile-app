from flet import *

def main(page: Page):
    # إعدادات لضمان التشغيل الفوري
    page.theme_mode = ThemeMode.LIGHT
    
    def set_flash(status):
        import os
        try:
            os.system(f"cmd notification post -S flash {status}")
        except:
            pass
        page.snack_bar = SnackBar(Text(f"Command sent: {status}"))
        page.snack_bar.open = True
        page.update()

    # بناء الواجهة بنفس الطريقة التي نجحت في الصورة السابقة
    page.add(
        AppBar(title=Text("Ashraf Flashlight"), bgcolor="red"),
        Text("\nتطبيق الكشاف يعمل الآن", size=25, weight="bold"),
        Icon(icons.FLASHLIGHT_ON, size=100, color="orange"),
        Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                ElevatedButton("ON", on_click=lambda _: set_flash(1), bgcolor="green", color="white"),
                ElevatedButton("OFF", on_click=lambda _: set_flash(0), bgcolor="red", color="white"),
            ]
        ),
        Text("\nAshraf App 2026", size=12),
        ElevatedButton("إغلاق", on_click=lambda _: page.window_close())
    )
    page.update()

if __name__ == "__main__":
    run(main)
