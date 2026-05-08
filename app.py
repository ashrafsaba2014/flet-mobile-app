from flet import *
import os

def main(page: Page):
    # إعدادات الصفحة الأساسية لضمان ظهور العناصر
    page.title = "Ashraf Flash"
    page.theme_mode = ThemeMode.LIGHT
    page.padding = 20
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    def set_flashlight(status):
        # محاولة تشغيل الكشاف عبر أوامر النظام
        try:
            os.system(f"cmd notification post -S flash {status}")
        except:
            pass

    # واجهة بسيطة ومباشرة لضمان عدم حدوث خطأ في الرسم
    page.add(
        Text("Ashraf Flashlight", size=30, weight="bold", color="red"),
        Divider(height=20, color="transparent"),
        # تأكد من وجود الصورة أو سيظهر مكان فارغ (يفضل وضع الصورة في حاوية)
        Container(
            content=Image(src="logof.png", width=250, error_content=Icon(icons.FLASH_ON, size=100)),
            alignment=alignment.center,
        ),
        Divider(height=20, color="transparent"),
        Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                ElevatedButton(
                    "ON", 
                    bgcolor="green", 
                    color="white", 
                    width=120, 
                    on_click=lambda _: set_flashlight(1)
                ),
                ElevatedButton(
                    "OFF", 
                    bgcolor="red", 
                    color="white", 
                    width=120, 
                    on_click=lambda _: set_flashlight(0)
                ),
            ]
        ),
        Text("\nAshraf App 2026", size=12, color="grey")
    )
    page.update()

if __name__ == "__main__":
    run(main, assets_dir="assets")
