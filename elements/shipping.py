""" Defines shipping type """

class Shipping():
    def __init__(self, _address: 'Address', _packages: int, _content: str, _carrier, _trackingNumber):
        self.address=_address
        self.packages=_packages
        self.content=_content
        self.carrier=_carrier
        self.trackingNumber=_trackingNumber