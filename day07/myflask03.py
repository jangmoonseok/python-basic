from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    c = [
        {'e_id':1, 'e_name':'1', 'sex':'1', 'addr':'1'},
        {'e_id':2, 'e_name':'2', 'sex':'2', 'addr':'2'},
        {'e_id':3, 'e_name':'3', 'sex':'3', 'addr':'3'},
    ]
    return render_template('forward.html',c = c)

if __name__ == '__main__':
    app.run(debug=True)