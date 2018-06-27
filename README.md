# Question-Classiffier-Heroku
Creating a question classifier and hosting the flask app on heroku within 3 hours

## Data

Since the training data only comprises of the Search query and the Hot degree off the query

    hindi movies for adults	        595
    are panda dogs real	            383
    asuedraw winning numbers	      478
    sentry replacement keys	        608
    rebuilding nicad battery packs	541

This is also unlabeled so it is really diffficult to understand if a query is a question


## Approach


* One way could be to take a validation set and annotate it with good split of questions and non-questions. That isn't a feasible option since we can't label it properly

* Second way could be to create a scoring function and decide on a threshold for what could be a question based on a set of features like if it has a question word. This could involve using statistical features like tf-idf scores after removing the stop words.

* Since these are search queries, we can't expect them to have a defining question mark and the mere presence of a ? doesn't necessarily mean it is a question because these are user entered search strings

  * List of question starter words could be 

          Who, What, When ,Where, Why, How, Do, Is, Can, Does, Should, Are
  * POS tag combinations of similar questions can be used to create a Grammar for a parse
    
## Approach used

I used the stats_parser package to create a parse tree for each sentence. Questions have the **SBARQ** node as root. 
    
## How to run

The requirements for this project are present in the requirements.txt file with a redirection to the stats_parser module.
This has been deployed on Heroku.

The deploy.py is the flask application which can run on localhost as well

    python deploy.py

The classify_train.py is the script hass a method called question_classify that writes the transformed output as per the specification
