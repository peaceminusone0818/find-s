import csv

weather_dataset = []

# Import the data from the CSV file
with open('enjoysport.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        weather_dataset.append(row)

# The attributes that describe the weather
dataset_attributes = ['Sky', 'AirTemp', 'Humidity', 'Wind', 'Water', 'Forecast']

# Initial hypothesis, which is the most specific hypothesis
target_concept = ['0', '0', '0', '0', '0', '0']

# Function that compares an attr. from a single positive training data and an attr. from the current hypothesis
# Returns the instance attr. if 0, the same attr. if they are the same and a ? if they are different
def finds(instance_attribute, hypotheses):
    if hypotheses == '0':
        return instance_attribute
    elif hypotheses == '?':
        return '?'
    else:
        if hypotheses == instance_attribute:
            return hypotheses
        else:
            return '?'

# Runs all the training data through the map function
for instance in weather_dataset:
    if instance[6] == '1':
        target_concept = list(map(finds, instance, target_concept))

# Displays the final hypothesis
print('The target concept for the Enjoy Sport data set is : '+str(dataset_attributes)+' => '+str(target_concept))