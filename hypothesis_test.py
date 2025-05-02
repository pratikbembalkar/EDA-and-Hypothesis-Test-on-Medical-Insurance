import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats.weightstats import ztest
import statsmodels.api as sm
from statsmodels.formula.api import ols

def chi2_test(a, b, cols='', significance_level=0.05):
  """A function for the Chi-Square Test. It starts by generating the Pandas crosstable for the observed values. Then it applies the chi_contingency from the Scipy.stats module.

  Args:
      a (pandas.core.series.Series): First categorical variable
      b (pandas.core.series.Series): Second categorical variable
      cols (str): Variable names for print function. Must be string so it indicates default to ''.
      significance_level (float, optional): The alpha threshold value to keep or reject the null hypothesis. Defaults to 0.05.
  
  Returns:
      Prints all the outcomes regarding to the Chi-Square test.
  """
  cross_table=pd.crosstab(a, b)
  print(f'Cross Table:\n\n{cross_table}\n')
  observed_values=cross_table.values
    
  print(f'Chi Square test is stating..................\n\n')
  chi2_stat, p_value, dof, expected_values=stats.chi2_contingency(observed_values)

  print(f'Chi Square Statistics: {np.round(chi2_stat, 2)}, P-value: {np.round(p_value, 2)}, Degree of Freedom: {dof}\n')
  print(f'Observed Values:\n{observed_values}\n')

  if p_value <= significance_level: 
      print(f'Reject NULL HYPOTHESIS, the variables {cols} are not independent of each other') 
  else: 
      print(f'ACCEPT NULL HYPOTHESIS, the variables {cols} are independent of each other') 
    
  print(f'\nExpected Values: \n{np.round(expected_values, 0)}\n')
    
  print(f'Stopped the test')

def one_sample_ttest(dataset, target_col, sample_col=None, group=None, new_samples=None, significance_level=0.05, categorical=False):
  """The function is for one sample T-test. It has two parts: one for categorical samples and another for continuous samples. If categorical == true, it compares the target variable's average for a specific category or group to the population average. Otherwise, for continuous data, it compares the new sample average with the old or entire population average.

  Args:
      dataset (pandas.core.frame.DataFrame): The entire dataset.
      target_col (str): target variable for the average.
      sample_col (str, optional): categorical column name. Defaults to None.
      group (str, optional): specific group or category. Defaults to None.
      new_samples (list of values, optional): new data. Defaults to None.
      significance_level (float, optional): The alpha threshold value to keep or reject the null hypothesis. Defaults to 0.05.
      categorical (bool, optional): True or False to perform the test on the either any specific group or the new data. Defaults to False.
  
  Returns:
      Prints all the results regarding to the one sample T-test.
  """
  if categorical == True:
      samples=dataset[dataset[sample_col] == group][target_col]
      print(f'{sample_col}({group}) Avg {target_col}: {np.round(samples.mean(), 2)}\n')
      print(f'Populations Avg {target_col}: {np.round(dataset[target_col].mean(), 2)}\n')
      print(f'Difference of {target_col}: {np.round(np.abs(np.round(samples.mean(), 2) - np.round(dataset[target_col].mean(), 2)), 2)}\n')
      t_stats, p_value=stats.ttest_1samp(a=samples, popmean=dataset[target_col].mean())
  else:
      samples_mean=dataset[target_col].mean()
      print(f'New Populations Avg {target_col}: {np.round(new_samples.mean(), 2)}\n')
      print(f'Populations Avg {target_col}: {np.round(samples_mean, 2)}\n')
      print(f'Difference of {target_col}: {np.round(np.abs(np.round(samples_mean, 2) - np.round(new_samples.mean(), 2)), 2)}\n')
      t_stats, p_value=stats.ttest_1samp(a=new_samples, popmean=samples_mean)

  print(f'T Statistics: {np.round(t_stats, 2)}, P-value: {np.round(p_value, 2)}\n')

  if p_value <= significance_level: 
      print(f'Reject NULL HYPOTHESIS, the samples are not independent to each other') 
  else: 
      print(f'ACCEPT NULL HYPOTHESIS, the samples are independent to each other') 

