from flask import Flask, render_template

app = Flask(__name__)

testurl = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"

test_data = [
    ("AMAZONAS",7812),
    ("ANTIOQUIA",943469),
    ("ARAUCA",16981),
    ("ATLANTICO",140378),
    ("BARRANQUILLA",275501),
    ("BOGOTA",1853456),
    ("BOLIVAR",40064),
    ("BOYACA",129291),
    ("Caldas",119312),
    ("CAQUETA",25587),
    ("CARTAGENA",162771),
    ("CASANARE",42830),
    ("CAUCA",76146),
    ("CESAR",108824),
    ("CHOCO",18830),
    ("CORDOBA",121939),
    ("Cundinamarca",7),
    ]
labels=[row[0] for row in test_data]
values=[row[1] for row in test_data]

@app.route('/')
def home():
    return render_template("home.html", labels=labels, values=str(values))

@app.route('/singup')
def singup():
    return render_template("singup.html")

@app.route('/subs')
def subs():
    return render_template("subs.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/lobby')
def lobby():
    return render_template("lobby.html", Nickname="David")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/graphs')
def graphs():
    return render_template("graphs.html", labels=labels, values=str(values), url=testurl)

if __name__ == '__main__':
    app.run(debug=False, port = 4269)

## Hacer template que muestre un gráfico y el chat perron ##