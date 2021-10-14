import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("./data/Intercept_2021.csv")
    df["Date Intercepted"] = pd.to_datetime(df["Date Intercepted"], dayfirst=True)
    grams = df.groupby(df['Date Intercepted'].dt.month)['Weight (in grams)'].sum()
    result = [g / 1_000_000 for g in grams]
    n_months = grams.index.tolist()
    months = month_list(n_months)

    plt.bar(months, result, color='#335522')

    plt.ylabel("Tonnes")
    plt.title("Monthly Intercepts 2021")
    plt.savefig('year.png')
    plt.show()

def month_list(month_nums):
    months= { 1: "Jan",2: "Feb",3: "Mar",4: "Apr",5: "may",6: "Jun",7: "Jul",8: "Aug",9: "Sep",10: "Oct",11: "Nov",12: "Dec"}
    return [months[num] for num in month_nums]
    

if __name__ == "__main__":
    main()