def two_sample_ttest(dataset, sample_col=None, group1=None, group2=None, target_col=None, significance_level=0.05):
    """The function is for two sample T-test. It compares the means of two independent groups in order to determine whether there is statistical evidence that the associated population means are significantly different.

    Args:
        dataset (pandas.core.frame.DataFrame): the entire dataset.
        sample_col (str): column name of the groups.. Defaults to None.
        group1 (str): first group name. Defaults to None.
        group2 (str): second group name. Defaults to None.
        target_col (str): target variable for the average. Defaults to None.
        significance_level (float, optional): The alpha threshold value to keep or reject the null hypothesis. Defaults to 0.05.
    
    Returns:
        Prints all the results regarding to the one sample T-test.
    """
    sample_group1=dataset[dataset[sample_col] == group1][target_col]
    sample_group2=dataset[dataset[sample_col] == group2][target_col]
    print(f'{sample_col}({group1}) Avg {target_col}: {np.round(sample_group1.mean(), 2)}\n')
    print(f'{sample_col}({group2}) Avg {target_col}: {np.round(sample_group2.mean(), 2)}\n')
    print(f'Difference of {target_col}: {np.round(np.abs(np.round(sample_group1.mean(), 2) - np.round(sample_group2.mean(), 2)), 2)}\n')
    
    
    t_stats, p_value=stats.ttest_ind(a=sample_group1, b=sample_group2, equal_var=False)

    print(f'T Statistics: {np.round(t_stats, 2)}, P-value: {np.round(p_value, 2)}\n')

    if p_value <= significance_level: 
        print(f'Reject NULL HYPOTHESIS, the mean {target_col} of {sample_col}({group1}) and the mean {target_col} of {sample_col}({group2}) are not independent of each other') 
    else: 
        print(f'ACCEPT NULL HYPOTHESIS, the mean {target_col} of {sample_col}({group1}) and the mean {target_col} of {sample_col}({group2}) are independent of each other') 

def paired_ttest(dataset, sample_col=None, group1=None, group2=None, target_col=None, significance_level=0.05, n_samples=500):
    """The function is for Paired T-test. When we are interested in the difference between two variables for the same subject, we use a paired t-test.

    Args:
        dataset (pandas.core.frame.DataFrame): the entire dataset.
        sample_col (str): column name of the groups.. Defaults to None.
        group1 (str): first group name. Defaults to None.
        group2 (str): second group name. Defaults to None.
        target_col (str): target variable for the average. Defaults to None.
        significance_level (float, optional): The alpha threshold value to keep or reject the null hypothesis. Defaults to 0.05.
        n_samples (int, optional): the number of the samples to be tested. Defaults to 500.
    
    Returns:
        Prints all the results regarding to the paired T-test.
    """
    sample_group1=dataset[dataset[sample_col] == group1][target_col].sample(n=n_samples)
    sample_group2=dataset[dataset[sample_col] == group2][target_col].sample(n=n_samples)
    print(f'{sample_col}({group1}) Avg {target_col}: {np.round(sample_group1.mean(), 2)}\n')
    print(f'{sample_col}({group2}) Avg {target_col}: {np.round(sample_group2.mean(), 2)}\n')
    print(f'Difference of {target_col}: {np.round(np.abs(np.round(sample_group1.mean(), 2) - np.round(sample_group2.mean(), 2)), 2)}\n')
    
    t_stats, p_value=stats.ttest_rel(a=sample_group1, b=sample_group2)

    print(f'T Statistics: {np.round(t_stats, 2)}, P-value: {np.round(p_value, 2)}\n')

    if p_value <= significance_level: 
        print(f'Reject NULL HYPOTHESIS, the mean {target_col} of {sample_col}({group1}) and the mean {target_col} of {sample_col}({group2}) are not independent of each other') 
    else: 
        print(f'ACCEPT NULL HYPOTHESIS, the mean {target_col} of {sample_col}({group1}) and the mean {target_col} of {sample_col}({group2}) are independent of each other') 

