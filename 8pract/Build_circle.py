import numpy as np
import matplotlib.pyplot as plt
import json

def get_data_from_json(filename):
    with open(filename, 'r') as file:
        file_data = json.load(file)

    return file_data

json_data = get_data_from_json("data.json")

first = second = third = absolute = 0

for i in json_data:
    if 200 <= float(i.get('light')) <= 300:
       first += 1
       absolute += 1
    elif 300 < float(i.get('light')) <= 400:
       second += 1
       absolute += 1
    else:
        absolute += 1
        third += 1


y = np.array([first, second, third])
mylabels = ["200-300", "300-400", "400+"]

plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle= 90)
plt.legend(title = "Кол-во записей показаний освещенности")
plt.show()



