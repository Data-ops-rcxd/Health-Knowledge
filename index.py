from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
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
    return render_template("home.html", labels=labels, values=str(values))

@app.route('/singup')
def cc():
    return render_template("singup.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login')
def ises():
    return render_template("login.html")

@app.route('/pprin')
def pprin():
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
    return render_template("pprin.html", labels=labels, values=str(values))

if __name__ == '__main__':
    app.run(debug=True, port = 4269)

## Hacer template que muestre un gráfico y el chat perron ##