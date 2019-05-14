from QuestionConceptExtractor.ConceptExtractor.ConceptExtractor import *
from QuestionConceptExtractor.DatabaseReader.ReadQuestion import *

# This is a test code and an example to show how the questionnaire concept extraction process works. This includes the following
# 1. Loads an original question from dobe database
# 2. Tokenize the question text and return the concepts in the text. The concept extraction is done in three ways after
# removing the stop words and the punctuation marks
# 2.1 Concepts in their lose sense which includes individual tokens other than stop words
# 2.2 Concepts in strict sense which only includes nouns from 2.1
# 2.3 Concepts in a very strict sense which includes concepts that have an entry in Germanet
#
# Run this example to test which of the above options work for you
#
# Prerequisits
# 1. Make sure you install mysql connector and all the necessary dependencies in python
# 2. Make sure germanet is loaded from  mongodb (follow instruction here https://pypi.org/project/pygermanet/)
# 3. make sure mysql is up and running with the correct credential.
# 4. This example is for questions under questionnaire 53. results can be compared with the expert evaluation here.

# Additional steps
# You may want to remove duplicate concepts (specially different cases (upper,lower))
# You may also link each question with each concept and send it back to the database.

test=ConceptExtractor()

test.extract("Rindviehzucht und Milchwirtschaft")

testQ=QuestionReader()
testQ.readQuestionByID(53)
# for record in testQ.records:
#     print(record[0], test.extract(record[1]))


for record in testQ.records:
    print("Question: ", record[0], record[1])
    print("All Concepts: \n ", test.extract(record[1]))
    print("Strictly Noun Concepts: \n ", test.extract_nouns_only_as_concept(record[1]))
    print("Germanet Concepts: \n ", test.extract_germanet_concepts_only(record[1]))
    print("=================================")
