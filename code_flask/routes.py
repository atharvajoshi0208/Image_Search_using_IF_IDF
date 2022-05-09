from flask import  render_template,request,Flask,url_for
# from httpx import 
from code_flask import app
from code_flask.forms import SerachForm
#from flask_wtf.csrf import CSRFProtect, CSRFError
from code_flask.Main_Code import main_Function
from collections import Counter, defaultdict, OrderedDict
import os

def get_ImageList(query):
    return main_Function(query)

def get_ImageList1(ImageList1):
    ImageList3=  defaultdict(dict)
    value = ''
    for index in ImageList1:
        value = ImageList1[index]
        # ImageList3[value] =  "code_flask\Images\\book"+ str(index-1) +".jpg"
        # ImageList3[value] =  r"F:\CA6005\Assignment_2\New folder\code_flask\Images\\book" + str(index-1) +".jpg"
        img_path = os.path.join(os.getcwd(), 'code_flask', 'static', 'Images', f'book{str(index-1)}.jpg')
        ImageList3[value] = url_for('static', filename=f'Images/book{str(index-1)}.jpg')

    return ImageList3

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def homepage():
    form=SerachForm()
    ImageList=  defaultdict(dict)
    ImageList2=  defaultdict(dict)

    if request.method == 'POST':
        query = request.form['SearchQuery']
        print(query)
        ImageList = get_ImageList(query)
        ImageList2 = get_ImageList1(ImageList)
        return render_template('HomePage.html',form=form,ImageList=ImageList,ImageList2=ImageList2)
    else:
        print(os.getcwd())
        return render_template('HomePage.html',form=form,ImageList=ImageList,ImageList2=ImageList2)