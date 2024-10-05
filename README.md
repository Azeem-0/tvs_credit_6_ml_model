# AI/ML-Powered Loan Suggester Backend

## Project Overview

This backend repository powers the AI/ML loan suggester that enhances the existing EMI calculator on the frontend. It provides personalized loan recommendations based on the user’s financial data and loan options. The backend is built using Flask and integrates machine learning algorithms to analyze different loan options and calculate suggestion scores, indicating the user's likelihood of successfully managing the EMI.

### Problem Statement

Users currently do not receive personalized loan suggestions from the basic EMI calculator. This backend addresses this limitation by analyzing financial inputs and offering more tailored loan recommendations. These suggestions help users choose optimal loan plans, reducing the risk of financial strain.

### Solution

The AI/ML loan suggester model provides:

- Personalized loan recommendations based on the user's financial data (income, savings, debts).
- Suggestion scores for various loan combinations, showing the likelihood of successful loan repayment.
- Logistic regression to predict the chances of managing EMIs successfully based on historical data.

## Technologies Used

- **Backend Framework**: Flask (Python)
- **Machine Learning**: Logistic Regression for loan suggestion scoring
  
## Installation

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/loan-suggester-backend.git
   cd loan-suggester-backend ```
  ```FLASK_APP=app.py
  FLASK_ENV=development```
```flask run
```

##The API will be available at http://localhost:5000
