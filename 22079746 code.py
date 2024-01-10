import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def data_6(csv_file):
    """
    Loading data from the CSV file 

    Parameters
    ----------
    csv_file : FILE PATH FOR THE CSV

    Returns
    -------
    data : DATAFRAME CONTAINING THE SALARY DATA

    """
    data = pd.read_csv(csv_file, header=None, names=['salary'])
    return data

file_path = 'data6.csv'
data = data_6(file_path)

def calculate_pdf(data):
    """
    probability density function and Histogram of salaries

    Parameters
    ----------
    data : DATAFRAME CONTAINING THE SALARY DATA

    Returns
    -------
    """
    sns.histplot(data['salary'], bins=35, edgecolor='black', alpha= 0.6, label='Histogram', kde=True, stat='density', element='step')
    sns.kdeplot(data['salary'], color='orange', label='KDE', linewidth=2)
    plt.title("probability density function and Histogram of salaries",fontsize=15)
    plt.xlabel("Yearly salary",fontsize=13)
    plt.ylabel("probability density function ",fontsize=13)
    plt.grid(axis='y', linestyle='--', alpha=0.6)

calculate_pdf(data)    

def calculate_mean(data):
    """
    In this we calculate the mean salary

    Parameters
    ----------
    data : DATAFRAME CONTAINING THE SALARY.

    Returns
    -------
    mean_salary : TYPE
        DESCRIPTION.

    """
    mean_salary = np.mean(data['salary'])
    mean_salary = round(mean_salary, 2)
    
    return mean_salary

mean_salary = calculate_mean(data)

def calculate_W_and_1_25W(data, mean_salary):
    """
    calculate the percentage between W̃ and 1.25W̃

    Parameters
    ----------
    data : DATAFRAME CONTAINING THE SALARY.
    mean_salary : MEAN SALARY

    Returns
    -------
    X_value :  percentage between W̃ and 1.25W̃

    """
    W̃ = mean_salary
    W̃_1_25 = 1.25 * W̃
    X_value = np.sum((data['salary'] >=W̃) & (data['salary'] <= W̃_1_25)).astype(int).mean()
    X_value = round(X_value, 2)
    
    return X_value
X_value = calculate_W_and_1_25W(data, mean_salary)
#Rounding the mean_salary and X_value
mean_salary_round = np.round(mean_salary, decimals=2)
X_value_round = np.round(X_value, decimals=2)
#plotting the three vertical lines 
plt.axvline(mean_salary_round, linestyle='dashed', color='r', linewidth=2, label=f'Average salary (W̃) = {mean_salary:.2f}')
plt.axvline(mean_salary_round * 1.25, linestyle='dashed', color='b', linewidth=2, label=f'1.25W̃ = {mean_salary * 1.25:.2f}')
plt.axvline(X_value_round, linestyle='dashed', color='g', linewidth=2, label=f'X: {X_value:.2%}')
#legend and saved the plot in '22079746.png', dpi=300
plt.legend(fontsize=11,loc='upper right')
plt.savefig('22079746.png', dpi=300)
plt.show()
