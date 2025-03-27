import flet as ft
from datetime import date


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    # Definição de fuções
    def exibir_idade_atual(e):
        try:
            data_inserida = input_ano.value
            data_atual = date.today()
            if len(data_inserida) == 10:
                barra = '{}{}'.format(data_inserida[2:3], data_inserida[5:6])
                if barra != '//':
                    raise ValueError
                else:
                    mes = '{}'.format(data_inserida[3:5])

                    ano = '{}'.format(data_inserida[6:])
                    dia = '{}'.format(data_inserida[:2])

                    idade = data_atual.year - int(ano)
                    if data_atual.month < int(mes):
                        idade -= 1 # idade = idade -1
                    elif data_atual.month == int(mes):
                        if data_atual.day < int(dia):
                            idade -= 1

                    txt_resultado.value = (f'{idade}\n'
                                           f'{'Maior' if idade >= 18 else "Menor"} de idade')
            else:
                raise ValueError
        except ValueError:
            txt_resultado.value = 'Erro de valor'

        page.update()



    # Criação de componentes (caixa de texto, botao ...)

    input_ano = ft.TextField(label="Data de nascimento: ",
                            hint_text="Ex.: 27/10/2007 ",
                            )
    btn_idade = ft.FilledButton(text="gerar idade",
                            width=page.window.width,
                            on_click=exibir_idade_atual,
                            )



    txt_resultado = ft.Text(value="")

    # Construir o layout

    page.add(
        ft.Column(
            [
                input_ano,
                btn_idade,
                txt_resultado,
            ]
        )
    )

ft.app(main)