import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
from statistics import mean, stdev

#List of Cross validation scores of tuned GradientBoosting regressor (not scaled):
cv_GBR_not_scalled = [14.93631343, 15.58386, 12.86628177, 36.06647914, 14.78576989,
  15.89662374, 14.90552378, 14.6379618, 11.00049996, 8.32913522]

#List of Cross validation scores of tuned GradientBoosting regressor (scaled):
cv_GBR_scalled = [17.33590152, 16.11795378, 11.36634574, 17.82568171, 13.80180982,
 14.96270583, 16.02632112, 16.46566786, 12.31262381, 7.3167631]

#List of Cross validation scores of tuned GradientBoosting regressor (scaled and MI):
cv_GBR_scalled_MI = [15.04557722, 15.71050756, 15.96516515, 17.53413451, 14.81243876,
 16.18152426, 13.16578652, 17.18676758, 10.82552675, 8.70888499]

#List of Cross validation scores of tuned SupportVector regressor (not scaled):
cv_SVR_not_scalled = [708.07419848, 452.89164681, 629.65957263, 129.4064383, 297.06637739,
 821.03365319, 405.02625248, 624.36893138, 449.43871697, 869.92839837]


def vis_cv():
    cv = input("Please input one of the lists above: ")
    if cv == "cv_GBR_not_scalled":
        cv = cv_GBR_not_scalled
        title = "Cross validation scores of tuned GradientBoosting Regressor (not scaled)"
    elif cv == "cv_GBR_scalled":
        cv = cv_GBR_scalled
        title = "Cross validation scores of tuned GradientBoosting Regressor (scaled)"
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