# The goal of the program is to analyse what skills requested from companies for Python development
# The result is the list of skills in descending order + picture of Top20 skills

import keys_1

if __name__ == '__main__':
    while True:
        print("1. Статистика")
        print("2. Matplotlib")
        print("3. Seaborn")
        print("4. Статистика в файл")
        print("0. Выход")
        x = 0
        try:
            x = int(input('==>'))
        except:
            x = 0

        match x:
            case 1: keys_1.stat_to_screen()
            case 2: keys_1.plot_matplotlib()
            case 3: keys_1.plot_seaborn()
            case 4: keys_1.stat_file()
            case 0: break
