import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score



df = pd.read_csv('male-elephant-tusk-size.csv')
df

##########################################################################################################
#فصل الداتا فريم حسب التاريخ
pre_poaching = df.query('period == "1966-68"')
pre_poaching.head

post_recovery = df.query('period == "2005-13"')
post_recovery.head(3)

#######################################################################################################
# Calculate the tusk length average (mean) for each Split Data Frame :-

pre_poaching_average = pre_poaching['tusk_length'].mean().round(2)
print(pre_poaching_average)

post_recovery_average = post_recovery['tusk_length'].mean().round(2)
print(post_recovery_average)

print("Before :", pre_poaching['tusk_length'].mean())

print("After:", post_recovery['tusk_length'].mean())

# def calculate_tusk_metrics(pre_poaching, post_recovery):
#     before_avg = pre_poaching['tusk_length'].mean()
#     after_avg = post_recovery['tusk_length'].mean()

#     return {
#         "before": round(before_avg, 2),
#         "after": round(after_avg, 2),
#         "delta": round(after_avg - before_avg, 2)
#     }

# print(calculate_tusk_metrics(pre_poaching, post_recovery))

# Before : 67.44088785046729
# After: 57.968809411764695
#نجد ان طول الانياب يقل في فترة مابعد الصيد الجائر عند مقارنة طول الانياب بالفترة الزمنية.
##########################################################################################################

# we will now compre the tusk length with the shoulder hight
# to see if there is any effect for the elephant age on the tusk length 
#Visualization :-
# Scatter plot :-


plt.scatter(pre_poaching['shoulder_height'], pre_poaching['tusk_length'], marker= '^')
plt.scatter(post_recovery['shoulder_height'] , post_recovery['tusk_length'], marker= 's')
plt.xlabel('Shoulder Height (cm)')
plt.ylabel('Tusk Length (cm)')

plt.text(x=200, y=120, s='Pre_poaching', color='C0')
plt.text(x=220, y=35, s='Post_recovery', color='C1')




##########################################################################################################

# Create the regression code for the Modeling :

class LinearModel:
    def __init__(self, model_name=""):
        self.model_name = model_name
        
    def fit(self, x, y):
        x = pd.DataFrame(x)
        linear_model = LinearRegression().fit(x, y)
        y_pred = linear_model.predict(x)
        self.slope = linear_model.coef_[0]
        self.intercept = linear_model.intercept_
        self.rsquared = r2_score(y, y_pred)
        
    def predict(self, x):
        return self.slope * x + self.intercept

    def plot_model(self, x_min, x_max, color="black"):
        y_min = self.predict(x_min)
        y_max = self.predict(x_max)
        plt.plot([x_min, x_max], [y_min, y_max], color=color)
        
    def print_model_info(self):
        m = self.slope
        b = self.intercept
        rsquared = self.rsquared
        model_name = self.model_name
        print(f'LinearModel({model_name}):')
        print(f'Parameters: slope = {m:.2f}, intercept = {b:.2f}')
        print(f'Equation: y = {m:.2f}x + {b:.2f}')
        print(f'Goodness of Fit (R²): {rsquared:.3f}')
        
##############################################################################################
# Modeling for the (Pre_Poaching):-     
pre_model = LinearModel("pre_poaching")
pre_model.fit(x=pre_poaching['shoulder_height'], y=pre_poaching['tusk_length'])

# Modeling for the (post_recovery):- 
post_model = LinearModel("post_recovery")
post_model.fit(x=post_recovery['shoulder_height'], y=post_recovery['tusk_length'])

###########################################################################################3
pre_model.plot_model(140, 250, 'C0')
post_model.plot_model(140, 250, 'C1')


pre_model.print_model_info()

# LinearModel(pre_poaching):
# Parameters: slope = 0.83, intercept = -91.14
# Equation: y = 0.83x + -91.14
# Goodness of Fit (R²): 0.831

#####################################################################################3

post_model.print_model_info()

# LinearModel(post_recovery):
# Parameters: slope = 0.40, intercept = -22.02
# Equation: y = 0.40x + -22.02
# Goodness of Fit (R²): 0.431

#######################################################################################
# نجد ان الانحدار في فترة ماقبل الصيد يساوي 0.83 بينما في فترة مابعد الصيد تناقصت قيمته حيث بلغت 0.40 مما يؤكد ان طول الانياب قد قل للاجيال القادمة .



##############################################################################################################
# Dashboard :-












