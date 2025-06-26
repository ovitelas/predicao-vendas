
# Sales Prediction with Linear Regression

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)
![Pandas](https://img.shields.io/badge/pandas-latest-blue.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-latest-orange.svg)

A data science project that demonstrates the use of a simple linear regression model to predict product sales based on advertising budget. This project showcases data handling, model training, evaluation, and visualization skills.

![Sales Prediction Plot](placeholder_for_plot_image.png)
*(You can replace the line above with a screenshot of the generated plot)*

---

## 📖 Table of Contents
- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

---

## 🎯 About the Project

The goal of this project is to build a simple linear regression model that predicts sales based on the money invested in TV advertising. It serves as a practical example of a complete, albeit basic, machine learning workflow.

Key features demonstrated:
- **Data Loading and Preparation:** Fetches a dataset from a URL and prepares it for modeling using Pandas.
- **Model Training:** Implements a linear regression model using Scikit-learn.
- **Model Evaluation:** Calculates the Root Mean Squared Error (RMSE) to evaluate the model's performance.
- **Data Visualization:** Creates a scatter plot with a regression line using Matplotlib to visualize the relationship between TV advertising and sales.

---

## 🛠️ Tech Stack

This project utilizes a range of standard data science libraries and tools:

- **Programming Language:**
  - `Python 3.13`
- **Libraries & Frameworks:**
  - `Scikit-learn`: For building the linear regression model and for model evaluation.
  - `Pandas`: For data manipulation and loading the dataset.
  - `Matplotlib`: For creating visualizations (scatter plot and regression line).
  - `NumPy`: For numerical operations, specifically for calculating the square root for RMSE.
  - `Requests`: For fetching the dataset from a URL.

---

## 📊 Dataset

The model is trained on the "Advertising" dataset, which contains data on the impact of different advertising channels on sales.

- **Source:** [An Introduction to Statistical Learning](https://www.statlearning.com/s/Advertising.csv)
- **Features Used:**
  - `TV`: Advertising budget for TV (in thousands of dollars).
- **Target Variable:**
  - `sales`: Product sales (in thousands of units).

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository:**
   
    git clone https://github.com/your-username/predicao-vendas.git
    cd predicao-vendas
    
    *(Replace `your-username` with your actual GitHub username)*

2.  **Create a virtual environment (recommended):**
    
    python -m venv venv
   

3.  **Install the required dependencies:**
    
    pip install -r requirements.txt
    

---

## Usage

To run the script, execute the following command in your terminal:


python sales_prediction.py


The script will:
1.  Download the `Advertising.csv` dataset.
2.  Train the linear regression model.
3.  Print the Root Mean Squared Error (RMSE) to the console.
4.  Display a plot visualizing the actual sales vs. the predicted sales.

---

## 📞 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/your-username/predicao-vendas](https://github.com/your-username/predicao-vendas)
