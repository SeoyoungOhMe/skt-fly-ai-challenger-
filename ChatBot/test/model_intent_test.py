import sys
sys.path.append('C:\chatbot_exercise')
from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='..\\..\\train_tools\\dict\\chatbot_dict.bin',
               userdic='..\\..\\utils\\user_dic.tsv')

intent = IntentModel(model_name='../../models/intent/intent_model.h5', proprocess=p)
query = "오늘 탕수육 주문 가능한가요?"
for q in query:
    predict = intent.predict_class(q)
    predict_label = intent.labels[predict]
    print(f"query : {q}\npredict_label : {predict_label}")