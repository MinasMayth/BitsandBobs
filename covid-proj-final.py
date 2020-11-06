# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:44:33 2020

@author: samya
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures 
import numpy as np
from sklearn.linear_model import LinearRegression
import datetime as dt

data = pd.read_csv("COVID-19")

#Function to change starting date
def range_chooser(country_code):
    data2 = data[(data['countryterritoryCode'] == country_code)]
    
    X = data2['dateRep'][::-1]
    X_new = pd.to_datetime(X)
    X_new = X_new.map(dt.datetime.toordinal)
    X_new = np.sort(np.array(X_new).astype(np.float64)).reshape(-1,1)
    
    #Calculates the earliest stored date in the array and the last one, as these are the limits the graphs
    #can be graphed on. Furthermore, different countries started recording COVID cases at different times
    #So this will automaticall show if the the starting date is different
    first_recorded_date = dt.date.fromordinal(int(X_new[0][0]))
    last_recorded_date = dt.date.fromordinal(int(X_new[-1][0]))
    
    print("Please enter your answers in the format DD/MM/YYYY")
    print("This only works for dates from " + str(first_recorded_date) + " to " + str(last_recorded_date))
    print("Starting Date?")
    date1= input()
    print("Ending Date?")
    date2 = input()
    
    date1_datetime = dt.datetime.strptime(date1, '%d/%m/%Y')
    date1_ordinal = date1_datetime.toordinal()
    
    date2_datetime = dt.datetime.strptime(date2, '%d/%m/%Y')
    date2_ordinal = date2_datetime.toordinal()
    
    result1 = np.where(X_new == date1_ordinal)
    result2 = np.where(X_new == date2_ordinal)
    results = np.dstack((result1[0][0],result2[0][0]))
    return(results)
    

#Main Function
def COVID_data_analyser(country_code):
    data2 = data[(data['countryterritoryCode'] == country_code)]
      
    X = data2['dateRep'][::-1]
    y = data2['cases'][::-1]
    y2 = data2['deaths'][::-1]
    
    
    
    X_new = pd.to_datetime(X)
    X_new = X_new.map(dt.datetime.toordinal)
    X_new = np.sort(np.array(X_new).astype(np.float64)).reshape(-1,1)
    
    
    #Plotting Overall graph for overview- no regression is done here
    fig, ax = plt.subplots(figsize=(10,7.5))
    ax.plot_date(X, y, xdate=True,color='red')
    ax.plot_date(X,y2,color='green')
    fig.autofmt_xdate()
    ax.set_xlim()
    ax.set_ylim(bottom=0)
    plt.xticks(np.arange(0, len(X), step=20))
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of People")
    plt.title("Daily cases and deaths")
    plt.show()
    
    zipped = range_chooser(country_code)
    
    startingdate = zipped[0][0][0]
    endingdate = zipped[0][0][1]
    X = X[startingdate: endingdate]
    X_new = X_new[startingdate:endingdate]
    y = y[startingdate:endingdate]
    y2 = y2[startingdate:endingdate]
    
    #Linear Regression x-y
    lin_reg=LinearRegression()
    lin_reg.fit(X_new,y)
    print("Linear Regression Dates-Cases Score: " + str(lin_reg.score(X_new,y)))
    
    #Linear Regression x-y2
    lin_reg2=LinearRegression()
    lin_reg2.fit(X_new,y2)
    print("Linear Regression Dates-Deaths Score: " + str(lin_reg2.score(X_new,y2)))
    print()
    
    #Polynomial Regression
    poly_reg=PolynomialFeatures(degree=4)
    X_poly=poly_reg.fit_transform(X_new)
    
    #Fitting X_poly-y
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, y)
    print("Polynomial Regression Dates-Cases Score: " + str(pol_reg.score(X_poly,y)))
    
    #Fitting X_poly-y2
    pol_reg2 = LinearRegression()
    pol_reg2.fit(X_poly, y2)
    print("Polynomial Regression Dates-Deaths Score: " + str(pol_reg2.score(X_poly,y2)))
    print()
    
    #Plotting Linear Regression
    fig, ax = plt.subplots(figsize=(10,7.5))
    ax.plot_date(X, y, xdate=True,color='red')
    ax.plot_date(X, lin_reg.predict(X_new), 10, color='blue', label="New cases")
    ax.plot_date(X,y2,color='green')
    ax.plot_date(X,lin_reg2.predict(X_new), 10, color='black', label="Deaths")
    fig.autofmt_xdate()
    ax.set_xlim()
    ax.set_ylim(bottom=0)
    plt.xticks(np.arange(0, len(X), step=20))
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of People")
    plt.title("Daily cases and deaths using Linear Regression")
    ax.legend(loc="upper left")
    plt.show()
    
    
    #Plotting Polynomial Regression
    fig, ax = plt.subplots(figsize=(10,7.5))
    X_grid=np.arange(min(X_new),max(X_new),0.1)
    X_grid=X_grid.reshape((len(X_grid),1))
    ax.plot_date(X,y,color='red')
    ax.plot_date(X, pol_reg.predict(X_poly), 10, color='blue', label="New cases")
    ax.plot_date(X, y2, color='green')
    ax.plot_date(X, pol_reg2.predict(X_poly), 10, color='black', label="Deaths")
    fig.autofmt_xdate()
    ax.set_xlim()
    ax.set_ylim(bottom=0)
    plt.xticks(np.arange(0, len(X), step=20))
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of People")
    plt.title("Daily cases and deaths using Polynomial Regression")
    ax.legend(loc="upper left")
    plt.show()
    
    
    #Predicting data Points
    while True:
        print("Please enter the date you would like to predict in the format DD/MM/YYYY")
        date1 = input()
        date1_datetime = dt.datetime.strptime(date1, '%d/%m/%Y')
        d = date1_datetime.toordinal()
        print("\nPredictions for " + country_code)
        print()
        print("Linear Regression model prediction for", date1 +": "+ str(round(lin_reg.predict([[d]])[0])) , "new cases,", str(round(lin_reg2.predict([[d]])[0])),"deaths.")
        print()
        print("Polynomial Regression model prediction for", date1 +": "+ str(round(pol_reg.predict(poly_reg.fit_transform([[d]]))[0])) , "new cases,", str(round(pol_reg2.predict(poly_reg.fit_transform([[d]]))[0])),"deaths.")
        
        answer = input("Enter 'exit' to exit, or enter anything else to predict again.").lower()
        
        if answer == "exit":
            break

    return("\ndone.")

if __name__ == "__main__":
    print(COVID_data_analyser(input("Please enter the ISO 3166 country code of the nation you wish to search for: ").upper()))