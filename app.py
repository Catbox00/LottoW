from flask import Flask, render_template
import random

app = Flask(__name__)

# Function to generate random lotto numbers
def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

@app.route('/')
def home():
    lotto_numbers = generate_lotto_numbers()
    return render_template('index.html', lotto_numbers=lotto_numbers)

if __name__ == '__main__':
    app.run(debug=True)