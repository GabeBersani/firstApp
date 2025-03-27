import flet as ft


def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Minha Aplicação Fleat"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funções
    def mostrar(e):
        txt_resultado.value = f'{input_nome.value} {input_sobrenome.value}'
        page.update()



    # Criação de componentes (caixa de texto, botao ...)
    input_nome = ft.TextField(label="Nome",
                              hint_text="Digite seu Nome"
                              )

    input_sobrenome = ft.TextField(label="Sobrenome",
                                   hint_text="Digite seu Sobrenome"
                                   )

    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click = mostrar,
    )

    txt_resultado = ft.Text(value="")

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_nome,
                input_sobrenome,
                btn_enviar,
                txt_resultado,

            ]
        )
    )

ft.app(main)
