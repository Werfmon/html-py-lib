from bs4 import BeautifulSoup
from html_tags.utils import render_attr

def render(struct, name='index', code_lang='html', lang='en',
           title='document', charset='UTF-8', head_tags=None, style=None):

    boilerplate = ''

    if code_lang == 'html':
        boilerplate += '<!DOCTYPE html>'

    head = ''
    for tag, tag_list in head_tags.items():
        for attr in tag_list:
            head += f'<{tag}{render_attr(attr)}/>'

    styles = ''
    if style:
        for selector, param in style.items():
            styles += selector + '{'
            for key, value in param.items():
                styles += f'{key}:{value};'
            styles += '}'


    boilerplate += f"""
        <html lang="{lang}">
        <head>
            <meta charset="{charset}">
            {head}
            <title>{title}</title>
            <style>
            {styles}
            </style>
        </head>
        <body>
            {str(struct)}
        </body>
        </html>
    """
    with open(f'{name}.{code_lang}', 'w') as file:
        soup = BeautifulSoup(boilerplate, 'html.parser')
        file.write(soup.prettify())
