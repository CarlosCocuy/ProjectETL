from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.ETL_project
car_details = db.car_details
car_sales = db.car_price
manufacturer = db.manufacturer_aggregate

@app.route("/")
def index():
   return render_template("ETL template.html")

@app.route("/car_details")
def cars():
    car_data = list(car_details.find())

    return render_template("car_details.html", cardata=car_data)

@app.route("/car_sales")
def sales():
    sale_data = list(car_sales.find())

    return render_template("car_sales.html", carsales=sale_data)

@app.route("/manufacturer")
def make():
    manufacturer_data = list(manufacturer.find())    

    return render_template("manufacturer.html", manufacturer=manufacturer_data)
 
if __name__ == "__main__":
    app.run(debug=True)