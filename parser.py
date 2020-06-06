# -*- coding: utf-8 -*-
""" Generates custom email based on templates """

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, PackageLoader, select_autoescape
from email_generator.person.support import Support
from email_generator.person.user import User
import pyperclip

#name = input()
def notes(_template, _asset=None, _amount=1,  _shipping=None, _trackingNo=None):
    env = Environment(
        loader=PackageLoader('email_generator', 'templates/notes'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template(_template)

    return template.render(accessory="Headset", sent=_shipping, destination="Okayama" )

def email(_template, _user: 'User'=None, _support: 'Support'=None, _asset=None, _shipping=None):
    env = Environment(
        loader=PackageLoader('email_generator', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template(_template)

    # Select support name to use on the introduction of the email.
    if _support.useFirst:
        supportName=_support.first
    else:
        supportName=_support.last

    return template.render(user_name=_user.last, support_name=supportName,
                          zip_code="158-0082", full_address=_user.address, contact_phone=_user.phone,
                          support_signature=_support.signature)

def main():
    aUser = User("Emanuel", "Gomez Arn",
                 "080-8870-1550", "東京都世田谷区等々力６−５−４わびさびハウスSE-4", "Shinagawa")
    aSupport = Support("Jorge", "Clooney", "j.clooney@philips.com", "Jorge Clooney (OSS)", True)
    email('address_confirmation.html', aUser, aSupport)
    print(repr(__name__))

if __name__ == "__main__":
    main()
