import csv
import pandas as pd
import plotly.express as px


df=pd.read_csv("studentidlevelattempt.csv")
student_df=df.loc[df["student_id"]=="TRL_987"]
print(df.groupby("level")["attempt"].mean())
fig= px.scatter(df, x="level", y = "attempt", color = "student_id",size_max= 60)
x=df.groupby("level")["attempt"].mean(),
y=['Level 1','Level 2','Level 3','Level 4'],
orientation = 'h'
fig.show()