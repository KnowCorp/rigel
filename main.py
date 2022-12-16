from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from pprint import pprint
import nltk
from Questgen import main

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", summary="Orion's Nebula Test Connection endpoint")
def state_endpoint():
    qg = main.QGen()
    questions_list = []
    payload = {
                "input_text": "Hall was charged with felony reckless manslaughter. He was found not guilty of the charge at a preliminary hearing. The district court affirmed the county court's decision.",
                "max_questions": 20
            }
    output = qg.predict_shortq(payload)
    for i in range(len(output['questions'])):
        pprint(output['questions'][i]['Question'])
        questions_list.append(output['questions'][i]['Question'])

    return questions_list
