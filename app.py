from flask import Flask, render_template, request
import json
import urllib2

app = Flask(__name__)

def azureMl(formList):
        data =  {
                "Inputs": {
                        "input1":
                        {
                            "ColumnNames": ["AcommadtionClass", "Sex", "Age", "SiblingSpouse", "ParentChild", "Fare", "Embarked"],
                            "Values": [ formList ]
                        },
                            },
                    "GlobalParameters": {}
                }
        body = str.encode(json.dumps(data))
        url = 'https://ussouthcentral.services.azureml.net/workspaces/4ad7b48daa0f4455bd1d812507c6edfe/services/75978b2c674f42879709fbb914e75e25/execute?api-version=2.0&details=true'
        api_key = 'sxl0lR4r/tsQPcIdnqdzfEEqRVEV7k+NPvlmr/JQrJNdrl2huPjbwo0wTemPkwx9IaAR1T+wJhRDjX3baaroyQ=='
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
        req = urllib2.Request(url, body, headers)

        try:
            response = urllib2.urlopen(req)

            # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
            # req = urllib.request.Request(url, body, headers)
            # response = urllib.request.urlopen(req)

            result = response.read()
            print(result)
        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))

@app.route('/')
def home_page():
   return render_template('home.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      formList = []
      temp = request.form['accomadation']
    #   formList.

      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)
