import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
from statistics import mean, stdev

#Cross validation RMSE for Linearregressor (prediction baseline):
cv_LR = [15.59187618, 18.53187914, 52.52091377, 26.68018309, 61.00628908,
 31.79323703, 49.28887858, 29.8147338, 16.29556922, 47.59093272]

#List of Cross validation scores of tuned GradientBoosting regressor (not scaled):
cv_GBR_not_scalled = [3.20111253, 9.04694478, 64.95582918, 30.08941435, 19.72279766,
 5.9280257, 19.90068852, 18.79080056, 5.52764909, 25.13186414]

#List of Cross validation scores of tuned GradientBoosting regressor (scaled):
cv_GBR_scalled = [4.09880926, 9.09157106, 64.95582918, 29.25922911, 20.00311377,
 6.00418416, 19.75807195, 18.96425584, 5.25329321, 23.57358236]

#List of Cross validation scores of tuned GradientBoosting regressor (scaled and MI):
cv_GBR_scalled_MI = [4.39984906, 8.95440849, 64.11675349, 24.33917009, 19.89371917,
 5.84562469, 19.97395398, 18.39476161, 5.17053847, 26.93956755]

#List of Cross validation scores of tuned SupportVector regressor (not scaled):
cv_SVR_not_scalled = [8.04922566, 37.35343258, 143.9929129, 43.69190337, 78.81934242, 
 31.59258209, 76.7425962, 65.82555325, 49.412206, 102.18485726]

#List of Cross validation scores of tuned SupportVector regressor (scaled):
cv_SVR_scalled = [60.02976787, 18.71548023, 100.07843786, 20.17727846, 49.72417145, 
 33.13548564, 335.7392413, 225.81269547, 34.89723575, 295.97521457]

#List of Cross validation scores of tuned SupportVector regressor (scaled and MI):
cv_SVR_scalled_MI = [69.9465295, 17.67691193, 115.32946474, 21.44037226, 52.40346051,
 33.73679494, 303.6293414, 215.87229828, 41.78009534, 285.14716552]

#List of Cross validation scores of of bagging strategy with kNN regressor (not scaled):
cv_BkNN_not_scalled = [69.17924392, 67.58730978, 214.35967085, 119.46703081, 174.07680393,
 148.49781384, 192.7084899, 137.30461242, 136.51373536, 257.04044932]

#List of Cross validation scores of of bagging strategy with kNN regressor (scaled):
cv_BkNN_scalled = [24.10735299, 12.39279059, 143.42323371, 54.55992453, 62.29332477,
  20.73492281, 86.60527133, 84.54023224, 25.24211369, 77.81768931]

#List of Cross validation scores of of bagging strategy with kNN regressor (not scaled):
cv_BkNN_scalled_MI = [88.36547161, 109.06222248, 175.62563888, 107.46137879, 99.01319755,
 111.74837605, 158.26231898, 113.94565713, 121.08036761, 169.11777268]

dict_of_results = {"cv_LR":[cv_LR, "Cross validation scores of LinearRegression (baseline)"], 
                   "cv_GBR_not_scalled":[cv_GBR_not_scalled, "Cross validation scores of tuned GradientBoosting Regressor (not scaled)"],
                    "cv_GBR_scalled":[cv_GBR_scalled, "Cross validation scores of tuned GradientBoosting Regressor (scaled)"],
                    "cv_GBR_scalled_MI":[cv_GBR_scalled_MI, "Cross validation scores of tuned GradientBoosting Regressor (scaled and MI)"],
                    "cv_SVR_not_scalled":[cv_SVR_not_scalled, "Cross validation scores of tuned SupportVector Regressor (not scaled)"],
                    "cv_SVR_scalled":[cv_SVR_scalled, "Cross validation scores of tuned SupportVector Regressor (scaled)"],
                    "cv_SVR_scalled_MI": [cv_SVR_scalled_MI, "Cross validation scores of tuned SupportVector Regressor (scaled and MI)" ],
                    "cv_BkNN_not_scalled":[cv_BkNN_not_scalled, "Cross validation scores of Bagging KNN (not scaled)"],
                    "cv_BkNN_scalled":[cv_BkNN_scalled, "Cross validation scores of Bagging KNN (scaled)"],
                    "cv_BkNN_scalled_MI":[cv_BkNN_not_scalled, "Cross validation scores of Bagging KNN (scaled and MI)"]}

def vis_cv():
    cv = input("Please input one of the lists above: ")
    for key, val in dict_of_results.items():
        if cv == key:
            cv = val[0]
            title = val[1]   
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