# apk هذا التطبيق لا تجربه عل الويندوز لانه لن يعمل ولابد من تحويله الى
# ثم نقله الى الموبايل

# 📱 تطبيق الكشاف - نسخة أندرويد جاهزة للبناء على GitHub Actions
# pip install flet flet-flashlight flet-permission-handler

# pip install flet --upgrade
# pip install flashlight                # from the terminal
# pip install flet-flashlight
# flet build apk --include-packages flet_flashlight,flet_permission_handler     # apk
# flet build apk --module-name mobile_flash_on


from flet import *                          # استيراد جميع أدوات مكتبة Flet لبناء الواجهة
try:
    from plyer import flashlight  # ✅ مكتبة قياسية للعتاد بدون واجهة
except ImportError:
    flashlight = None
# from flet_flashlight import Flashlight
# يجب تثبيت:     pip install flet-permission-handler
# from flet_permission_handler import PermissionHandler  # ✅ إزالة PermissionGroup

def main(page: Page):                       # الدالة الأساسية التي يبدأ منها التطبيق وتتحكم في الصفحة
    page.title = "Ashraf Mobile Flash"      # تحديد نص عنوان نافذة التطبيق
    page.scroll = 'auto'
    page.theme_mode = ThemeMode.LIGHT
    page.horizontal_alignment = CrossAxisAlignment.CENTER  # ✅ لضبط المحاذاة على الموبايل

    # 📱 إزالة خصائص النافذة الخاصة بالديسكتوب (تسبب مشاكل على الأندرويد)
    # page.window.height = 740              # تحديد طول نافذة التطبيق بالبكسل
    # page.window.width = 390               # تحديد عرض نافذة التطبيق (مناسب لحجم الموبايل)
    # page.window.top = 1                   # تحديد مسافة ظهور النافذة من أعلى الشاشة
    # page.window.left = 960                # تحديد مسافة ظهور النافذة من يسار الشاشة

    # بداية كود الكشاف
    # flashlight = Flashlight()       # بدون استدعاء المكتبة فى الاعلى
    # page.overlay.append(flashlight)
    # نهاية كود الكشاف

    def turn_on(e):
        if flashlight:
            try:
                flashlight.on()
            except Exception:
                pass  # يتجاهل الأخطاء الصامتة في بيئة المحاكاة
        page.update()

    def turn_off(e):
        if flashlight:
            try:
                flashlight.off()
            except Exception:
                pass
        page.update()

    # ✅ دالة آمنة للأندرويد بدل window_close()
    def show_exit_confirm(e):
        page.show_dialog(
            AlertDialog(
                title=Text("خروج"),
                content=Text("هل تريد إغلاق التطبيق؟"),
                actions=[
                    TextButton("لا", on_click=lambda _: page.pop_dialog()),
                    TextButton("نعم", on_click=lambda _: exit(0)),
                ],
            )
        )

    # settings زر الاعدادات
    # my_permission_handler = PermissionHandler()
    # page.overlay.append(my_permission_handler)
    # settings زر الاعدادات

    # def check_permissions_and_on(e):
    #     # طلب إذن الكاميرا (الفلاش جزء منها في الأندرويد)
    #     # ملاحظة: في الكود الفعلي للأندرويد يفضل استخدام await مع الدوال المتزامنة
    #     # my_permission_handler.request_permission(PermissionGroup.CAMERA)
    #     my_permission_handler.request_permission("camera")  # ✅ النص هو الطريقة المعتمدة حاليًا
    #     flashlight.turn_on()
    #     page.update()

    # def open_settings(e):
    #     my_permission_handler.open_app_settings()

    page.add(
        AppBar(
            title=Text("Flash Light"),
            color=Colors.WHITE,
            bgcolor=Colors.RED,
            actions=[  # اضافة ايقونات او ازرار لها احداث
                # IconButton(Icons.SETTINGS,on_click = open_settings),
                PopupMenuButton(
                    items=[
                        PopupMenuItem('إعدادات التطبيق'),
                        PopupMenuItem('من نحن'),
                        PopupMenuItem(),  # اضافة فاصل
                        PopupMenuItem('إغلاق التطبيق', on_click=show_exit_confirm),
                    ]
                )
            ]
        ),
        Row(
            controls=[Text('\n\nFlash Light App',size=31,color=Colors.BLACK)],
            alignment=MainAxisAlignment.CENTER  # هذا السطر يوسط العناصر داخل الصف
        ),
        Row(
            controls=[Image(src='logof.png', width=360)],        # ✅ تأكد أن logof.png داخل مجلد assets/
            alignment=MainAxisAlignment.CENTER                   # هذا السطر يوسط العناصر داخل الصف
        ),
        Row(
            controls=[
                Button(
                    'ON',
                    width=100,
                    color='white',
                    icon=Icons.PLAY_ARROW,
                    style=ButtonStyle(
                        bgcolor=Colors.GREEN,
                        color=Colors.WHITE,
                        padding=15,
                        shape=ContinuousRectangleBorder(radius=100),
                    ),
                    on_click=turn_on
                ),
                Button(
                    'OFF',
                    width=100,
                    color='white',
                    icon=Icons.PLAY_DISABLED_SHARP,
                    style=ButtonStyle(
                        bgcolor=Colors.RED,
                        color=Colors.WHITE,
                        padding=15,
                        shape=ContinuousRectangleBorder(radius=100),
                    ),
                    on_click=turn_off
                )
            ],
            alignment=MainAxisAlignment.CENTER  # هذا السطر يوسط العناصر داخل الصف
        ),
        Row(
            controls=[
                Text('\n\nAshraf Flash Light App 2026', size=14, color=Colors.BLACK),
            ],
            alignment=MainAxisAlignment.CENTER  # هذا السطر يوسط العناصر داخل الصف
        ),
    )

if __name__ == "__main__":
    # ✅ assets_dir ضروري لتحميل الصور من مجلد assets/
    run(main, assets_dir="assets")
