import csv

weather_dataset = []

with open('enjoysport.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        weather_dataset.append(row)

dataset_attributes = ['Sky', 'AirTemp', 'Humidity', 'Wind', 'Water', 'Forecast']

target_concept = ['0', '0', '0', '0', '0', '0']


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


for instance in weather_dataset:
    if instance[6] == '1':
        target_concept = list(map(finds, instance, target_concept))

print('The target concept for the Enjoy Sport data set is : '+str(dataset_attributes)+' => '+str(target_concept))
