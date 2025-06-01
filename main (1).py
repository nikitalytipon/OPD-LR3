from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.html')

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        str = ""
        name1 = request.form.get('name1')
        name2 = request.form.get('name2')
        name3 = request.form.get('name3')
        name4 = request.form.get('name4')
        name5 = request.form.get('name5')
        name6 = request.form.get('name6')
        str = "" + name1 + " " + name2 + " " + name3 + " " + name4 + " " + name5 + " " + name6 + '\n'
        with open('answers.txt', 'a') as file:
            file.write(str)
        return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)