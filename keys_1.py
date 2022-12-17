''' Counting key skills from vacancy requests and summarise them'''

import matplotlib.pyplot as plt

d = {}
top20 = {}
ss = []
def stat():
    ''' To count statitic of skills frequency '''

    with open('key_skills.txt', encoding = 'utf-8') as fi:
        total, hm = 0, 0
        for s in fi:
            if s.strip() == '': continue
            hm += 1
            if s in ss: continue
            ss.append(s)
            total += 1
            for ii in s.split(','):
                i = ii.strip().lower()
                if i == 'алгоритмы':
                    i = 'алгоритмы и структуры данных'
                    ii = 'Алгоритмы и структуры данных'
                elif i == 'django':
                    i = 'django framework'
                    ii = 'Django Framework'
                elif i == 'airflow':
                    i = 'Apache Airflow'.lower()
                    ii = 'Apache Airflow'
                elif i == 'английский язык':
                    i = 'английский'
                    ii = 'Английский'
                elif i == 'c' or i == 'c++' or i == 'c/c++':
                    i = 'c/c++'
                    ii = 'C/C++'
                elif i == 'ml' or i == 'machine learning':
                    i == 'ml'
                    ii = 'Machine Learning'
                elif i == 'js' or i == 'javascript':
                    i == 'js'
                    ii = 'Javascript'

                elif i == ' ' or i == '':
                    continue

                if i not in ['python']:
                    if i not in d:
                        d[i] = [0, ii.strip()]
                    d[i][0] = d[i][0] + 1
        for i in sorted(d, key=lambda x: (-d[x][0], d[x][1]))[:20]:
            top20[d[i][1]] = d[i][0]
        return hm, total

def stat_file():
    ''' To count statitic of skills frequency and to write results to file'''

    ss = []
    with open('key_skills.txt', encoding = 'utf-8') as fi, open('result_keys.txt', 'w', encoding = 'utf-8') as fo:
        d = {}
        total, hm = 0, 0
        for s in fi:
            if s.strip() == '': continue
            hm += 1
            if s in ss: continue
            ss.append(s)
            total += 1
            for ii in s.split(','):
                i = ii.strip().lower()
                if i == 'алгоритмы':
                    i = 'алгоритмы и структуры данных'
                    ii = 'Алгоритмы и структуры данных'
                elif i == 'django':
                    i = 'django framework'
                    ii = 'Django Framework'
                elif i == 'airflow':
                    i = 'Apache Airflow'.lower()
                    ii = 'Apache Airflow'
                elif i == 'английский язык':
                    i = 'английский'
                    ii = 'Английский'
                elif i == 'c' or i == 'c++' or i == 'c/c++':
                    i = 'c/c++'
                    ii = 'C/C++'
                elif i == 'ml' or i == 'machine learning':
                    i == 'ml'
                    ii = 'Machine Learning'
                elif i == 'js' or i == 'javascript':
                    i == 'js'
                    ii = 'Javascript'

                elif i == ' ' or i == '':
                    continue

                if i not in ['python']:
                    if i not in d:
                        d[i] = [0, ii.strip()]
                    d[i][0] = d[i][0] + 1
        print('Start to write')
        for j, i in enumerate(sorted(d, key=lambda x: (-d[x][0], d[x][1])), 1):
            #print(f"{j:>3} {d[i][1]:<28} {d[i][0]:>3} {round(d[i][0] / total, 4):6.2%}", )
            print(f"{j:>3} {d[i][1]:<28} {d[i][0]:>3} {round(d[i][0] / total, 4):6.2%}", file=fo)


def stat_to_screen():
    ''' function of displaing result to screen'''

    hm, total = stat()
    print(f"Всего вакансий = {hm}, из них уникальных = {total}")
    input("-------------")
    for j, i in enumerate(sorted(d, key=lambda x: (-d[x][0], d[x][1])), 1):
        print(f"{j:>3} {d[i][1]:<28} {d[i][0]:>3} {round(d[i][0] / total, 4):6.2%}")
        if j % 10 == 0:
            input("-------------")
    print("-------------")
    return
def plot_matplotlib():
    ''' Graphic chat on Top20  (matplotlib version)'''

    import matplotlib.pyplot as plt
    import pandas as pd

    if not top20: stat()
    dind = sorted(top20.keys(), key=lambda x: (top20[x], x))
    df = pd.Series(top20, index=dind)
    df.plot(kind='barh')
    plt.show()
    #input('more?')


def plot_seaborn():
    ''' Graphic chat on Top20  (seaborn version)'''
    import matplotlib.pyplot as plt
    import seaborn as sns

    if not top20: stat()
    y = list(top20.values())
    x = list(top20.keys())

    sns.barplot(x=y, y=x)
    plt.show()
    #input('more?')

def search():
    ''' The search of strings (vacancies) which have all substring divided by commas '''

    if not ss: stat()
    while True:
        x = input('Введите подстроки, разделенные запятыми:')
        if x == '': break
        y = x.lower().strip().split(',')
        hm = 0
        for i in ss:
            j = i.lower()
            yn = True
            for z in y:
                if z.strip() not in j:
                    yn = False
                    break
            if yn:
                hm += 1
                print(hm, i.strip())
        print()
        print(f'Найдено {hm} из {len(ss)}')
    return



