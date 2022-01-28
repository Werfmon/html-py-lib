class Tag: 
    _child: object
    _class: str
    _id: str
    _style: str
class Actions: 
    _onSubmit: str
    _onClick: str
    _onChange: str

class A(Tag, Actions):
    _href: str
    _title: str
    _target: str
    _require: bool

    def __init__(self, _href, _title, _target):
        self._href = _href
        self._title = _title
        self._target = _target

    
class Input(Tag, Actions):
    _type: str
    _value: str


class Select(Tag, Actions):
    _multiple: bool

class Option(Tag):
    _content: str
    _value: str 
class Img(Tag, Actions): 
    _src: str
    _alt: str
    _title: str

class Div(Tag):
    pass

class Form(Tag, Actions):
    _action: str
    _method: str