''' Counting key skills from vacancy requests and summarise them'''

import matplotlib.pyplot as plt

def stat():
    ''' To count statitic of skills frequency '''

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

        top20 = {}
        for i in sorted(d, key=lambda x: (-d[x][0], d[x][1]))[:20]:
            top20[d[i][1]] = d[i][0]

        print(f"Всего вакансий = {hm}, из них уникальных = {total}")

        for j, i in enumerate(sorted(d, key=lambda x: (-d[x][0], d[x][1])), 1):
            print(f"{j:>3} {d[i][1]:<28} {d[i][0]:>3} {round(d[i][0] / total, 4):6.2%}")
            print(f"{j:>3} {d[i][1]:<28} {d[i][0]:>3} {round(d[i][0] / total, 4):6.2%}", file=fo)
            if j % 10 == 0:
                pass
                input("-------------")


def plot_matplotlib():
    ''' Graphic chat on Top20  (matplotlib version)'''
    import matplotlib as plt
    import pandas as pd
    # d = {'SQL': 24, 'PostgreSQL': 18, 'Git': 15, 'Linux': 13, 'Английский': 10, 'docker': 9, 'Django Framework': 8, 'MySQL': 6, 'ClickHouse': 5, 'Kubernetes': 5, 'RabbitMQ': 5, 'Tableau': 5, 'flask': 5, 'Apache Airflow': 4, 'Redis': 4, 'ООП': 4, 'C/C++': 3, 'DWH': 3, 'Data Mining': 3, 'Golang': 3}
    dind = sorted(top20.keys(), key=lambda x: (top20[x], x))
    df = pd.Series(top20, index=dind)
    print(df)
    df.plot(kind='barh')


def plot_seaborn():
    ''' Graphic chat on Top20  (seaborn version)'''
    import matplotlib.pyplot as plt
    import seaborn as sns
    d = {'SQL': 24, 'PostgreSQL': 18, 'Git': 15, 'Linux': 13, 'Английский': 10, 'docker': 9, 'Django Framework': 8,
         'MySQL': 6, 'ClickHouse': 5, 'Kubernetes': 5, 'RabbitMQ': 5, 'Tableau': 5, 'flask': 5, 'Apache Airflow': 4,
         'Redis': 4, 'ООП': 4, 'C/C++': 3, 'DWH': 3, 'Data Mining': 3, 'Golang': 3}

    y = list(d.values())
    x = list(d.keys())

    sns.barplot(x=y, y=x)

