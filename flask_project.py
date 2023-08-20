# import flask module
from flask import Flask,render_template,request
import pickle
# import sklearn
import pandas as pd


# instance of flask application
app = Flask(__name__)
 
# home route that returns below text when root url is accessed
@app.route("/",methods=['GET',"POST"])
def home_page():
    with open('pipe.pkl', 'rb') as f:
         model = pickle.load(f)
    with open('columns.pkl', 'rb') as f:
         column_name = pickle.load(f)
    list = ["Gender",'xmarks',"xboard","xiimarks","xiiboard","branch","grade",'domain',"workex","subject","mba"]
    query = {}
    if request.method == "POST":
       for i in range(11):
            query[column_name[i]] = [(request.form.get(list[i]))]
       query = pd.DataFrame(query)
       prob = model.predict_proba(query)
       prob = round(prob[0][1]*100,3)
       return render_template("predict.html",list = list,query = query,prob=prob,key=column_name)
    return render_template("home_page.html")
 
if __name__ == '__main__': 
   app.run(debug=True)