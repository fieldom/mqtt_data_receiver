import matplotlib.pyplot as plt
import json

def get_data_plot():
    with open('data.json') as f:
        data = json.load(f)
        return data

def data_plot():
    data = get_data_plot()
    mov_list = []
    time_list = []
    for i in data["values"]:
        mov_list.append(i["movement"])
        time_list.append(i["time"])
    return time_list, mov_list

plt.title('График датчика движения', fontsize = 14, fontweight = 'bold', color = 'blue')
plt.xlabel('Время', fontsize = 12, color = 'black')
plt.ylabel('Ед. измерения движения', fontsize = 12, color = 'black')
plt.plot(*data_plot(), label = 'Значение движения')
plt.legend()
plt.grid()
plt.show()