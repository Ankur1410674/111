import random
import csv 
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import typing as counter
import statistics as st 
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df["Math_score"].tolist()
def randomsetoffmean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex =  random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

meanlist=[]
for i in range(1,1000):
    setoffmeans=randomsetoffmean(100)
    meanlist.append(setoffmeans)
           
df1=pd.read_csv("data1.csv")
data1=df1["Math_score"].tolist()
mean1 = st.mean(data1)
fig = ff.create_distplot([meanlist],["Math_score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name="mean1"))
fig.show()







