from flask import Flask, render_template,jsonify,request

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('home.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method=='POST':
        make = request.form.get("Make")
        Model = request.form.get("Model")
        year = request.form.get("year")
        fuel_type = request.form.get("fuel_type")
        engine_cylinder = request.form.get("engine_cylinder")
        driven_wheels = request.form.get("driven_wheels")
        engine_hp = request.form.get("engine_hp")
        transmission_type = request.form.get("transmission_type")
        num_doors = request.form.get("num_doors")
        market_category = request.form.get("market_category")
        vehicle_size = request.form.get("vehicle_size")
        vehicle_style = request.form.get("vehicle_style")
        highway_mpg = request.form.get("highway_mpg")
        city_mpg = request.form.get("city_mpg")
        popularity = request.form.get("popularity")
        print(make,Model,year,fuel_type,engine_cylinder,driven_wheels,engine_hp,transmission_type,num_doors,
              market_category,vehicle_size,vehicle_style,highway_mpg,city_mpg,popularity)
        return jsonify({"status":"data fetched successfully"})
    
    else:
        return render_template("predict.html")


if __name__=='__main__':
    app.run(host= '0.0.0.0')


