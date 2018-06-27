import os
from time import time
from stat_parser import Parser

DATA_FILE=os.path.join(os.getcwd(),"Data/queries.10k.txt")


def is_question(sentence):
    parser=Parser()
    result = parser.parse(sentence)[0]
    return ["n/a","QUESTION_CODE"][result=="SBARQ"]


class Solution(object):
    def __init__(self):
        print("Initializing Data Loader...")
        # Load dataframe and process it
        self.parser = Parser()
        self.count=0

    def is_question(self,sentence):
        self.count+=1 # To check which line gives error
        print(self.count)
        result = str(self.parser.parse(sentence)).split()
        if '(SBARQ' in result[0]:
            return "QUESTION_CODE"
        else:
            return "n/a"


    def question_classify(self):
        with open(DATA_FILE, 'r') as doc:
            with open("result.txt",'w') as target:
                dat = doc.read()
                lines = dat.splitlines()
                for line in lines[1:]:
                    query,freq = line.strip().split("\t")
                    try:
                        is_q = self.is_question(query)
                        bin_val=[0,1][is_q=="QUESTION_CODE"]
                    except TypeError:
                        is_q = "n/a"
                        bin_val=0

                    target.write("%s\t%s\t%s\n" % (query,bin_val,is_q ))
            target.close()
        doc.close()


if __name__=="__main__":
    s=Solution()
    print(s.is_question("How old is barack obama?"))