def one_smaple_ztest(new_samples, original_data, target_measurement, significance_level=0.05):
    """The function is for One Sample Z-test. When we are interested in the difference between any specific sample and the entire population, we use one sample z-test.

    Args:
        new_samples (numpy.ndarray): a numpy list of new data. (must be normal)
        original_data (numpy.ndarray): a numpy list of original data. (must be normal)
        target_measurement (str): name of the new and the old samples.
        significance_level (float, optional): The alpha threshold value to keep or reject the null hypothesis. Defaults to 0.05.
    
    Returns:
        Prints all the results regarding to the one sample Z-test.
    """
    original_mean=original_data.mean()
    new_samples_mean=new_samples.mean()
    diff=original_mean-new_samples_mean
    print(f'{target_measurement} on Average are {np.round(original_mean, 2)} and {np.round(new_samples_mean, 2)}, repectively\n')
    print(f'Differences between them are: {np.round(np.abs(diff), 2)}\n')
    
    z_stats, p_value=ztest(new_samples, value=original_mean)
    print(f'T Statistics: {np.round(z_stats, 2)}, P-value: {np.round(p_value, 2)}\n')

    if p_value <= significance_level: 
        print(f'Reject NULL HYPOTHESIS, the mean of {target_measurement} are not independent of each other') 
    else: 
        print(f'ACCEPT NULL HYPOTHESIS, the mean of {target_measurement} are independent of each other') 

def two_smaple_ztest(group1, group2, target_measurement, significance_level=0.05):
    """The function is for Two Sample Z-test. When we are interested in the difference between two specific group of samples, we use two sample z-test.

    Args:
        group1 (numpy.ndarray): a numpy list of first group (must be normal).
        group2 (numpy.ndarray): a numpy list of second group (must be normal).
        target_measurement (str): name of the first and the second group samples.
        significance_level (float, optional): The alpha threshold value to keep or reject the null hypothesis. Defaults to 0.05.
    """
    sample1_mean=group1.mean()
    sample2_mean=group2.mean()
    diff=sample1_mean-sample2_mean
    print(f'{target_measurement} on Average are {np.round(sample1_mean, 2)} and {np.round(sample2_mean, 2)}, repectively\n')
    print(f'Differences between them are: {np.round(np.abs(diff), 2)}\n')
    
    z_stats, p_value=ztest(group1, group2, value=0)
    print(f'T Statistics: {np.round(z_stats, 2)}, P-value: {np.round(p_value, 2)}\n')

    if p_value <= significance_level: 
        print(f'Reject NULL HYPOTHESIS, the mean of {target_measurement} are not independent of each other') 
    else: 
        print(f'ACCEPT NULL HYPOTHESIS, the mean of {target_measurement} are independent of each other') 

def anova_test(dataset, independent_variable, outcome_variable, independent_variable_=None, two_way=False):
    """The function is for ANOVA Test. When we are interested in the difference between two or more group of samples, we use it. If two_war==True, there are two independent varibales with the target. Otherwise one independent variable is used.

    Args:
        dataset (pandas.core.frame.DataFrame): the entire dataset.
        independent_variable (str): independent variable name.
        outcome_variable (str): target variable name.
        independent_variable_ (str, optional): second independent variable name. Defaults to None.
        two_way (bool, optional): True or False to check whether the test is two way or not. Defaults to False.

    Returns:
        pandas.core.frame.DataFrame: the anova table.
    """
    if two_way == True:
        model=ols(f'{outcome_variable} ~ C({independent_variable})*C({independent_variable_})', data=dataset).fit()
        print(f'ANOVA-TABLE for ({independent_variable}, {independent_variable_}) and {outcome_variable}:')
    else:
        model=ols(f'{outcome_variable} ~ C({independent_variable})', data=dataset).fit()
        print(f'ANOVA-TABLE for {independent_variable} and {outcome_variable}:')
    
    anov_table=sm.stats.anova_lm(model, typ=2)
    return anov_table