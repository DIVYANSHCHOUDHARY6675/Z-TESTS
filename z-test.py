import csv 
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objects as go 
df=pd.read_csv("studentm.csv")
data=df["Math_score"].tolist()
mean=statistics.mean(data)
mode=statistics.mode(data)
median=statistics.median(data)
sd=statistics.stdev(data)
print(mean)
print(mode)
print(median)
print(sd)
def random_mean(counter): 
    dataset=[]
    for i in range (0,counter):
        number=random.randint(0,len(data)-1)
        value=data[number]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean    

def setup():
    mean_list=[]
    for i in range (0,1000):
        set_of_means=random_mean(100)
        mean_list.append(set_of_means)
    mean=statistics.mean(mean_list)
    sd=statistics.stdev(mean_list)
    print("The mean of sampling distributing ",str(mean))
    print("The sd of sampling distributing ",str(sd))
    fig=ff.create_distplot([mean_list],["MATHS(MARKS)"],show_hist=True)    
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0.20], mode="lines", name="MEAN"))
    fig.show()

setup()

fig=ff.create_distplot([data],["Math_score"],show_hist=False)

fig.show()


