""" Defines address type """

class Address():
    def __init__(self, _zip_code, _full_address, _contact_phone, _isPGN: bool):
        self.zip_code=_zip_code
        self.full_address=_full_address
        self.contact_phone=_contact_phone
        self.isPGN=_isPGN