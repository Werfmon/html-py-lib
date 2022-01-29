import html_tags as html
from html_tags import render

html_fname = html.Input(placeholder='Zadej jmeno', name='jmeno')
html_lname = html.Input(placeholder='Zadej prijmeni', name='prijmeni')

html_option_muz = html.Option(value='muz', content='Muz')
html_option_zena = html.Option(value='zena', content='Zena')
html_option_jine = html.Option(value='jine', content='Jine')

html_select_pohlavi = html.Select(name='pohlavi', child=[html_option_muz, html_option_zena, html_option_jine])

form = html.Form(child=[html_fname, html_lname, html_select_pohlavi])

div = html.Div(child=form, other={'id': 'dsa'})

render(div, 'hello', title='ahoj', head_tags={'meta': [{'charset': 'UTF-8'}, {'http-equiv': 'refresh', 'content': '3'}]})