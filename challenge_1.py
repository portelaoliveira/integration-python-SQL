import sqlite3

import pandas as pd


def format(value):
    return f"R${value:.2f}"


connection = sqlite3.connect("salarios.sqlite")
salary_table = pd.read_sql("SELECT * FROM Salaries", connection)

salary_table = salary_table.loc[salary_table["Agency"] == "San Francisco", :]
mean_salary_table = salary_table.groupby("Year")[
    ["TotalPay", "TotalPayBenefits"]
].mean()
table_count = salary_table.groupby("Year").count()
table_count = table_count[["Id"]]
table_count = table_count.rename(columns={"Id": "Quantidade"})
table_total = salary_table.groupby("Year")[["TotalPay", "TotalPayBenefits"]].sum()
table_total["TotalPay"] = table_total["TotalPay"].apply(format)
table_total["TotalPayBenefits"] = table_total["TotalPayBenefits"].apply(format)

# print(salary_table.info())
# print(mean_salary_table)
print(table_total)


connection.close()
