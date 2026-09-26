import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.title = "App"

    texto_mensagem = ft.Text(value="", size=22, weight=ft.FontWeight.BOLD)

    def ao_clicar_no_botao(e):
        texto_mensagem.value = "Olá, Mundo!"
        page.update()

    botao_arredondado = ft.FilledButton("Clique Aqui", on_click=ao_clicar_no_botao)

    page.add(
        botao_arredondado,
        ft.Container(height=30),
        texto_mensagem
    )

ft.run(main)
