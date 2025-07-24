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

# Function to load and preprocess the dataset in chunks
def load_data(file_path, target_column, chunk_size=100000):
    print("Loading dataset in chunks...")
    chunk_iter = pd.read_csv(file_path, low_memory=False, chunksize=chunk_size)  # Read in chunks
    data_list = []
    
    # Iterate through each chunk
    for chunk in chunk_iter:
        print(f"Processing chunk with shape: {chunk.shape}")
        
        # Select the genotype columns (X) and phenotype column (Y)
        X_chunk = chunk.drop(target_column, axis=1)  # Genotype data (features)
        Y_chunk = chunk[target_column]               # Phenotype data (target)
        
        # Append the chunk data to the list
        data_list.append((X_chunk, Y_chunk))
        
    # Concatenate all chunks into a final DataFrame
    X_final = pd.concat([x for x, _ in data_list], axis=0)
    Y_final = pd.concat([y for _, y in data_list], axis=0)
    
    print(f"Final data shape: X={X_final.shape}, Y={Y_final.shape}")
    return X_final, Y_final

# Function to train and evaluate the Random Forest model
def train_and_evaluate(X, Y, model_type='regressor'):
    print(f"Splitting data into training and testing sets...")
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
    file_path = r"G:/Shared drives/csds456/Project Midterm/combined_output.csv"  
    target_column = 'phenotype_column'  
    X, Y = load_data(file_path, 'phenotype_column')  

    # Train and evaluate the model
    print("\nStarting the model training and evaluation...")
    train_and_evaluate(X, Y, model_type='classifier')
        
    # Train and evaluate the model as a regressor
    print("\nNow training and evaluation as a regressor...")
    train_and_evaluate(X, Y, model_type='regressor')
        
        
    
    


