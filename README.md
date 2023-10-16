# **FastAPI Application CICD with Chatgpt API and Cocktail API**

This repository contains a FastAPI application that integrates the Chatgpt API and Cocktail API. It also includes GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD) using pytest for testing.

- **main.py: This file contains the code to build a FastAPI application. 
- **test_main.py: This file is dedicated to unit tests for your FastAPI application. It uses the pytest framework to run tests and ensure that the application functions as expected.
- **requirements.txt: This file lists the necessary Python dependencies and their specific versions required to run the FastAPI application and its associated tests.
- **.github/workflows/main.yml: This file represents the GitHub Actions workflow file. It defines the CI/CD pipeline for your FastAPI application, specifying the steps to be executed when certain events occur, such as pushing changes to the main branch.


## **Setup and Installation**

### **Prerequisites**

- Python 3.7 or higher
- pip package manager

### **Installation**

1. Clone the repository:
    
    ```bash
    git clone git@github.com:chihhua28/test_fast_api_cicd.git
    ```
    
2. Navigate to the project directory:
    
    ```bash
    cd <your-project-directory>
    ```
    
3. Install the required dependencies:
    
    ```bash
    pip3 install -r requirements.txt
    ```
    

### **Configuration**

1. Obtain the required API keys:
    - Chatgpt API key
2. Add these API keys to your GitHub repository secrets with the names **`CHATGPT_API_KEY`.**

## **Usage**

1. Run the FastAPI application:
    
    ```bash
    python3 -m uvicorn main:app --reload
    ```
    
2. Access the FastAPI application in your browser at **`http://127.0.0.1:8000`**.
3. Test the application endpoints using the provided documentation and sample API requests.

## **GitHub Actions**

The repository is configured with GitHub Actions to perform Continuous Integration and Continuous Deployment.

Once you push your changes to the main branch, the GitHub Actions workflow is triggered automatically. This workflow includes the following steps:

- **Checkout repository**: This step checks out the repository code.
- **Set up Python**: This step sets up the Python environment for the workflow.
- **Install dependencies**: This step installs the project dependencies, including flake8, pytest, and httpx.
- **Static Code Linting with flake8**: This step ensures that the code follows the specified linting criteria and checks for any potential issues.
- **Unit Testing with pytest**: This step runs pytest to perform automated tests on the FastAPI application, including the integration with the Chatgpt API and Cocktail API.

## **Tests**

The repository includes automated tests written using pytest. These tests cover the functionality of the FastAPI application, including the integration with the Chatgpt API and Cocktail API.

## **Contributing**

FastAPI tutorial: [Datacamp](https://www.datacamp.com/tutorial/introduction-fastapi-tutorial)

Where I found the Cocktail API: [Public APIs](https://github.com/public-apis/public-apis#food--drink)

CICD with Git action: [Continuous Integration on Github with FastAPI and pytest](https://retz.dev/blog/continuous-integration-github-fastapi-and-pytest)

## **License**

[MIT](https://choosealicense.com/licenses/mit/)
