from flet import *
import sys

def main(page: Page):
    # إعدادات الصفحة
    page.theme_mode = ThemeMode.LIGHT
    page.scroll = "always"
    
    # دالة لعرض الأخطاء على الشاشة مباشرة
    def show_error(error_msg):
        page.add(
            Container(
                content=Column([
                    Text("⚠️ تم اكتشاف خطأ في التشغيل:", color="red", weight="bold"),
                    Text(str(error_msg), color="black", selectable=True),
                ]),
                padding=20,
                bgcolor="yellow"
            )
        )
        page.update()

    try:
        # بناء الواجهة
        page.add(
            AppBar(title=Text("Ashraf Flashlight Test"), bgcolor="red"),
            Text("\nإذا رأيت هذا النص، فالواجهة تعمل!", size=20),
            ElevatedButton("تجربة إغلاق التطبيق", on_click=lambda _: page.window_close()),
            Divider(),
            Text("معلومات النظام:", weight="bold"),
            Text(f"Platform: {page.platform}"),
        )
        
        # محاولة تنفيذ أمر الكشاف داخل try مستقلة
        try:
            import os
            # سنكتفي بطباعة رسالة هنا للتأكد من قدرة بايثون على الوصول لـ os
            page.add(Text("✅ مكتبة OS جاهزة"))
        except Exception as e:
            page.add(Text(f"❌ خطأ في مكتبة OS: {e}"))
            
    except Exception as global_error:
        # إذا فشل كل شيء، اعرض الخطأ فوراً
        show_error(global_error)
    
    page.update()

if __name__ == "__main__":
    run(main)
