import pandas as pd
import matplotlib.pyplot as plt


class CountryVisitors:
    df = pd.read_excel('IMVA.xls')
    print("")
    print(df.columns)
    print("")

    df = df.replace('na', 0, regex=True)
    countries = df[['Belgium & Luxembourg', 'Denmark', 'Finland', 'France', 'Germany',
                    'Italy', 'Netherlands', 'Norway', 'Rep Of Ireland',
                    'Russian Federation', 'Spain', 'Sweden', 'Switzerland',
                    'United Kingdom']]
    print(countries.head(120))
    print("")
    dft = df['Periods'].str.split(' ', n=1, expand=True)
    dft.head()
    print(dft.head(120))

    countries_list = ['Belgium & Luxembourg', 'Denmark', 'Finland', 'France', 'Germany',
                      'Italy', 'Netherlands', 'Norway', 'Rep Of Ireland',
                      'Russian Federation', 'Spain', 'Sweden', 'Switzerland',
                      'United Kingdom']
    total_countries = {"Country": [], "Total Visitors": []}
    for x in countries_list:
        total_countries["Total Visitors"].append(df[x].sum())
        total_countries["Country"].append(x)

    total_countries = pd.DataFrame.from_dict(total_countries)
    total_countries.sort_values(by=["Total Visitors"], inplace=True, ascending=False)
    total_countries.reset_index(drop=True, inplace=True)

    print("")
    print("Total visitors for each country in Europe")
    print(total_countries)
    print("")
    print("Top 3 Countries in Europe")
    print(total_countries.head(3))
    print("")
    Country = total_countries["Country"].to_list()
    Total = total_countries["Total Visitors"].to_list()

    plt.figure(figsize=(10, 5))
    plt.gcf().subplots_adjust(bottom=0.40)
    plt.xticks(range(len(Country)), Country, rotation='vertical')
    plt.bar(total_countries["Country"].tolist(), total_countries["Total Visitors"].tolist())
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.savefig("All_Countries.jpg")
    plt.show()

    plt.figure(figsize=(7, 5))
    plt.bar(total_countries["Country"].head(3).tolist(), total_countries["Total Visitors"].head(3).tolist())
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.savefig("Top_3_Countries.jpg")
    plt.show()

    df1 = df[["United Kingdom", "Germany", "France"]]

    total = round(df1.values.sum(), 0)
    print("The total no. of visitors for the top 3 countries is", total)

    mean = round(total / 3, 0)
    print("The mean value for the top 3 countries is", mean)
