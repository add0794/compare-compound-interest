from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Example data
    data = [10, 20, 30, 40, 50]
    labels = ['A', 'B', 'C', 'D', 'E']

    return render_template('index.html', data=data, labels=labels)

if __name__ == '__main__':
    app.run(debug=True)