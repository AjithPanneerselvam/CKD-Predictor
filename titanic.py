
import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json


data =  {
        "Inputs": {
                "input1":
                {
                    "ColumnNames": ["AcommadtionClass", "Sex", "Age", "SiblingSpouse", "ParentChild", "Fare", "Embarked"],
                    "Values": [ [ "1", "female", "24", "1", "0", "0", "C" ], [ "1", "male", "20", "2", "0", "0", "C" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/4ad7b48daa0f4455bd1d812507c6edfe/services/75978b2c674f42879709fbb914e75e25/execute?api-version=2.0&details=true'
api_key = 'sxl0lR4r/tsQPcIdnqdzfEEqRVEV7k+NPvlmr/JQrJNdrl2huPjbwo0wTemPkwx9IaAR1T+wJhRDjX3baaroyQ==' # Replace this with the API key for the web service
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
