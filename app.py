from flask import Flask, render_template

app = Flask(__name__)

TEAMS_2026 = [
    {
        "name": "McLaren",
        "engine": "Mercedes",
        "color": "#FF8000",
        "drivers": [
            {"name": "Lando Norris", "number": 4, "country": "GB"},
            {"name": "Oscar Piastri", "number": 81, "country": "AU"},
        ],
    },
    {
        "name": "Ferrari",
        "engine": "Ferrari",
        "color": "#E8002D",
        "drivers": [
            {"name": "Charles Leclerc", "number": 16, "country": "MC"},
            {"name": "Lewis Hamilton", "number": 44, "country": "GB"},
        ],
    },
    {
        "name": "Red Bull Racing",
        "engine": "Red Bull Powertrains",
        "color": "#3671C6",
        "drivers": [
            {"name": "Max Verstappen", "number": 1, "country": "NL"},
            {"name": "Isack Hadjar", "number": 6, "country": "FR"},
        ],
    },
    {
        "name": "Mercedes",
        "engine": "Mercedes",
        "color": "#27F4D2",
        "drivers": [
            {"name": "George Russell", "number": 63, "country": "GB"},
            {"name": "Andrea Kimi Antonelli", "number": 12, "country": "IT"},
        ],
    },
    {
        "name": "Aston Martin",
        "engine": "Honda",
        "color": "#229971",
        "drivers": [
            {"name": "Fernando Alonso", "number": 14, "country": "ES"},
            {"name": "Lance Stroll", "number": 18, "country": "CA"},
        ],
    },
    {
        "name": "Alpine",
        "engine": "Mercedes",
        "color": "#0093CC",
        "drivers": [
            {"name": "Pierre Gasly", "number": 10, "country": "FR"},
            {"name": "Franco Colapinto", "number": 43, "country": "AR"},
        ],
    },
    {
        "name": "Haas",
        "engine": "Ferrari",
        "color": "#B6BABD",
        "drivers": [
            {"name": "Esteban Ocon", "number": 31, "country": "FR"},
            {"name": "Oliver Bearman", "number": 87, "country": "GB"},
        ],
    },
    {
        "name": "Racing Bulls",
        "engine": "Red Bull Powertrains",
        "color": "#6692FF",
        "drivers": [
            {"name": "Liam Lawson", "number": 30, "country": "NZ"},
            {"name": "Arvid Lindblad", "number": 27, "country": "GB"},
        ],
    },
    {
        "name": "Williams",
        "engine": "Mercedes",
        "color": "#64C4FF",
        "drivers": [
            {"name": "Alex Albon", "number": 23, "country": "TH"},
            {"name": "Carlos Sainz", "number": 55, "country": "ES"},
        ],
    },
    {
        "name": "Audi",
        "engine": "Audi",
        "color": "#C0C0C0",
        "drivers": [
            {"name": "Nico Hülkenberg", "number": 27, "country": "DE"},
            {"name": "Gabriel Bortoleto", "number": 5, "country": "BR"},
        ],
    },
    {
        "name": "Cadillac",
        "engine": "Ferrari",
        "color": "#FFD700",
        "drivers": [
            {"name": "Valtteri Bottas", "number": 77, "country": "FI"},
            {"name": "Sergio Pérez", "number": 11, "country": "MX"},
        ],
    },
]


@app.route("/")
def home():
    return render_template("index.html", teams=TEAMS_2026)


@app.route("/grid")
def grid():
    return render_template("grid.html", teams=TEAMS_2026)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
