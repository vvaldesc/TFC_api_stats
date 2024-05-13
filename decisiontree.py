import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

import regression_model_test

def decisionTree(historical, request, test = False):
    # Convert historical data into a DataFrame
    historical_data = pd.DataFrame(historical["result"]["serviceConsumptions"])

    # Separate features (X) and target variable (y)
    X = historical_data.drop(["delay", "_id", "created_at", "updated_at"], axis=1)  # Exclude non-numeric and target columns
    y = historical_data["delay"]

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define preprocessing for numeric and categorical variables
    numeric_features = ['price']  # Adjust based on actual numeric features
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    categorical_features = ['service_id', 'employee_id', 'client_id']  # Adjust based on actual categorical features
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Create the model pipeline
    model = Pipeline(steps=[('preprocessor', preprocessor),
                            ('regressor', RandomForestRegressor())])

    # Train the model
    model.fit(X_train, y_train)

    # Prepare the request data
    request_data = pd.DataFrame([request]).drop(["_id", "created_at", "updated_at"], axis=1)  # Adjust based on actual columns

    # Make the prediction
    prediction = model.predict(request_data)
    
    if test:
        (mse, rmse, mae, r2) = regression_model_test.RMT_testing(model, X_test, y_test)
        prediction_json = json.dumps({'estimated_delay': prediction[0], 'mse': mse, 'rmse': rmse, 'mae': mae, 'r2': r2})
    else:
        prediction_json = json.dumps({'estimated_delay': prediction[0]})

    # Convert the prediction to JSON and return
    # prediction_json = json.dumps({'estimated_delay': prediction[0]})

    return prediction_json