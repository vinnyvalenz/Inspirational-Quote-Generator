import pathlib as p
import pandas as pd
import re


def preprocess_data(filename):
    # Open Motivational-Quotes-Database.csv
    data = pd.read_csv(p.Path.cwd().joinpath('../data', 'Motivational-Quotes-Database.csv'))

    # Remove rows where data is inconsistently entered. Then remove the Category and Author columns
    data = data[~data['Quotes'].str.contains('[0-9];', regex=True)]
    del data['Category']
    del data['Author']

    # Convert back into csv
    data.to_csv(str(p.Path.cwd().joinpath('preprocessed_data', filename+'.csv')), index=None)

    # Read in csv and remove quotations
    data1 = open(str(p.Path.cwd().joinpath('preprocessed_data', filename+'.csv'))).read()
    data1 = re.sub('"', '', data1)
    data1 = re.sub('\'', '', data1)

    # Take first 20k entries out of ~45k for Colab
    data2 = data1.split('\n')
    data2 = data2[1:10000]
    f = open(str(p.Path.cwd().joinpath('preprocessed_data', filename+'.txt')), 'w')

    for s in data2:
        f.write(s + "\n")


preprocess_data("mqd2")










