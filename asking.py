import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def extract_data(file, year, countries):
    """
    Function to get input file and the specific countries and the years

    input: 
    filename (string)
    year (array of years)
    countries (array of countries)

    output:
    result (array of the required values for specific years)
    """
    df = pd.read_csv (file ,on_bad_lines='skip')
    result = []
    for k in range(0, len(year)):
        for j in range(0, len(countries)): 
            for i in range (0, len(df[ 'Country Name'])) :
                if df['Country Name'][i] == countries[j]:
                    result.append(df[year[k]][i])
    return result
