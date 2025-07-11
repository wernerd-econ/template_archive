import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

### DEFINE
def main():
    df = pd.read_csv('output/data_merged.csv')
    plot_data(df)
    df = clean_data(df)
    df.to_csv('output/data_cleaned.csv', index = False)

def plot_data(df):
    #plt.hist(df['chips_sold'])
    chips = df['chips_sold']
    plt.hist(chips, weights=np.ones(len(chips)) / len(chips))
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.xlabel('Chips Sold')
    plt.ylabel('Percentage')
    plt.title('Histogram of Chips Sold (in %)')
    plt.savefig('output/chips_sold.pdf')

def clean_data(df):
    df['chips_sold'][df['chips_sold'] == -999999] = np.nan
    return(df)
    
### EXECUTE
main()
