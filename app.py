import os
import pandas as pd
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

####################################################################
products_prob = pd.read_csv("prob.csv")

def recommend_items(prod, n):
    basket=prod
    no_of_suggestions = n
    all_of_basket = products_prob[basket]
    all_of_basket = all_of_basket.sort_values( ascending=False)
    suggestions_to_customer = list(all_of_basket.index[:no_of_suggestions])
    #print(products_prob)
    #print(all_of_basket)
    print('You may also consider buying:', suggestions_to_customer)
    output=[]
    for i in suggestions_to_customer:
        output.append(products_prob.loc[i,'Unnamed: 0'])
    return (output)
####################################################################

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/index', methods=['GET', 'POST'])
def home():
    return render_template("./index.html",res=0)

@app.route('/index/<product>', methods=['GET', 'POST'])
def predict(product):
    l=recommend_items(product, 5)
    return render_template("./index.html", ob1=l[0], ob2=l[1], ob3=l[2],ob4=l[3],ob5=l[4],res=1)




if __name__=='__main__':
    app.run(debug=True)