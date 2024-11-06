from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/routes')
def routes():
    return render_template('routes.html')

@app.route('/prices')
def prices():
    return render_template('prices.html')

@app.route('/fleet')
def fleet():
    return render_template('fleet.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/parcels')
def parcels():
    return render_template('parcels.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
