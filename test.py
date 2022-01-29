import html_tags as html
from html_tags import render

html_fname = html.Input(other={'placeholder': 'Zadej jmeno'}, name='jmeno')
html_lname = html.Input(other={'placeholder': 'Zadej prijmeni'}, name='prijmeni')

html_option_muz = html.Option(value='muz', content='Muz')
html_option_zena = html.Option(value='zena', content='Zena')
html_option_jine = html.Option(value='jine', content='Jine')

html_select_pohlavi = html.Select(
    name='pohlavi',
    child=[html_option_muz, html_option_zena, html_option_jine])

html_submit = html.Input(_type='submit', value='Register')

form = html.Form(
    child=[html_fname, html_lname, html_select_pohlavi],
    other={'style': 'display: flex; flex-direction: column'})

div = html.Div(
    child=[form, html_submit],
    other={'id': 'container'}
    )

render(div, 'hello',
       title='Part I',
       head_tags={'meta': [
           {'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'},
           {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}
       ]},
       style={'#container': {'width': '10rem'}})
