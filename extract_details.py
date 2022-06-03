from medcat.cat import CAT
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector
from collections import defaultdict
import re
import json

@Language.factory("language_detector")
def get_lang_detector(nlp, name):
   return LanguageDetector()

# Download the model_pack from the models section in the github repo.
DATA_DIR = "C:/Users/HP/nlptools/data/"
model_pack_path = DATA_DIR + "medmen_wstatus_2021_oct.zip"
cat = CAT.load_model_pack(model_pack_path)
print("--------------------------------------")

keys = []
values = []
with open('C:/Users/HP/nlptools/files/input.txt', 'r') as file:
    text = file.read().replace('\n', '')
type_ids_filter = ['T033']
cui_filters = set()
for type_ids in type_ids_filter:
  cui_filters.update(cat.cdb.addl_info['type_id2cuis'][type_ids])
cat.cdb.config.linking['filters']['cuis'] = cui_filters
doc=cat(text)
idx=0
for ent in doc.ents:
    if str(ent)!="detection":
        keys.append('Covid-Result')
        values.append(str(ent))
    print(ent)
doc2 = cat(text)

print("--------------------------------------")

nlp = spacy.load('en_core_web_md')

text1= nlp(text)
for w in text1.ents:
    if w.label_=='DATE':
        keys.append('DATE')
        values.append(w.text)
        print(w.text)
        break
print("--------------------------------------")
text2 = nlp(text)
for w in text2.ents:
  if w.label_=='PERSON':
    keys.append('PERSON')
    values.append(w.text)
    print(w.text)
    break
print("--------------------------------------")


def patientID(text):
  ID_REG = re.compile(r'[a-zA-Z0-9\.\-+_]{14}')
  IDs = re.findall(ID_REG,text)
  patientID = ",".join(IDs)
  patientID = patientID.split(',')
  patientID = patientID[0]

  return patientID
patientID=patientID(text)
list_words= text.split()
index =list_words.index("ID")
pre_IDs=list_words[index-3:index+3]
for i in pre_IDs:
  if i==patientID:
    ID=i
keys.append('PATIENT ID')
values.append(ID)
print(ID)
print("--------------------------------------")
dictionary = dict(zip(keys, values))
json_object = json.dumps(dictionary, indent = 4)
jsonFile = open("output.json", "w")
jsonFile.write(json_object)
jsonFile.close()
print(json_object)
print("--------------------------------------")

nlp.add_pipe('language_detector', last=True)
doc = nlp(text)
print(doc._.language)
print("--------------------------------------")