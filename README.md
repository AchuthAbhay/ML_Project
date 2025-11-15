# Student Exam Performance Indicator

A web-based application to predict a student's **Math score** based on their demographic data, parental education, lunch type, test preparation course, and other exam scores using machine learning regression models.

---

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

---

## Demo

The application is deployed on **AWS Elastic Beanstalk**:

[Student Performance Indicator Web App](http://StudentPerfromanceIndicator-env.eba-dnkmv3qm.ap-southeast-2.elasticbeanstalk.com)

---

## Features

- Predict **Math scores** using student demographic and academic data.
- Input fields include:
  - Gender
  - Race/Ethnicity
  - Parental Level of Education
  - Lunch Type
  - Test Preparation Course
  - Reading Score
  - Writing Score
- Machine learning model selects the **best-performing regressor** automatically.
- Interactive and responsive **HTML form** with gradient styling.
- Returns predicted math score instantly.

---

## Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, XGBoost, CatBoost
- **Frontend:** HTML, CSS
- **Deployment:** AWS Elastic Beanstalk

---

## Project Structure

```
StudentExamPerformance/
│
├── artifacts/              # Saved models and preprocessors
│   └── model.pkl
├── src/
│   ├── pipeline/           # ML pipeline
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── templates/              # HTML templates
│   ├── index.html
│   └── home.html
├── app.py                  # Flask app
├── requirements.txt
└── README.md
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/StudentExamPerformance.git
cd StudentExamPerformance
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Flask application:

```bash
python app.py
```

Open your browser and go to:
```
http://127.0.0.1:5000
```
Fill in the form with student data and click **Predict Math Score** to get predictions.

---

## Model Training

Multiple regression models are trained to predict math scores:
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

The pipeline automatically selects the best model based on **R² score**.

The trained model is saved as `artifacts/model.pkl`.

---

## Deployment

- Deployed using AWS Elastic Beanstalk.
- Environment: Python 3.13 running on 64-bit Amazon Linux.
- Accessible via the Elastic Beanstalk domain (see Demo section).

---

## Future Enhancements

- Add data visualization dashboards for analysis of student performance.
- Include confidence intervals for predictions.
- Enable batch predictions from CSV uploads.
- Add user authentication and store past predictions.

---

## Author

- **Your Name**  
- [Your GitHub](https://github.com/<your-username>)

---

Feel free to open issues or submit pull requests to contribute!
