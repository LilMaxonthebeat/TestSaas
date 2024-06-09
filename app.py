from flask import Flask, redirect, request,render_template
import time
from line_profiler import LineProfiler

app = Flask(__name__)

def profile_func(func):
    def wrapper(*args, **kwargs):
        profiler = LineProfiler()
        profiler.add_function(func)
        profiler.enable_by_count()
        result = func(*args, **kwargs)
        profiler.print_stats()
        return result
    return wrapper

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/helloo')
@profile_func
def redirect_url():
    start_time = time.process_time()  # Start CPU time measurement

    # Your redirect logic here
    long_url = 'https://www.google.com'  # Example target URL

    end_time = time.process_time()  # End CPU time measurement
    cpu_time_used = end_time - start_time
    print(f"CPU time used for redirect: {cpu_time_used} seconds")

    return redirect(long_url)

if __name__ == '__main__':
    app.run(debug=True)
