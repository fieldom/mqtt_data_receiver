from datetime import datetime

import matplotlib.pyplot as plt
import json


# Функция получения данных из json-файла
def get_data_from_json(filename):
    with open(filename, 'r') as file:
        file_data = json.load(file)

    return file_data


def create_plots(plots_data_lists):
    # Создание графиков для отрисовки данных
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))  # Получим окно с 1 колонкой и 2 столбцами графиков

    # fig - окно, в котором будут отрисовываться графики
    # axs содержит в себе список графиков для отрисовки на них значений

    # Задание набора точек для отрисовки
    # Первый аргумент - список значений по оси X, второй аргумент - по оси Y
    axs[0].plot(plots_data_lists['time'], plots_data_lists['movement'], color = 'blue')

    # Задание лейблов для осей и графика
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Movement level')
    axs[0].set_title('Movement')

    # Формирование гистограммы
    axs[1].hist(plots_data_lists['noise'], color='lime')
    axs[1].set_xlabel('Noise level')
    axs[1].set_ylabel('Count')
    axs[1].set_title('Noise')

    return fig, axs


def main():
    plots_data_lists = {
        'movement': [],
        'noise': [],
        'time': [],
        'temperature': [],
        'light': []
    }

    json_data = get_data_from_json("data.json")

    # Заполнение списков с данными, с преобразованием типов
    for json_dict in json_data:
        plots_data_lists['movement'].append(int(json_dict.get('movement')))
        plots_data_lists['time'].append(datetime.fromisoformat(json_dict.get('time')))
        plots_data_lists['noise'].append(float(json_dict.get('noise')))
        plots_data_lists['light'].append(float(json_dict.get('light')))
        plots_data_lists['temperature'].append(str(json_dict.get('temperature')))

    fig, axs = create_plots(plots_data_lists)

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()