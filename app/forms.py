from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class AddressForm(Form):
    Address = TextField('address', validators = [Required()])
    City = TextField('city', validators = [Required()])
    Zip = TextField('zip', validators = [Required()])

class PreferencesForm(Form):
    NumberParty = TextField('numbParty', validators = [Required()])
    MaxMoney = BooleanField('maxMoney', default = false)
    Allergies = TextField('allegies', validators = [Required()])
