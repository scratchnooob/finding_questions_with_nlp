# finding_questions_with_nlp
##approach
separate the line by sentences using split(".")
check for the first and last word as indication of interrogation e.g. having first words as what, who , which , was or last word  having "?" using spacy
check for any verb(e.g. is , do , what, ) in the sentence body followed by noun or pronoun idicates a question (e.g. so, is it raining, )
as soon as you identify the question in the line return 1 
save the results to the txt file
