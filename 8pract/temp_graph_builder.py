import matplotlib.pyplot as plt
import json

def get_data_plot():
    with open('data.json') as f:
        data = json.load(f)
        return data

def data_plot():
    data = get_data_plot()
    temp_list = []
    time_list = []
    for i in data["values"]:
        temp_list.append(str(i["temperature"]))
        time_list.append(i["time"])
    return time_list, temp_list

plt.title('График температуры', fontsize = 14, fontweight = 'bold', color = 'blue')
plt.xlabel('Время', fontsize = 12, color = 'black')
plt.ylabel('Градусы', fontsize = 12, color = 'black')
plt.plot(*data_plot(), label = 'Значение температуры')
plt.legend()
plt.grid()
plt.show()