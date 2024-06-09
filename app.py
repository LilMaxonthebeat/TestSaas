from flask import Flask, redirect, request,render_template
import time
from line_profiler import LineProfiler

app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/helloo')
def redirect_url():
    long_url = 'https://www.google.com'
    return redirect(long_url)

if __name__ == '__main__':
    app.run(debug=True)
