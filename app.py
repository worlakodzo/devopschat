from flask import Flask, render_template, request, jsonify, session
import datetime
import json


database = []


app = Flask(__name__)
app.secret_key = "chat"

@app.route('/<room>')
def index(room):
    return render_template("index.html")


@app.route('/api/chat/<room>', methods=["POST", "GET"])
def get_and_save_message(room):

    if request.method == "POST":

        # format data submited
        data = {
            "room": room,
            "username": request.form['username'],
            "message": request.form['msg'],
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }


        database.append(data)
        session['database'] = database

        with open("database.json", "w") as json_file:
            json_file.write(json.dumps(session['database']))


    
        
        return jsonify({"success": True})

        
    elif request.method == "GET":

        #for data in database:
        # "[2018-02-25 14:00:51] omri: hi everybody!"
        data_list = []
        with open("database.json", "r") as file:
            data_list = json.loads(file.read())



        data_format = ""
        for data in data_list:
            data_format += f"{data['datetime']} {data['username']}: {data['message']}\n"


        return jsonify(data_format)
        


    
    






if __name__ == "__main__":
    app.run(debug=True)
