from flet import *
import os

def main(page: Page):
    page.title = "Ashraf Flashlight"
    page.theme_mode = ThemeMode.LIGHT
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER

    def set_flashlight(status):
        # status: 1 للتشغيل، 0 للإطفاء
        try:
            # محاولة تشغيل الكشاف عبر أوامر النظام في أندرويد
            os.system(f"cmd notification post -S flash {status}")
            # طريقة ثانية لضمان العمل على إصدارات مختلفة
            os.system(f"service call flashlight {status+1}") 
        except:
            pass

    def turn_on(e):
        set_flashlight(1)
        page.snack_bar = SnackBar(Text("🔦 تم إرسال أمر التشغيل"))
        page.snack_bar.open = True
        page.update()

    def turn_off(e):
        set_flashlight(0)
        page.snack_bar = SnackBar(Text("🔦 تم إرسال أمر الإيقاف"))
        page.snack_bar.open = True
        page.update()

    page.add(
        AppBar(title=Text("Ashraf Flashlight"), bgcolor=colors.RED, color=colors.WHITE),
        Text("Flashlight App", size=30, weight="bold"),
        Image(src="logof.png", width=300),
        Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                ElevatedButton("ON", on_click=turn_on, bgcolor=colors.GREEN, color=colors.WHITE, width=120),
                ElevatedButton("OFF", on_click=turn_off, bgcolor=colors.RED, color=colors.WHITE, width=120),
            ]
        ),
        Text("\nAshraf Flash Light App 2026", size=14)
    )

if __name__ == "__main__":
    run(main, assets_dir="assets")
