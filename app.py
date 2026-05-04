import flet as ft
def main(page: ft.Page):
    page.title = "تجربة أندرويد"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.Text("Ashraf Helmy", size=30, color="blue", weight=ft.FontWeight.BOLD))

if __name__ == "__main__":
    ft.run(main)