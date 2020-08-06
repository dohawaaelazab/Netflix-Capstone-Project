#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# In[2]:


# Step 2 
netflix_stocks = pd.read_csv('NFLX.csv')
dowjones_stocks = pd.read_csv("DJI.csv")
netflix_stocks_quarterly = pd.read_csv("NFLX_daily_by_quarter.csv")


# In[3]:


# Step 3
print('2017')
print('yyyy-mm-dd')
print('dowjones and netflix are the average per month')
print('netflix_stocks is the average of each while the quarterly is the overall')


# In[4]:


# Step 4 
print(netflix_stocks.head())
netflix_stocks = netflix_stocks.rename(columns={'Adj Close':'Price'})
netflix_stocks_quarterly = netflix_stocks_quarterly.rename(columns={'Adj Close':'Price'})
dowjones_stocks = dowjones_stocks.rename(columns={'Adj Close':'Price'})
print(netflix_stocks.head())
print(netflix_stocks_quarterly.head())
print(dowjones_stocks.head())


# In[5]:


# Step 5
ax = sns.violinplot(x='Quarter',y='Price',data=netflix_stocks_quarterly)
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
ax.set_ylabel('Closing Stock Price')
ax.set_xlabel( "Business Quarters in 2017")
plt.show()


# In[7]:


# Step 6
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
plt.scatter(x_positions,earnings_actual,color='red',alpha=0.5)
plt.scatter(x_positions,earnings_estimate,color='blue',alpha=0.5)
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.title("Earnings Per Share in Cents")
plt.show()


# In[6]:


# Step 7
# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]
# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.5 # Width of each bar
bars1_x = [t*element + w*n for element in range(d)]
# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.5 # Width of each bar
bars2_x = [t*element + w*n for element in range(d)]
middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]
plt.bar(bars1_x , revenue_by_quarter)
plt.bar(bars2_x,earnings_by_quarter)
plt.legend(labels)
plt.title('Diffrence between earnings and revenue')
plt.xticks(middle_x,quarter_labels)
plt.show()


# In[8]:


# Step 8
# Left plot Netflix
ax1 = plt.subplot(1, 2, 1)
sns.barplot(x='Date',y='Price',data=netflix_stocks)
plt.xticks(rotation=90)
ax1.set_title('Netflix')
ax1.set_xlabel("Date")
ax1.set_ylabel("Stock Price")
figure1 = plt.gcf()

# Right plot Dow Jones
ax2 = plt.subplot(1, 2, 2)
sns.barplot(x="Date",y='Price',data=dowjones_stocks)
ax2.set_title("Dow Jones")
plt.subplots_adjust(wspace=.5)
ax2.set_ylabel("Stock Price")
ax2.set_xlabel("Date")

plt.xticks(rotation=90)
figure2 = plt.gcf()
figure2.set_size_inches(20, 11)
#plt.savefig("2sidebarplot.png")

plt.show()

