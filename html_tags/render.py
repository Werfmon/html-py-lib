def render(struct, name='index', lang='html'):
    file = open(f'{name}.{lang}', "w")
    file.write(str(struct))
    file.close()