import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

data_file_names = ['Intercept_2021.csv', 'Intercept-KPI-Historic-21.csv']
data_directory = '../data/'

def main():
    data_files = [f'{data_directory}{file}' for file in data_file_names]
    df = fetch_all_data(data_files)
    df.to_csv('../output/all_data.csv')
    df["Date Intercepted"] = pd.to_datetime(df["Date Intercepted"], dayfirst=True)
    monthly_totals = df.groupby(df['Date Intercepted'].dt.month)['Weight (in grams)'].sum()
    month_list = month_list_names(monthly_totals.index.tolist())

    plot_year(monthly_totals, month_list)
    print_table(monthly_totals, month_list)
    print('\n')
    print_sum_products(df)

def fetch_all_data(data_files: list):
    return  pd.concat(map(pd.read_csv, data_files), ignore_index=True)

    
def plot_year(data, months: list):
    plt.bar(months, data / 1_000_000, color='#335522')
    plt.ylabel("Tonnes")
    plt.title("Monthly Intercepts 2021")
    plt.savefig('../output/year.png')
    plt.show()

def print_sum_products(df_all):
    x = PrettyTable()
    x.field_names = ['Product', 'Weight KG']
    for product in np.sort(df_all['Product'].unique()):
        total = df_all.loc[df_all['Product'] == product]['Weight (in grams)'].sum()
        x.add_row([f'{product}', f'{round(total/1_000):,}'])
        x.align["Product"] = "l"
    # print(x.get_string(sortby="Product"))
    print(x)

def print_table(data, month):
    x = PrettyTable()
    x.field_names = ['Month', 'Weight KG', 'Meals saved']
    for i, row in enumerate(data):
        x.add_row([month[i], f'{round(row/1000):,}', f'{round(row/420):,}'])
    x.add_row(['', '', ''])
    x.add_row(['Tot', f'{round(sum(data)/1000):,}', f'{round(sum(data)/420):,}'])

    print(x)

def month_list_names(month_nums):
    months= { 1: "Jan",2: "Feb",3: "Mar",4: "Apr",5: "May",6: "Jun",7: "Jul",8: "Aug",9: "Sep",10: "Oct",11: "Nov",12: "Dec"}
    return [months[num] for num in month_nums]
    
if __name__ == "__main__":
    main()