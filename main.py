from fastapi.middleware.cors import CORSMiddleware
from api.requests import ExplorerRigelRequest
from jobs.background import BackgroundJob
from fastapi import FastAPI
from pprint import pprint
from Questgen import main
from utils.time import *

import time
import nltk

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

process = BackgroundJob(print_settings=True, first_run=True)


@app.get("/", summary="Rigel healthcheck endpoint")
def state_endpoint():
    if process.orion_nebula_state:
        return True

    return False


@app.post("/inference", summary="Rigel v1")
def inference_endpoint(body: ExplorerRigelRequest):
    inference_time = time.time()

    if process.rigel_state:

        qg = main.QGen()
        questions_list = []
        payload = {
            "input_text": "Hall was charged with felony reckless manslaughter. He was found not guilty of the charge at a preliminary hearing. The district court affirmed the county court's decision.",
            "max_questions": 20,
        }
        output = qg.predict_shortq(payload)
        for i in range(len(output["questions"])):
            pprint(output["questions"][i]["Question"])
            questions_list.append(output["questions"][i]["Question"])

        print_time(inference_time, "Rigel inference time")

        return questions_list

    return {"state": "offline"}
