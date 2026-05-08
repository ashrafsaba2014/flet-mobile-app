from flet import *
import os

def main(page: Page):
    page.title = "Ashraf Flashlight"
    page.theme_mode = ThemeMode.LIGHT
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = "auto"

    # دالة التحكم في الكشاف (الطريقة المضمونة برمجياً)
    def set_flashlight(status):
        try:
            # محاولة تشغيل الكشاف عبر أوامر النظام
            os.system(f"cmd notification post -S flash {status}")
            # رسالة تأكيد للمستخدم
            page.snack_bar = SnackBar(Text("🔦 تم إرسال الأمر بنجاح"))
            page.snack_bar.open = True
            page.update()
        except:
            pass

    page.add(
        AppBar(title=Text("Ashraf Flashlight"), bgcolor="red", color="white"),
        Text("\nFlashlight App", size=30, weight="bold"),
        
        # إضافة الصورة داخل حاوية مع معالجة الخطأ
        Container(
            content=Image(
                src="logof.png", 
                width=250,
                # إذا لم يجد الصورة، سيظهر أيقونة بدلاً من الشاشة البيضاء
                error_content=Icon(icons.FLASH_ON, size=100, color="orange")
            ),
            padding=20
        ),
        
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
        
        Divider(height=50, color="transparent"),
        Text("Ashraf App 2026", size=12, color="grey"),
        ElevatedButton("إغلاق التطبيق", on_click=lambda _: page.window_close())
    )

if __name__ == "__main__":
    run(main, assets_dir="assets")
