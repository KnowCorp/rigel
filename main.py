from fastapi.middleware.cors import CORSMiddleware
from api.requests import ExplorerRigelRequest
from jobs.background import BackgroundJob
from utils.print import console_print
from fastapi import FastAPI
from utils.time import *

import time

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

rigel = process.rigel


@app.get("/", summary="Rigel healthcheck endpoint")
def state_endpoint():
    if process.rigel_state:
        return True

    return False


@app.post("/inference", summary="Rigel v1")
def inference_endpoint(body: ExplorerRigelRequest):
    """
    > The function takes in a payload from the client, passes it to the question generation model, and
    returns the questions generated by the model

    :param body: ExplorerRigelRequest
    :return: A list of Context, Questions, and Answers
    """

    inference_time = time.time()

    console_print(debug=f"Rigel v1 payload\n{body}")

    questions_list = []

    if process.rigel_state:

        # payload = {
        #     "input_text": "Hall was charged with felony reckless manslaughter. He was found not guilty of the charge at a preliminary hearing. The district court affirmed the county court's decision.",
        #     "max_questions": 20,
        # }

        if body.max_questions <= 0:
            body.max_questions = 1

        payload = {
            "input_text": f"{body.input_text}",
            "max_questions": body.max_questions,
        }

        output = rigel.predict_shortq(payload)

        if output == {}:
            return questions_list.append("Error [7071] - Empty Body")

        for i in range(len(output["questions"])):
            question = output["questions"][i]["Question"]
            answer = output["questions"][i]["Answer"]
            context = output["questions"][i]["context"]

            console_print(debug=f"Context:{context}\nQ:{question}\nA:{answer}")

            questions_list.append((context, question, answer))

        print_time(inference_time, "rigel inference time")

        return questions_list

    return questions_list.append("Error [7070] - No Response")
