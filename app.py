from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	favfood = ["Burger", "Pizza", "Salad", "Sushi"]
	opposite_day = True
    # return "Sushi"
	return render_template("index.html", favfood=favfood, opposite_day=opposite_day)

if __name__ == '__main__':
	app.run(debug = True)