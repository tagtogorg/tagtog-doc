from flask import Flask
from flask import request
import json
import requests
import pickle
from train_model import train_model, predict_trained_model
from keras.models import load_model

# Initialize the flask app
app = Flask(__name__)

# Endpoint for the tagtog documents API
tagtog_docs_api_url = "https://localhost/-api/documents/v1"

# Name of the path where your model is saved
model_path = "model.h5"

# This is where your tagtog username and password would go
auth = requests.auth.HTTPBasicAuth(username="yourUsername", password="yourPassword")

################################################################################
#   FUNCTION NAME: tagtog_webhook
#   INPUT:
#   OUTPUT:
#       · tagtogID - Id of the document that has been changed
#   DESCRIPTION:
#       ·This is the method that will be executed when the webhook notifies
#        an action to your system, it retrains your model with the new data
#        the user has provided
################################################################################
@app.route("/tagtog_webhook", methods=['PUT', 'POST'])
def tagtog_webhook():

    # First you need to get the body of the request
    body = request.get_json()
    # Get the tagtogID -- If you have chosen ann.json in the webhook definition you don't need to do this
    tagtogID = body["tagtogID"]
    # Get the owner of the project
    owner = body["owner"]
    # Get the project name
    project_name = body["project"]
    # Set up the input parameters of your request
    params = {"owner": owner, "project": project_name, "ids": tagtogID}
    # Set up the output -- Check tagtog documentation for further info about the different possible formats
    params["output"] = "ann.json"

    # Send the get request
    annjson = (requests.get(tagtog_docs_api_url, params=params, auth=auth)).json()

    if not annjson["anncomplete"]:
        print("The annotations were changed, but they are not confirmed: {}".format(tagtogID))
        return ""

    else:
        label = parse_label(annjson)

    # Now set the output format to be a string and retrieve the text from your document
    params["output"] = "text"
    text = (requests.get(tagtog_docs_api_url, params=params, auth=auth)).text

    # load your machine learning model
    model = load_model(model_path)
    # load the tokenizer associated to the model
    with open('tokenizer.pickle', "rb") as handle:
        tokenizer = pickle.load(handle)
    # Train your model with the new data
    (model, acc) = train(text, label, model, tokenizer)
    acc = 1.0
    # Now pass the model new unseen data and let it make a prediction
    corpus = collect_unlabeled_sample()
    # Make a prediction and upload it to tagtog
    predict_and_upload(text, model, tokenizer, acc, project_name, owner)

    return tagtogID


def predict_and_upload(text, model, tokenizer, probability, project_name, owner):
    # Make the prediction and get the probability that the prediction is correct
    (label, who) = predict(text, model, tokenizer)
    # Format the prediction
    predicted_annjson = format_label_as_annjson(label, probability, who)

    # print(text, predicted_annjson)

    params = {"owner": owner, "project": project_name, "output": "html"}
    # Create the new document and get the html
    plain_html = upload_new_text(text[1], params)

    files = [("files", ('text.plain.html', plain_html)), ("files", ('text.ann.json', predicted_annjson))]
    params['format'] = 'anndoc'
    params['output'] = 'null'
    response = requests.post(tagtog_docs_api_url, params=params, auth=auth, files=files)

    print(response.text)

    return response

################################################################################
#   FUNCTION NAME: parse_label
#   INPUT:
#       · annjson - The annjson you want to get the label from
#   OUTPUT:
#       · label - The label of the annjson
#   DESCRIPTION:
#       ·This method get the label from an annjson
################################################################################
def parse_label(annjson):
    return next(iter(annjson["metas"].values()))["value"]


def format_label_as_annjson(label, probability, who):
    format = {
      "annotatable": {
        "parts": [
        ]
      },
      "anncomplete": False,
      "sources": [],
      "metas": {
        "m_1": {
          "value": label,
          "confidence": {
            "state": "pre-added",
            "who": [
              who
            ],
            "prob": probability
          }
        }
      },
      "entities": [],
      "relations": []
    }
    format_as_json = json.dumps(format, ensure_ascii=False)
    return format_as_json


def train(text, label, model, tokenizer):
    (model, acc) = train_model(text, label, model, tokenizer)
    # print("Text to train with: {}, output: {}".format(text,label))
    return(model, acc)


def collect_unlabeled_sample():
    corpus = [
        "Hi, just wanted to say that you are a worthless piece of shit",
        "Hello John! Please txt ur favorite footballer and sign up in www.vivafootball.com to get a discount in your next purchase!",
        "who are you?",
        "Hi, send a sms to the number +44 888 888 888 to get free ringtones",
        "Thanks for your subscription to Ringtone UK your mobile will be charged £5/month Please confirm by replying YES or NO. If you reply NO you will not be charged"
    ]
    return corpus


def predict(text, model, tokenizer):
    prediction = predict_trained_model(text, model, tokenizer)
    who = "ml:my_ml"
    return (prediction, who)


def upload_new_text(text, params):
    payload = {"text": text}
    response = requests.post(tagtog_docs_api_url, params=params, auth=auth, data=payload)
    # The plain.html (the request's response is in string form). You will have to parse the html's text
    plain_html = response.text
    return plain_html


if __name__ == '__main__':
    app.run(debug=True)
