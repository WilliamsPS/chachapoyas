from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('consulta_instituciones_salud.html')

if __name__ == '__main__':
    app.run(debug=True)