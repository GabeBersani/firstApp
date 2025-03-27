import flet as ft



def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    # Definição de fuções
    def exibir_soma(e):
        soma = int(input_num1.value) + int(input_num2.value)
        txt_resultado.value = soma
        page.update()
    def exibir_sub(e):
        subtracao = int(input_num1.value) - int(input_num2.value)
        txt_resultado.value = subtracao
        page.update()
    def exibir_multi(e):
        multiplicacao = int(input_num1.value) * int(input_num2.value)
        txt_resultado.value = multiplicacao
        page.update()
    def exibir_div(e):
        divsao = int(input_num1.value) / int(input_num2.value)
        txt_resultado.value = divsao
        page.update()


    # Criação de componentes (caixa de texto, botao ...)
    input_num1 = ft.TextField(label="Número: ",
                            hint_text="Digite seu primeiro número",
                            )
    input_num2 = ft.TextField(label="Número: ",
                            hint_text="Digite seu segundo número",)


    btn_somar = ft.FilledButton(text="Somar",
                            width=page.window.width,
                            on_click=exibir_soma,
                            )

    btn_subtracao = ft.FilledButton(text="Subtrair",
                            width=page.window.width,
                            on_click=exibir_sub,)

    btn_multiplicacao = ft.FilledButton(text="Multiplicar",
                            width=page.window.width,
                            on_click=exibir_multi,)

    btn_divisao = ft.FilledButton(text="Dividir",
                            width=page.window.width,
                            on_click=exibir_div,)


    txt_resultado = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_num1,
                input_num2,
                btn_somar,
                btn_subtracao,
                btn_multiplicacao,
                btn_divisao,
                txt_resultado,
            ]
        )
    )

ft.app(main)
