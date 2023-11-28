import matplotlib.pyplot as plt
import json

def get_data_plot():
    with open('data.json') as f:
        data = json.load(f)
        return data

def data_plot():
    data = get_data_plot()
    light_list = []
    time_list = []
    for i in data["values"]:
        light_list.append(i["movement"])
        time_list.append(i["time"])
    return time_list, light_list

plt.title('График датчика освещения', fontsize = 14, fontweight = 'bold', color = 'blue')
plt.xlabel('Время', fontsize = 12, color = 'black')
plt.ylabel('Люксы', fontsize = 12, color = 'black')
plt.plot(*data_plot(), label = 'Значение освещения')
plt.legend()
plt.grid()
plt.show()