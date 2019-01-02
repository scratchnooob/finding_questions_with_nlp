import nltk
import spacy
import sys
nlp = spacy.load('en_core_web_sm')
def line_check(text):
    for x in text.split("."):
        t=isquestion(x)
        if t==1:
            return t
    else:
        return t
def isquestion(sentence):
    start_list=[]
    doc = nlp(sentence)
    question_list=['what',"where","who","whom","whose","when","why","which","how",
                   "when","is","are","did","were","will","would","do"]
    word_list=[]
    pos_list=[]
    for token in doc:
        #print(token.text, token.pos_, token.tag_, token.dep_)
        word_list.append(token.text.lower())
        pos_list.append(token.pos_)
    if len(word_list)==0:
        return 0
    if word_list[0].lower() in question_list or "?" in word_list:
        return 1
    check_for_indirect_question_list=list(set(word_list).intersection(pos_list))
    if len(check_for_indirect_question_list) >0:
        for _ in check_for_indirect_question_list:
            if pos_list[word_list.index(_)+1] in ["NOUN", "PROPN","PRON"]:
                return 1
    else:    
        return 0
with open(sys.arg[1],"r",encoding="utf8") as f:
#with open("testinputs.txt","r",encoding="utf8") as f:
    temp=f.read()
answer_list=[]
i=0
for line in temp.splitlines():
    i+=1
    print(i)
    if line_check(line)==1:
        answer_list.append("1")
    else:
        answer_list.append("0")
with open('./result_file.txt', 'w') as f:
    for item in answer_list:
        f.write("%s\n" % item)
print("results saved in result_file.txt")
