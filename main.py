import pandas as pd
from matplotlib import pyplot as plt


def create_graph(country):
    happiness_data = pd.read_csv('CSVs/Happiness/2015.csv')
    us_happiness = happiness_data[happiness_data.Country == country]
    for i in range(16, 20):
        happiness_data = pd.read_csv('CSVs/Happiness/20' + str(i) + '.csv')
        us_happiness = us_happiness.append(happiness_data[happiness_data.Country == country])
    us_happiness.insert(0, 'Year', ['2015', '2016', '2017', '2018', '2019'])
    
    # Health vs Economy Graph
    us_score = us_happiness[['Year', 'Score','Economy', 'Health', 'Generosity', 'Freedom']]
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    lns1 = ax1.plot(us_score.Year, us_score.Health, color=color, label="Health")

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    lns2 = ax2.plot(us_score.Year, us_score.Economy, color=color, label="Economy")

    lns = lns1+lns2
    labs = [l.get_label() for l in lns]
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()

    lines = lines_1 + lines_2
    labels = labels_1 + labels_2

    ax1.legend(lines, labels, loc=0)
    ax1.set_title(country + " Comparison of Money and Health (2015-2019)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Health Score based on Life Expectancy")
    ax2.set_ylabel("GDP Per Capita")
    fig.tight_layout()
    plt.savefig("output/" + country + "_Health.svg")

    #Happiness vs Economy Graph
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    lns1 = ax1.plot(us_score.Year, us_score.Score, color=color, label="Score")

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    lns2 = ax2.plot(us_score.Year, us_score.Economy, color=color, label="Economy")

    lns = lns1+lns2
    labs = [l.get_label() for l in lns]
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()

    lines = lines_1 + lines_2
    labels = labels_1 + labels_2

    ax1.legend(lines, labels, loc=0)
    ax1.set_title(country + " Comparison of Money and Happiness (2015-2019)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Happiness Score")
    ax2.set_ylabel("GDP Per Capita")
    fig.tight_layout()
    plt.savefig("output/" + country + "_Happiness.svg")

create_graph("United Kingdom")
create_graph("United States")
create_graph("China")
create_graph("Japan")
