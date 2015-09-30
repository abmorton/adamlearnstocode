from flask import Flask, render_template, request
# from yahoo_finance import Share
from app import app
# from .forms import StockSearchForm
# from .models import Stock


# This is now done in the __init__.py file
# app = Flask(__name__)    
# app.config.from_object('config')

# I'm not sure if I should be doing this in the handler functions below, seems dirty.
# user = {'nickname': 'Adam'}

# portfolio = [{'symb':'AAPL',
# 			'shares': 10},
# 			{'symb':'GOOG',
# 			'shares': 10}]
 
@app.route('/')
def home():
  return render_template('index.html')

# @app.route('/stock/<symbol>')
# def stock(symbol):

# 	stock = Share(symbol)
# 	return render_template('stock.html', stock=stock, symbol=symbol)


# @app.route('/stocks', methods=['GET', 'POST'])
# def stocks():

# # Trying to implement the StockSearchForm on the stocks.html template.
# # Need to change the methods to include 'POST'.

# 	form = StockSearchForm()

# 	if request.method == 'POST':
# 		stock = Share(form.stocklookup.data)
# 		return render_template('stocks.html', form=form, stock=stock)

# 	elif request.method == 'GET':
# 		stock = Share('aapl')
# 		return render_template('stocks.html', form=form, stock=stock)

# @app.route('/user')
# def user():
# 	user = {'nickname': 'Adam'}
#   	return render_template('user.html', user=user)


# Perhaps write a program or create a file (csv) which contains 
# a large list of stocks, then write a funciton to look them up 
# in this way later.

# ^ Actually, why don't we try to use SQLAlchemy like a big boy!?


# Going to take care of this in the run.py file now.
# if __name__ == '__main__':
#   app.run(debug=True)

