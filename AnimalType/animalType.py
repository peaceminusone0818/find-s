import csv

animal_dataset = []

with open('zoo.data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        animal_dataset.append(row)

#animal_dataset = [animal[1:] for animal in animal_dataset]

dataset_attributes = ['name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed',
                      'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize']
attributes = len(animal_dataset[0])

no_of_animal_types = 7

animal_types = ['mammal', 'bird', 'reptilia', 'fish', 'amphibias', 'insect', 'other']

target_concept = ['x'] * (attributes-1)
target_concept = [target_concept] * no_of_animal_types

def finds(instance_attribute, hypotheses):
    if hypotheses == 'x':
        return instance_attribute
    elif hypotheses == '?':
        return '?'
    else:
        if hypotheses == instance_attribute:
            return hypotheses
        else:
            return '?'

for animal in animal_dataset:
    target = int(animal[attributes-1])
    target_concept[target-1] = list(map(finds, animal, target_concept[target-1]))

print('The target concept for the Animal Type data set is :')
print(str(dataset_attributes))
for animal in range(0, no_of_animal_types):
    print('For '+animal_types[animal]+' : '+str(target_concept[animal]))




