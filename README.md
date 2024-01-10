ABSTRACT:
The purpose of the python code that is being shown is to do an exploratory data analysis (EDA) on a dataset that includes salary. To provide some insight into the salary distribution, the code dose statistical analysis and create visual. The main features of the code are described in this report along with data loading, visualization, and the computation of the mean salary and a certain percentage value indicated as X.

INTRODUCTION :        
             The python script analyzes a dataset including annual salary information by utilizing a number of packages for data processing and visualization. This analysis includes calculating the average pay, figuring out 1.25 times the average salary, and figuring out what proportion of salary fall into this range.Data6 loads the dataset and uses the pandas library to generate a dataframe with a single column labeled salary to indicate yearly salary.

DISTRIBUTION :
                                       A probability density function (PDF) and histogram are used to illustrate the distribution using seaborn and matplotlib revealing information about the salary data central tendency and distribution.

MEAN VALUE :
                         The np.mean() method from the Numpy package is used to calculate the mean salary (W̃). To do this, add up all of the individual values, then divide the total by the number of observatio. The mean value for the dataset is 26847.65. The  value for (1.25W̃) is 33559.56.
                                               
                                                 W̃ = (∑_(i=1)^n▒█(salary@i))/n

PERCENTAGE VALUE X :
                                          Boolean indexing and NumPy operations are used to calculate the percentage value X, which represents the percentage of salary lying between the mean salary (W̃) and 1.25 times the mean salary (1.25W̃). The computed percentage value X for the dataset that is supplied is 49500.00%.
                      
                      X = (Number of salarie between W̃ and 1.25 W̃)/(Total Number of salarie)

CONCLUSION :
                          The average salary in the dataset are repreented by the mean salary, which acts as a central reference. The proportion os salary between W̃ and 1.25 W̃ analysis sheds light on how widely the distribution is distributed around the mean.
