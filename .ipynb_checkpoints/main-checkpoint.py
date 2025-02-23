import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the train_dataset
file_path = 'train.csv'
train_data = pd.read_csv(file_path, index_col="Id")

# Columns to be deleted
columns_to_delete = ['MoSold', 'YrSold', 'SaleType', 'SaleCondition', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature']

# Delete the specified columns
train_data_cleaned = train_data.drop(columns=columns_to_delete, axis=1)

# Define the input features (X) and the output (y)
X = train_data_cleaned.drop('SalePrice', axis=1)
y = train_data_cleaned['SalePrice']

# Identify the categorical columns in X
categorical_columns = X.select_dtypes(include=['object']).columns

# Initialize a LabelEncoder for each categorical column
label_encoders = {column: LabelEncoder() for column in categorical_columns}

# Apply Label Encoding to each categorical column
for column in categorical_columns:
    X[column] = label_encoders[column].fit_transform(X[column])

# Display the first few rows of X to confirm the encoding
# print(X.head())

# ______________________________________________________________________________________

from sklearn.model_selection import train_test_split

# Split the first dataset (X, y) into train and test sets with a 70% - 30% split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.30, random_state=42)

# Fill NaN values in X_train and X_val with the median of the respective columns
X_train_filled = X_train.fillna(X_train.median())
X_val_filled = X_val.fillna(X_val.median())

(X_train.shape, X_val.shape, y_train.shape, y_val.shape)

# _________________________________________________________________________________

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt

# Create a Random Forest model
rf_model = RandomForestRegressor(random_state=42)

# Train the model on the training data
rf_model.fit(X_train_filled, y_train)

# Make predictions on the validation data
y_val_pred_filled = rf_model.predict(X_val_filled)

# Calculate the RMSE on the validation data
rmse_filled = sqrt(mean_squared_error(y_val, y_val_pred_filled))

# Print the RMSE
print(f'RMSE on the validation data: {rmse_filled}')

# __________________________________________________________________________

from sklearn.metrics import mean_absolute_percentage_error
from math import sqrt
import time


# Define the parameter ranges
n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
max_features_range = ['sqrt', 'log2', None]  # None means using all features
max_depth_range = [1, 2, 5, 10, 20, None]  # None means no limit


# Function to evaluate all parameter combinations
def evaluate_combinations(n_estimators_range, max_features_range, max_depth_range, X_train_filled, y_train, X_val_filled, y_val):
    best_rmse = float('inf')
    best_mape = float('inf')
    best_model = None
    best_parameters = {}

    for n_estimators in n_estimators_range:
        for max_features in max_features_range:
            for max_depth in max_depth_range:
                # Create and train the Random Forest model
                rf_model = RandomForestRegressor(
                    n_estimators=n_estimators,
                    max_features=max_features,
                    max_depth=max_depth,
                    random_state=42
                )
                rf_model.fit(X_train_filled, y_train)

                # Make predictions and compute RMSE
                y_val_pred = rf_model.predict(X_val_filled)
                rmse = sqrt(mean_squared_error(y_val, y_val_pred))
                mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100

                # Print parameters and metrics
                print(f"The parameters: {n_estimators}, {max_features}, {max_depth}. RMSE: {rmse}, MAPE: {mape}%")

                # Update the best model if this one is better
                if rmse < best_rmse:
                    best_rmse = rmse
                    best_mape = mape
                    best_model = rf_model
                    best_parameters = {
                        'n_estimators': n_estimators,
                        'max_features': max_features,
                        'max_depth': max_depth
                    }

    return best_rmse, best_mape, best_model, best_parameters

# ________________________________________________________________________________________

# Sequential Execution
start_time = time.time()

best_rmse_seq, best_mape_seq, best_model_seq, best_params_seq = evaluate_combinations(
    n_estimators_range,
    max_features_range,
    max_depth_range,
    X_train_filled,
    y_train,
    X_val_filled,
    y_val
)

end_time = time.time()
sequential_time = end_time - start_time

print(f"\nSequential Execution:")
print(f"Best Parameters: {best_params_seq}, RMSE: {best_rmse_seq}, MAPE: {best_mape_seq}%")
print(f"Execution Time: {sequential_time} seconds")

# _________________________________________________________________________________________

# Implementing Threads

import threading

# Thread-safe list to store results and lock for printing
lock = threading.Lock()
results_threading = []

# Thread function to evaluate combinations
def thread_worker(param_ranges):
    rmse, mape, model, params = evaluate_combinations(
        param_ranges[0], param_ranges[1], param_ranges[2],
        X_train_filled, y_train, X_val_filled, y_val
    )
    with lock:
        results_threading.append((rmse, mape, params))

# Split parameter ranges into chunks (e.g., by splitting `n_estimators_range`)
chunks = [n_estimators_range[:len(n_estimators_range)//2], n_estimators_range[len(n_estimators_range)//2:]]

threads = []
start_time = time.time()

for chunk in chunks:
    thread = threading.Thread(target=thread_worker, args=([chunk, max_features_range, max_depth_range],))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
threading_time = end_time - start_time

# Find the best result from all threads
best_threading_result = min(results_threading, key=lambda x: x[0])

print(f"\nThreading Execution:")
print(f"Best Parameters: {best_threading_result[2]}, RMSE: {best_threading_result[0]:.4f}, MAPE: {best_threading_result[1]:.2f}%")
print(f"Execution Time: {threading_time:.2f} seconds")

# _______________________________________________________________________________________

# Implementing Processes

from multiprocessing import Pool

# Multiprocessing worker function (evaluates a subset of parameter combinations)
def process_worker(param_ranges):
    return evaluate_combinations(
        param_ranges[0], param_ranges[1], param_ranges[2],
        X_train_filled, y_train, X_val_filled, y_val
    )

# Split parameter ranges into chunks (e.g., by splitting `n_estimators_range`)
chunks = [n_estimators_range[:len(n_estimators_range)//2], n_estimators_range[len(n_estimators_range)//2:]]

start_time = time.time()

with Pool() as pool:
    multiprocessing_results = pool.map(
        process_worker,
        [(chunk, max_features_range, max_depth_range) for chunk in chunks]
    )

end_time = time.time()
multiprocessing_time = end_time - start_time

# Find the best result from all processes
best_multiprocessing_result = min(multiprocessing_results, key=lambda x: x[0])

print(f"\nMultiprocessing Execution:")
print(f"Best Parameters: {best_multiprocessing_result[3]}, RMSE: {best_multiprocessing_result[0]:.4f}, MAPE: {best_multiprocessing_result[1]:.2f}%")
print(f"Execution Time: {multiprocessing_time:.2f} seconds")


