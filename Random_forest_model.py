import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier # Being used for classification
from sklearn.ensemble import RandomForestRegressor # Being used for regression
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
import numpy as np
import matplotlib.pyplot as plt

# Load OpenSNP into the Dataframe
#dataOpenSNP = pd.read_csv('OpenSNP.csv') blocked out until the data is available and file name can be entered

#Display the first few rows to inspect the data
##print(dataOpenSNP.head()) blocked out until the data is available and file name can be entered

# Function to load and preprocess the data set
def load_data(file_path, target_column):
    print("Loading dataset...")
    # Load the dataset (replace with your actual OpenSNP data file)
    data = pd.read_csv(file_path, low_memory=False)
    print("Dataset loaded successfully.")
    
    # Select the genotype columns (X) and phenotype column (Y)
    print(f"Selecting features and target columns...")
    X = data.drop(target_column, axis=1)  # Genotype data (features)
    Y = data[target_column]               # Phenotype data (target)
    print("Features and target columns selected.")

    # Handle missing values (e.g., drop rows with missing phenotype or genotype data)
    print("Handling missing values...")
    data = data.dropna()  # Alternatively, you can fill missing values if appropriate
    print(f"Missing values handled. Data shape: {data.shape}")

    return X, Y

# Function to train and evaluate the Random Forest model
def train_and_evaluate(X, Y, model_type = 'regressor'):
    print(f"Slitting data into training and testing sets...")
    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print(f"Data split was successful. Training set size: {X_train.shape[0]}, Testing set size: {X_test.shape[0]}")
    
    # Initialize the model (Classifier or Regressor)
    if model_type == 'classifier':
        print("Initializing Random Forest Classifier...")
        model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
        print("Random Forest Classifier initialized.")
    elif model_type == 'regressor':
        print("Initializing Random Forest Regressor...")
        model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
        print("Random Forest Regressor initialized.")
    else:
        raise ValueError("Model type must be either 'classifier' or 'regressor'")
    
    # Train the model
    print("Training the model...")
    model.fit(X_train, Y_train)
    print("Model training completed and successful.")
    
    # Make predictions
    print("Making predictions on the test set...")
    Y_pred = model.predict(X_test)
    print("Predictions made successfully.")
    
    # Evaluate the model
    if model_type == 'classifier':
        print("Evaluating classification performance...")
        accuracy = accuracy_score(Y_test, Y_pred)
        print(f"Accuracy: {accuracy}")
        print("Classification Report:")
        print(classification_report(Y_test, Y_pred))
    elif model_type == 'regressor':
        print("Evaluating regression performance...")
        mse = mean_squared_error(Y_test, Y_pred)
        print(f"Mean Squared Error: {mse}")
    
    # Feature imoortance (visualization)
    print("Calculating feature importance...")
    importance = model.feature_importances_

    # Sort the importance scores in descending order
    sorted_idx = np.argsort(importance)[::-1]
    
    # Get the top 10 features
    top_10_features = sorted_idx[:10]
    
    # Plotting feature importance
    plt.figure(figsize=(10, 6))
    plt.barh(top_10_features, importance[sorted_idx][:10], align='center')
    plt.xlabel('Feature Importance')
    plt.title('Top 10 SNP Features for {model_type.capitalize()} Prediction')
    plt.show()
    
    # Return the trained model and predictions
if __name__ == "__main__":
    # Load the data
    print("Starting the data loading and preprocessing...")
    file_path = r"G:/Shared drives/csds456/Project Midterm/combined_output.csv"  # Path to your CSV file
    target_column = 'phenotype_column'  # Adjust to your actual phenotype column name
    X, Y = load_data(file_path, 'phenotype_column')  # Pass the file path to the function

    # Train and evaluate the model
    print("\nStarting the model training and evaluation...")
    train_and_evaluate(X, Y, model_type='classifier')
        
    # Train and evaluate the model as a regressor
    print("\nNow training and evaluation as a regressor...")
    train_and_evaluate(X, Y, model_type='regressor')
        
        
    
    


