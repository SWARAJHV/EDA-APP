from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return "No file uploaded", 400

    # Read the CSV file
    df = pd.read_csv(file)
    
    # Perform EDA
    data_preview = df.head().to_dict()
    num_rows = df.shape[0]
    num_cols = df.shape[1]

    # Perform Machine Learning
    X = df.iloc[:, :-1]  # Features (all columns except the last one)
    y = df.iloc[:, -1]   # Target (last column)

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a model (Linear Regression as an example)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate error
    mse = mean_squared_error(y_test, predictions)

    # Return results
    return jsonify({
        "preview": data_preview,
        "num_rows": num_rows,
        "num_cols": num_cols,
        "mse": mse
    })

if __name__ == '__main__':
    app.run(debug=True)
