from html_tags.utils import nextRender


def render(struct, name='index', code_lang='html', lang='en', title='document', charset='UTF-8', head_tags=None):

    boilerplate = ''

    if code_lang == 'html':
        boilerplate += '<!DOCTYPE html>'

    # {'meta': {'charset': 'UTF-8'}}
    head = ''
    for tag, tag_list in head_tags.items():
        for attr in tag_list:
            head += f'<{tag}{nextRender(attr)}/>'

    boilerplate += f"""
        <html lang="{lang}">
        <head>
            <meta charset="{charset}">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {head}
            <title>{title}</title>
        </head>
        <body>
            {str(struct)}
        </body>
        </html>
    """
    print(boilerplate)
    file = open(f'{name}.{code_lang}', "w")
    file.write(boilerplate)
    file.close()