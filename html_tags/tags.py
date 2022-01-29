from .utils import format_pair_tag, format_single_tag

class Tag:
    def __init__(self, content=None, other=None, child=None):
        self.content = content
        self.child = child
        self.other = other

class Div(Tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return format_pair_tag(child=self.child, tag_name='div', other=self.other)


class A(Tag):
    def __init__(self, href=None, target='_self', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.href = href
        self.target = target

    def __str__(self):
        return format_pair_tag(tag_name='a', other=self.other, href=self.href, target=self.target)


class Input(Tag):
    def __init__(self, _type='text', value=None, name=None, placeholder=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type = _type
        self.value = value
        self.name = name
        self.placeholder = placeholder

    def __str__(self):
        return format_single_tag(tag_name='input', other=self.other, value=self.value, type=self._type, placeholder=self.placeholder, name=self.name)


class Select(Tag):
    def __init__(self, multiple=False, name=None, value=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.multiple = multiple
        self.name = name
        self.value = value

    def __str__(self):
        return format_pair_tag(child=self.child, tag_name='select', other=self.other, name=self.name, value=self.value)


class Option(Tag):
    def __init__(self, value='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = value

    def __str__(self):
        return format_pair_tag(tag_name='option', other=self.other, content=self.content, value=self.value)


class Img(Tag):
    def __init__(self, src=None, alt=None, title=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.src = src
        self.alt = alt
        self.title = title

    def __str__(self):
        return format_single_tag(tag_name='input', other=self.other, src=self.src, alt=self._alt, title=self._title)


class Form(Tag):
    def __init__(self, action='/', method='GET', *args, **kwargs):
        self.action = action
        self.method = method
        super().__init__(*args, **kwargs)

    def __str__(self):
        return format_pair_tag(child=self.child, tag_name='form', other=self.other, action=self.action, method=self.method)