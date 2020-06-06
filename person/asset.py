""" Asset type will contain necessary asset information """


class Asset():
    def __init__(self, _name, _type, _description):
        self.name=_name
        self.type=_type
        self.description=_description


class Category1(Asset):
    """ Category 1 objects are assets which have a serial number and usually are expensive """
    def __init__(self, _name, _type, _description, _serial, _hostname=None, _url_db=None):
        Asset.__init__(_name, _type, _description)
        self.serial = _serial
        self.hostname = _hostname
        self.url_db = _url_db

class Category2(Asset):
    def __init__(self):


class Category3(Asset):
    def __init__(self):
