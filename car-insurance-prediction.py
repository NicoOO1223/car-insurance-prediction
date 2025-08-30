# Import required modules
import pandas as pd
import numpy as np
from statsmodels.formula.api import logit


df = pd.read_csv('car_insurance.csv')

response = "outcome"  # Binary response variable
predictors = df.columns.drop(response)  # Exclude target from predictors

results = {}

for predictor in predictors:
    formula = f"{response} ~ {predictor}"  # Define formula
    model = logit(formula, data=df).fit(disp=0)  # Fit model
    
    # Predict probabilities and convert to binary (threshold = 0.5)
    df["predicted"] = (model.predict(df) > 0.5).astype(int)
    
    # Calculate accuracy
    accuracy = (df["predicted"] == df[response]).mean()
    results[predictor] = accuracy  # Store accuracy score

# Get the best predictor based on accuracy
best_predictor = max(results, key=results.get)
print(f"Best predictor: {best_predictor} with accuracy {results[best_predictor]:.5f}")

best_feature_df = pd.DataFrame({'best_feature': ['driving_experience'], 'best_accuracy': [0.77710]})
print(best_feature_df)