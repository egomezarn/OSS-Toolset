""" Asset type will contain necessary asset information """


class Asset():
    def __init__(self, _name, _type, _description=None):
        self.name=_name
        self.type=_type
        self.description=_description


class Category1(Asset):
    """ Category 1 objects are assets which have a serial number and usually are expensive """

    def __init__(self, _name, _description, _serial, _hostname=None, _url_db=None):
        Asset.__init__(_name, "Category 1", _description)
        self.serial = _serial
        self.hostname = _hostname
        self.url_db = _url_db


class Category2(Asset):
    """ Category 2 objects may have a serial number """

    def __init__(self, _name, _description, _serial, _url_db=None):
        Asset.__init__(_name, "Category 2", _description)
        self.serial = _serial
        self.url_db = _url_db


class Category3(Asset):
    """ Category 3 objects are just cheap accessories """
    def __init__(self, _name):
        Asset.__init__(_name, "Category 3")
