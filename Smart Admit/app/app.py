from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def smart_admit():
    model = joblib.load('model_joblib') 
    if request.method == 'POST':
        tex = request.form['rank']
        text = np.array(tex).reshape(-1, 1)
        prd=model.predict(text)
        prd = np.round(prd) 
        prde = int(prd)
        colleges = {
            1: "National Institute of Technology, Tiruchirapalli",
            2: "National Institute of Technology Karnataka, Surathkal",
            3: "National Institute of Technology, Rourkela",
            4: "National Institute of Technology, Warangal",
            5: "National Institute of Technology, Calicut",
            6: "Visvesvaraya National Institute of Technology, Nagpur",
            7: "National Institute of Technology, Durgapur",
            8: "National Institute of Technology, Silchar",
            9: "Malaviya National Institute of Technology, Jaipur",
            10: "Motilal Nehru National Institute of Technology, Allahabad",
            11: "National Institute of Technology, Kurukshetra",
            12: "Dr B R Ambedkar National Institute of Technology, Jalandhar",
            13: "S V National Institute of Technology, Surat",
            14: "National Institute of Technology Meghalaya",
            15: "National Institute of Technology, Patna",
            16: "National Institute of Technology, Raipur",
            17: "National Institute of Technology, Srinagar",
            18: "Maulana Azad National Institute of Technology, Bhopal",
            19: "National Institute of Technology, Agartala",
            20: "National Institute of Technology Goa",
            21: "National Institute of Technology, Jamshedpur",
            22: "National Institute of Technology Manipur",
            23: "National Institute of Technology, Hamirpur",
            24: "National Institute of Technology Uttarakhand",
            25: "National Institute of Technology Puducherry",
            26: "National Institute of Technology Arunachal Pradesh",
            27: "National Institute of Technology Sikkim",
            28: "National Institute of Technology Delhi"
        }
        if prde in colleges.keys():
            result = dict(list(colleges.items())[prde-1:])
            return render_template('index.html', output=result)
        else:
            return render_template("index.html", output="Invalid input")
    else:
        return render_template("index.html")

