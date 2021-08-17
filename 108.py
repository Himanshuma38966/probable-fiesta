import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff

df=pd.read_csv("data2.csv")
fig=ff.create_distplot([df["Height(Inches)"].tolist()],["height"],show_hist = False)
fig.show()