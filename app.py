from flet import *

def main(page: Page):
    page.title = "Ashraf Flashlight"
    page.theme_mode = ThemeMode.LIGHT
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    # دالة التحكم (بسيطة جداً لاختبار الواجهة أولاً)
    def toggle_flash(e):
        import os
        status = "1" if e.control.text == "ON" else "0"
        try:
            # تنفيذ الأمر داخل try لضمان عدم توقف البرنامج إذا رفض الهاتف الأمر
            os.system(f"cmd notification post -S flash {status}")
            page.snack_bar = SnackBar(Text(f"تم إرسال أمر {e.control.text}"))
            page.snack_bar.open = True
        except Exception as ex:
            print(f"Error: {ex}")
        page.update()

    # إضافة العناصر مباشرة بدون حاويات معقدة
    page.add(
        AppBar(title=Text("Ashraf Flashlight"), bgcolor="red", color="white"),
        Icon(icons.FLASH_ON, size=100, color="amber"),
        Text("تطبيق الكشاف", size=25, weight="bold"),
        Divider(height=20, color="transparent"),
        Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                ElevatedButton("ON", bgcolor="green", color="white", on_click=toggle_flash),
                ElevatedButton("OFF", bgcolor="red", color="white", on_click=toggle_flash),
            ]
        ),
        Text("\nAshraf App 2026", size=12, color="grey")
    )

if __name__ == "__main__":
    run(main)
