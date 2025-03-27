import flet as ft


def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Minha Aplicação Fleat"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667



    # Definição de funções
    def impar_par(e):
        if int(input_numero.value) != 0:
            if int(input_numero.value) % 2 == 0:
                text_resultado.value = "Esse numero é Par"
            else:
                text_resultado.value = "Esse numero é Impar"
        else:
            text_resultado.value = "escolha outro valor"
        page.update()

    # Criação de componentes (caixa de texto, botao ...)
    input_numero = ft.TextField(
        label="Digite um numero para saber se é par ou impar",
        )
    btn_enviar = ft.FilledButton(
        text="Descobrir",
        width=page.window.width,
        on_click = impar_par
    )

    text_resultado = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_numero,
                btn_enviar,
                text_resultado,
            ]
        )
    )

ft.app(main)
