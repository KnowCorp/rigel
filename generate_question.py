"""
In this experiment we use Questgen.ai to generate faq questions
"""

from pprint import pprint
import nltk
import csv
from Questgen import main

# load the paragraphs 
paragraphs = []
with open('short_summary.csv', newline='', encoding='utf8') as csv_file:
    reader = csv.DictReader(csv_file,)
    for row in reader:
        paragraphs.append(row.get('paragraph'))


# qe= main.BoolQGen()
qg = main.QGen()

# save questions to a .csv file
data_file = open('qg_questgen_ai.csv', 'a', newline='', encoding='utf8')
csv_writer = csv.writer(data_file)
csv_writer.writerow(['paragraph', 'generated_questions'])

for index, paragraph in enumerate(paragraphs):
    
    payload = {
                "input_text": paragraph,
                "max_questions": 20
            }

    output = qg.predict_shortq(payload)
    
    if len(output) > 0:
        for i in range(len(output['questions'])):
            csv_writer.writerow([paragraph, output['questions'][i]['Question']])
            print(output['questions'][i])
    