from flask import Flask, render_template, request
import json
import urllib2

app = Flask(__name__)


def azureMl(formList):
    data =  {

    "Inputs": {

            "input1":
            {
                "ColumnNames": ["age", "bloodpressure", "specificgravity", "albumin", "sugar", "puscell", "puscellclumps", "bacteria", "bloodglucoserandom", "bloodurea", "serumcreatinine", "sodium", "potassium", "hemoglobin", "packedcellvolume", "whitebloodcellcount", "redbloodcellcount", "hypertension", "diabetesmellitus", "coronaryarterydisease", "appetite", "pedalenema", "anemia"],
                "Values": [ formList ]
            },        },
        "GlobalParameters": {}
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/4ad7b48daa0f4455bd1d812507c6edfe/services/7d25282d3b2a4326881597f8f1287b1a/execute?api-version=2.0&details=true'
    api_key = 'Paste your API key here'
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers)

    try:
        response = urllib2.urlopen(req)
        result = response.read()
        print("result is" + result)
        result = json.loads(result)
        result = result["Results"]["output1"]["value"]["Values"][0][23]
        return result

    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(json.loads(error.read()))


@app.route('/')
def home_page():
   return render_template('home.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      formList = []
      formList.append(str(request.form['age']))
      formList.append(str(request.form['BloodPressure']))
      formList.append(str(1.02))
      formList.append(str(request.form['albumin']))
      formList.append(str(request.form['sugar']))
      formList.append(str("normal"))
      formList.append(str("notpresent"))
      formList.append(str("notpresent"))
      formList.append(str(request.form['bloodGlucose']))
      formList.append(str(request.form['bloodUrea']))
      formList.append(str(5.23))
      formList.append(str(130))
      formList.append(str(6.5))
      formList.append(str(request.form['haemoglobin']))
      formList.append(str(request.form['packed']))
      formList.append(str(request.form['white']))
      formList.append(str(request.form['red']))
      formList.append(str(request.form['hypertension']))
      formList.append(str("no"))
      formList.append(str("no"))
      formList.append(str(request.form['appetite']))
      formList.append(str("no"))
      formList.append(str(request.form['anaemia']))

      result = azureMl(formList)

      if result == "ckd":
          result = "Chronic Kidney Disease."
      else:
          result = "Not a Chronic Kidney Disease."

      return render_template("result.html",result = result)


if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)
