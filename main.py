import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from prettytable import PrettyTable

data_file_names = ['Intercept_2021.csv', 'Intercept-KPI-Historic-21.csv']
data_directory = './data/'

def main():
    data_files = [f'{data_directory}{file}' for file in data_file_names]
    df = fetch_all_data(data_files)
    df["Date Intercepted"] = pd.to_datetime(df["Date Intercepted"], dayfirst=True)
    monthly_totals = df.groupby(df['Date Intercepted'].dt.month)['Weight (in grams)'].sum()
    month_list = month_list_names(monthly_totals.index.tolist())

    plot_year(monthly_totals, month_list)
    print_table(monthly_totals, month_list)

def fetch_all_data(data_files: list):
    return  pd.concat(map(pd.read_csv, data_files), ignore_index=True)

    
def plot_year(data, months):
    plt.bar(months, data / 1_000_000, color='#335522')
    plt.ylabel("Tonnes")
    plt.title("Monthly Intercepts 2021")
    plt.savefig('./output/year.png')
    plt.show()

def print_table(data, month):
    x = PrettyTable()
    x.field_names = ['Month', 'Weight KG', 'Meals saved']
    for i, row in enumerate(data):
        x.add_row([month[i], f'{int(row/1000):,}', f'{int(row/420):,}'])
    x.add_row(['', '', ''])
    x.add_row(['Tot', f'{int(sum(data)/1000):,}', f'{int(sum(data)/420):,}'])
    print(x)

def month_list_names(month_nums):
    months= { 1: "Jan",2: "Feb",3: "Mar",4: "Apr",5: "May",6: "Jun",7: "Jul",8: "Aug",9: "Sep",10: "Oct",11: "Nov",12: "Dec"}
    return [months[num] for num in month_nums]
    
if __name__ == "__main__":
    main()