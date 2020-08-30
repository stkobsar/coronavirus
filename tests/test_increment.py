import pandas as pd
import coronavirus.functionalities.increment_days as id


CSV = "https://covid.ourworldindata.org/data/ecdc/full_data.csv"

df_coronavirus = pd.read_csv(CSV)
condition = df_coronavirus["location"] == "Spain"
df_cond = df_coronavirus[condition]
head_csv = df_cond.head(42)
print(head_csv)

field = "total_cases"


def test_increment(csv=head_csv):
    increment_test_result = id.pl_increment_cases(csv, field=field)
    assert increment_test_result[-1] == 1

#increment = increment_test(head_csv)
#print(increment)

