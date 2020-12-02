import pandas as pd
from matplotlib import pyplot as plt

def create_graph(country, desc, y):
    # Parse Data
    happiness_data = pd.read_csv('CSVs/Happiness/2015.csv')
    country_data = happiness_data[happiness_data.Country == country]
    for i in range(16, 20):
        happiness_data = pd.read_csv('CSVs/Happiness/20' + str(i) + '.csv')
        country_data = country_data.append(happiness_data[happiness_data.Country == country])
    country_data.insert(0, 'Year', ['2015', '2016', '2017', '2018', '2019'])
    
    country_mod = country_data[['Year', 'Score','Economy', 'Health', 'Generosity', 'Freedom']]
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    if y == 'Happiness':
        lns1 = ax1.plot(country_mod.Year, country_mod.Score, color=color, label=y)
    elif y == 'Health':
        lns1 = ax1.plot(country_mod.Year, country_mod.Health, color=color, label=y)
    elif y == 'Generosity':
        lns1 = ax1.plot(country_mod.Year, country_mod.Generosity, color=color, label=y)
    elif y == 'Freedom':
        lns1 = ax1.plot(country_mod.Year, country_mod.Freedom, color=color, label=y)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'

    lns2 = ax2.plot(country_mod.Year, country_mod.Economy, color=color, label="Economy")

    lns = lns1+lns2
    labs = [l.get_label() for l in lns]
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()

    lines = lines_1 + lines_2
    labels = labels_1 + labels_2

    ax1.legend(lines, labels, loc=0)
    ax1.set_title(title)
    ax1.set_xlabel("Year")
    ax1.set_ylabel(y + " Score")
    ax2.set_ylabel("GDP Per Capita")
    fig.tight_layout()
    plt.savefig("output/" + country + "_" + y + ".png")

while True:
    country = input("Input in a country: ")
    options = ['Happiness', 'Health', 'Generosity', 'Freedom']
    y = input("Input in the y-axis: ")
    while y not in options:
        y = input("Invalid choice. Input in y-axis: ")
    title = input("Title the graph: ")
    create_graph(country, title, y)
    if input("Continue? (y/n) ") == 'n':
        break
