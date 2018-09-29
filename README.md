
# find-s
The goal of a concept learning task is to find the hypothesis from a large space of hypotheses that best fits the training examples. The Find-S Algorithm provides one solution to this task.

## Problems/Tasks

### 1. Enjoy Sport
Takes a data set consisting of weather conditions and returns a hypothesis to determine if it is favorable to enjoy a sport or not. 
Weather Attributes = { 'Sky', 'AirTemp', 'Humidity', 'Wind', 'Water', 'Forecast' }
Possible Outcomes = { 'Yes', 'No'}, given by 1 and 0 respectively
  
### 2. Animal Type
Takes a data set consisting of animals and their attributes and returns hypotheses to determine the type of animal species.  The data set was taken from the link provided in the References section.
Animal Attributes = { 'name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize' }
Possible Animal Types = { 'mammal', 'bird', 'reptilia', 'fish', 'amphibias', 'insect', 'other' } 

## Code
You can run the code by following the below steps,
1. Clone the repository to your local system. `git clone https://github.com/anikeshk/find-s.git`
2. Change into the folder of the algorithm you want to run. `cd EnjoySport` or `cd AnimalType`
3. Run the code. `python hello.py` or `python3 hello.py`

**Todo** : A script for the algorithms to analyse test data. 

## References 
1. Machine Learning by Tom M Mitchel 
2. For the animal data set - http://archive.ics.uci.edu/ml/datasets/zoo
