#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)


# In[4]:


@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model = joblib.load("regression")
        pred = model.predict([[rates]])
        print(pred)
        return(render_template("index.html", result=pred))
    else:
        return(render_template("index.html", result="WAITING"))


# In[ ]:


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("80"))


# In[ ]:




