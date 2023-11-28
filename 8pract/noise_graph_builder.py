import matplotlib.pyplot as plt
import json

def get_data_plot():
    with open('data.json') as f:
        data = json.load(f)
        return data

def data_plot():
    data = get_data_plot()
    noise_list = []
    time_list = []
    for i in data["values"]:
        noise_list.append(i["noise"])
        time_list.append(i["time"])
    return time_list, noise_list

plt.title('График датчика шума', fontsize = 14, fontweight = 'bold', color = 'blue')
plt.xlabel('Время', fontsize = 12, color = 'black')
plt.ylabel('Децибелы', fontsize = 12, color = 'black')
plt.plot(*data_plot(), label = 'Значение шума')
plt.legend()
plt.grid()
plt.show()