from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class AddressForm(Form):
    address = TextField('address', validators = [Required()])
    city = TextField('city', validators = [Required()])
    zip = TextField('zip', validators = [Required()])
