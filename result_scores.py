import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
from statistics import mean, stdev

#Cross validation RMSE for Linearregressor (prediction baseline):
cv_LR = [14.49867332, 23.21982682, 48.46220478, 60.72577752, 27.94318639,
 31.75786754, 23.30192079, 25.15959812, 54.13407105, 38.11686137]

#List of Cross validation scores of tuned GradientBoosting regressor (not scaled):
cv_GBR_not_scalled = 

#List of Cross validation scores of tuned GradientBoosting regressor (scaled):
cv_GBR_scalled = 

#List of Cross validation scores of tuned GradientBoosting regressor (scaled and MI):
cv_GBR_scalled_MI = 

#List of Cross validation scores of tuned SupportVector regressor (scaled and MI):
cv_SVR_scalled_MI = 


def vis_cv():
    cv = input("Please input one of the lists above: ")
    if cv == "cv_LR":
        cv = cv_LR
        title = "Cross validation scores of LinearRegression (baseline)"    
    elif cv == "cv_GBR_not_scalled":
        cv = cv_GBR_not_scalled
        title = "Cross validation scores of tuned GradientBoosting Regressor (not scaled)"
    elif cv == "cv_GBR_scalled":
        cv = cv_GBR_scalled
        title = "Cross validation scores of tuned GradientBoosting Regressor (scaled)"
    elif cv == "cv_GBR_scalled_MI":
        cv = cv_GBR_scalled_MI
        title = "Cross validation scores of tuned GradientBoosting Regressor (scaled and MI)"        
    elif cv == "cv_SVR_not_scalled":
        cv = cv_SVR_not_scalled
        title = "Cross validation scores of tuned SupportVector Regressor (not scaled)"
    mean_cv = round(mean(cv), 2)
    std_cv = round(stdev(cv), 2)       
    width = 12
    height = 6
    sns.set(rc = {'figure.figsize':(width,height)})
    sns.barplot(data=cv, color="#099c94").set(title=f'Cross validation scores of {title}')
    sns.set_style("dark")
    plt.xlabel(f'Mean value = {mean_cv}, Standard deviation = {std_cv}')
    plt.show()
vis_cv()