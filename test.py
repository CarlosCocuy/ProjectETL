from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.ETL_project
car_details = db.car_details


@app.route("/")
def index():
    car_data = list(car_details.find())

    return render_template("cardetails.html", cardata=car_data)


if __name__ == "__main__":
    app.run(debug=True)
