from html_tags.utils import nextRender

def render(struct, name='index', code_lang='html', lang='en', title='document', charset='UTF-8', head_tags=None):

    boilerplate = ''

    if code_lang == 'html':
        boilerplate += '<!DOCTYPE html>'

    head = ''
    for tag, tag_list in head_tags.items():
        for attr in tag_list:
            head += f'<{tag}{nextRender(attr)}/>'

    boilerplate += f"""
        <html lang="{lang}">
        <head>
            <meta charset="{charset}">
            {head}
            <title>{title}</title>
        </head>
        <body>
            {str(struct)}
        </body>
        </html>
    """
    file = open(f'{name}.{code_lang}', "w")
    file.write(boilerplate)
    file.close()