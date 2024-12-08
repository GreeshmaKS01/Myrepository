# pythoncodeforazure
# Python Flask App for Azure App Services

This repository contains a simple Python web application using Flask, intended to demonstrate how to deploy Python applications to **Azure App Services**.

## App Overview

This application runs a basic Flask web server and returns a "Hello, Azure!" message when accessed. It serves as a simple demonstration for teaching purposes.

### Code Structure

- `app.py` - The main Python file that runs the Flask web app.
- `requirements.txt` - Specifies the dependencies required to run the Flask application on Azure.

## How to Run Locally

If you want to run this application locally:

1. Make sure you have Python installed.
2. Install Flask by running:
    ```bash
    pip install Flask
    ```
3. Run the app:
    ```bash
    python app.py
    ```
4. Access the app in your browser at `http://localhost:8000`.

## Deployment to Azure App Services

This app is ready for deployment to **Azure App Services**. You can follow these steps to deploy:

1. Create an Azure App Service instance.
2. Link the App Service to this GitHub repository.
3. Azure will automatically deploy and run the Flask app based on the `app.py` and `requirements.txt` files.

### Output

Once deployed, you will see the message:
