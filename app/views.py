from flask import render_template
from app import app
from forms import AddressForm, PreferencesForm
#is that right? will this even commit? does it look like I know what's going on? I don't.

@app.route('/')
def home():
  return render_template('home.html')
