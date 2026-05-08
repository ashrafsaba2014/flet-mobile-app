from flet import *
import os

def main(page: Page):
    page.title = "Ashraf Flash"
    page.theme_mode = ThemeMode.LIGHT
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    # دالة التحكم في الكشاف عبر النظام
    def set_flashlight(status):
        try:
            os.system(f"cmd notification post -S flash {status}")
        except:
            pass

    # بناء الواجهة داخل متغير لضمان جاهزيتها قبل الإضافة
    content = Column(
        horizontal_alignment=CrossAxisAlignment.CENTER,
        controls=[
            Text("Ashraf Flashlight", size=30, weight="bold", color=colors.RED),
            Image(src="logof.png", width=250),
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    ElevatedButton("ON", bgcolor=colors.GREEN, color=colors.WHITE, on_click=lambda _: set_flashlight(1)),
                    ElevatedButton("OFF", bgcolor=colors.RED, color=colors.WHITE, on_click=lambda _: set_flashlight(0)),
                ]
            ),
            Text("\nAshraf App 2026", size=12)
        ]
    )

    # تنظيف الصفحة وإضافة المحتوى فوراً
    page.clean()
    page.add(content)
    page.update()

if __name__ == "__main__":
    run(main, assets_dir="assets")
