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
        return format_pair_tag(tag_name='div', child=self.child, other=self.other)


class A(Tag):
    def __init__(self, href=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.href = href

    def __str__(self):
        return format_pair_tag(tag_name='a', href=self.href, other=self.other)


class Input(Tag):
    def __init__(self, _type='text', value=None, name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type = _type
        self.value = value
        self.name = name

    def __str__(self):
        return format_single_tag(tag_name='input', value=self.value, type=self._type,  name=self.name, other=self.other)


class Select(Tag):
    def __init__(self, name=None, value=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.value = value

    def __str__(self):
        return format_pair_tag(tag_name='select', child=self.child, name=self.name, value=self.value, other=self.other)


class Option(Tag):
    def __init__(self, value=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = value

    def __str__(self):
        return format_pair_tag(tag_name='option', content=self.content, value=self.value, other=self.other)


class Img(Tag):
    def __init__(self, src=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.src = src

    def __str__(self):
        return format_single_tag(tag_name='img', src=self.src, other=self.other)


class Form(Tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return format_pair_tag(tag_name='form', child=self.child, other=self.other)
