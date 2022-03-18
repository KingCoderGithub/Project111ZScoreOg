import statistics as st
import plotly.figure_factory as ff
import pandas as pd
import csv
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["reading_time"].to_list()
fig = ff.create_distplot([data], ["Math Score"], show_hist=False)
fig.show()

meanMain = st.mean(data)
stdMain = st.stdev(data)

print("Mean of the Math Marks : ", meanMain)
print("Standard Deviation of Math Marks", meanMain)

def randomSetOfMean(counter) :
    dataSet = []
    
    for i in range (0, counter) :
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)
    
    mean = st.mean(dataSet)
    return mean

meanList = []

for i in range (0, 1000) :
    setOfMeans = randomSetOfMean(100)
    meanList.append(setOfMeans)

# Mean and Sd Of sample data
sampleMean = st.mean(meanList)
sampleSTD = st.stdev(meanList)

print("Mean of the Sample Math Marks : ", sampleMean)
print("Standard Deviation of Sample Math Marks", sampleSTD)

# Calculating SD 1, 2, 3 for sample data
firstSDStart , firstSDEnd = sampleMean - sampleSTD, sampleMean + sampleSTD
secondSDStart , secondSDEnd = sampleMean -(2*sampleSTD), sampleMean + (2*sampleSTD)
thirdSDStart , thirdSDEnd = sampleMean -(3*sampleSTD), sampleMean + (3*sampleSTD)

print("STD 1", firstSDStart, firstSDEnd)
print("STD 2", secondSDStart, secondSDEnd)
print("STD 3", thirdSDStart, thirdSDEnd)

# Finding th emean for Method 1 of Intervention
df = pd.read_csv("sampledata.csv")
data = df["reading_time"].to_list()
meanOfMTD1 = st.mean(data)

print("The mean of Method 1: ", meanOfMTD1)

fig = ff.create_distplot([meanList], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x = [sampleMean, sampleMean], y = [0, 0.17], mode="lines", name = "mean"))
fig.add_trace(go.Scatter(x = [meanOfMTD1, meanOfMTD1], y = [0, 0.17], mode="lines", name="method1"))
fig.add_trace(go.Scatter(x = [firstSDEnd, firstSDEnd], y = [0, 0.17], mode="lines", name = "SD1"))
fig.add_trace(go.Scatter(x = [secondSDEnd, secondSDEnd], y = [0, 0.17], mode="lines", name = "SD2"))
fig.add_trace(go.Scatter(x = [thirdSDEnd, thirdSDEnd], y = [0, 0.17], mode="lines", name = "SD3"))
fig.show()


# Finding z-score
zScore = (sampleMean - meanOfMTD1) / sampleSTD
print("The z-Score is", zScore)