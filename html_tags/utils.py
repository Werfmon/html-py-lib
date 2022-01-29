def format_pair_tag(content=None, child=None, tag_name='div', other=None, **kwargs):
    attributes = ''
    
    for name in kwargs:
        if(kwargs[name] == None): 
            continue
        attributes += f'{name}="{kwargs[name]}" '
    struct = ''
    if type(child) == list:
        for value in child:
            struct += str(value)
    else: 
        struct = child
    return f"<{tag_name} {attributes}>{struct if struct else content}</{tag_name}>"

def format_single_tag(tag_name='br',other=None, **kwargs):
    attributes = ''
    for name in kwargs:
        if(kwargs[name] == None): 
            continue
        attributes += f'{name}="{kwargs[name]}" '
    return f"<{tag_name} {attributes} />"
     