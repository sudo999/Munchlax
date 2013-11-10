from flask import render_template
from app import app
#from forms import AddressForm

@app.route('/')
def home():
  return render_template('home.html')

#@app.route('/order', methods = ['GET','POST'])
#def order():
#  form = AddressForm()
#  return(render_template('order.html',form=form)
