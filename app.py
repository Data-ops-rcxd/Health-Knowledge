from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/Crearcuenta')
def cc():
    return render_template("cc.html")

@app.route('/Iniciarsesion')
def ises():
    return render_template("ises.html")

@app.route('/pprincipal')
def principal():
    return render_template("pprincipal.html")

if __name__ == '__main__':
    app.run(debug=True, port = 4269)

## Hacer template que muestre un gráfico y el chat perron ##
