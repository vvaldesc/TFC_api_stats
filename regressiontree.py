from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import json
from regression_model_test import RMT_testing
from joblib import dump, load

def regressiontree(historical, request, test = False, loadTrained = False):
    # Prepare the request data
    request_data = pd.DataFrame([request]).drop(["created_at", "id", "updated_at"], axis=1)  # Adjust based on actual columns
    request_data = request_data.reset_index(drop=True)
    
    if loadTrained:
        print("Loading trained model...")
        model = load('model.joblib')
    
    else:
        historical["result"]["data"].pop()
        
        # Convert historical data into a DataFrame
        historical_data = pd.DataFrame(historical["result"]["data"])
        
        # # Handle NaN values
        historical_data = historical_data.dropna(subset=["delay"])
        
        # Separate features (X) and target variable (y)
        X = historical_data.drop(["delay", "created_at", "updated_at"], axis=1)  # Exclude non-numeric and target columns
        y = historical_data["delay"]

        # Split data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Define preprocessing for numeric and categorical variables
        numeric_features = ['price','employee_salary','rating']  # Adjust based on actual numeric features
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),  # Replace nulls with mean
            ('scaler', StandardScaler())
        ])

        categorical_features = ['service_id','client_id','teacher_id','weather']  # Adjust based on actual categorical features
        categorical_transformer = Pipeline(steps=[
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])
            
        print("Training model...")
        # Create the model pipeline
        model = Pipeline(steps=[('preprocessor', preprocessor),
                                ('regressor', RandomForestRegressor())])
        # Train the model
        model.fit(X_train, y_train)
        dump(model, 'modeltest.joblib')
        
        # Check if necessary columns are missing and add them if they are
        necessary_columns = ['price','employee_salary','rating', 'service_id','client_id','teacher_id','weather']
        for column in necessary_columns:
            if column not in request_data.columns:
                request_data[column] = 0  # or some other default value

        # Handle null values in the request
        for column in request_data.columns:
            if pd.isnull(request_data[column]).any():
                if column in numeric_features:
                    request_data[column].fillna(request_data[column].mean(), inplace=True)
                else:
                    mode = request_data[column].mode()
                    if not mode.empty:
                        request_data[column].fillna(mode[0], inplace=True)
                    else:
                        request_data[column].fillna("Unknown", inplace=True)  # or some other default value

    # Make the prediction
    prediction = model.predict(request_data)
    
    if test:
        (mse, rmse, mae, r2) = RMT_testing(model, X_test, y_test)
        prediction_json = json.dumps({'estimated_delay': prediction[0], 'mse': mse, 'rmse': rmse, 'mae': mae, 'r2': r2})
    else:
        prediction_json = json.dumps({'estimated_delay': prediction[0]})

    # Convert the prediction to JSON and return
    return prediction_json