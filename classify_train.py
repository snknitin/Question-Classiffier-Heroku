import os
from stat_parser import Parser
parser=Parser()
DATA_FILE=os.path.join(os.getcwd(),"Data/queries.10k.txt")


def is_question(sentence):
    """
    This is the helper function to call in the predict function of the Flask API
    :param sentence:
    :return: Boolean value for it being a question
    """
    result = parser.parse(sentence)[0]
    return ["n/a","QUESTION_CODE"][result=="SBARQ"]


class Solution(object):
    def __init__(self):
        print("Initializing Data Loader...")
        # Load Parser and process it
        self.parser = Parser()
        self.count=0

    def is_question(self,sentence):
        """
        Class function for the boolean tagging
        :param sentence:
        :return:
        """
        self.count+=1 # To check which line gives error
        print(self.count)
        result = str(self.parser.parse(sentence)).split()
        if '(SBARQ' in result[0]:
            return "QUESTION_CODE"
        else:
            return "n/a"


    def question_classify(self):
        """
        This function classifies each sentence in the input file and outputs a tsv into a result.txt file
        :return: result.txt file
        """
        with open(DATA_FILE, 'r') as doc:
            with open("result.txt",'w') as target:
                dat = doc.read()
                lines = dat.splitlines()
                for line in lines[1:]:
                    query,freq = line.strip().split("\t")
                    try:
                        # Since some sentences may not have any valid parse
                        is_q = self.is_question(query)
                        bin_val=[0,1][is_q=="QUESTION_CODE"]
                    except TypeError:
                        # It is highly likely that it ont be a question
                        is_q = "n/a"
                        bin_val=0

                    target.write("%s\t%s\t%s\n" % (query,bin_val,is_q ))
            target.close()
        doc.close()


if __name__=="__main__":
    s=Solution()
    # Uncomment the next line for the question tagging
    #s.question_classify()
    print(s.is_question("How old is barack obama?"))
    print(s.is_question("How old is barack obama"))





