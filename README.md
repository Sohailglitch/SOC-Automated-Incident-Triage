# SOC Automated Incident Triage

## Overview

SOC Automated Incident Triage is a machine learning-based security operations project that automates the assignment of security incidents to analysts.

The project processes Wazuh security alerts, extracts relevant features, generates labeled training data, trains a Random Forest classifier, and predicts which SOC analyst should handle new security incidents.

This project demonstrates practical applications of Machine Learning in Security Operations Centers (SOC).

---

## Features

- Parse Wazuh JSON alerts
- Extract alert features
- Generate labeled training datasets
- Train a Random Forest classification model
- Predict analyst assignment for new incidents
- Simple and modular workflow

---

## Project Workflow

```text
Wazuh JSON Alerts
        │
        ▼
Feature Extraction
        │
        ▼
Training Data Generation
        │
        ▼
Random Forest Model Training
        │
        ▼
Analyst Assignment Prediction
```

---

## Repository Structure

```
SOC-Automated-Incident-Triage/
│
├── data/
│   ├── sample_alerts.json
│   ├── output10.csv
│   ├── output11.csv
│
├── src/
│   ├── extract_features.py
│   ├── generate_training_labels.py
│   └── train_model.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Wazuh
- Machine Learning
- Random Forest Classifier

---

## Installation

Clone the repository.

```bash
git clone https://github.com/Sohailglitch/SOC-Automated-Incident-Triage.git
```

Install the required libraries.

```bash
pip install -r requirements.txt
```

---

## Usage

### Step 1

Extract features from Wazuh alerts.

```bash
python src/extract_features.py
```

### Step 2

Generate training labels.

```bash
python src/generate_training_labels.py
```

### Step 3

Train the machine learning model and predict analyst assignments.

```bash
python src/train_model.py
```

---

## Machine Learning Model

Algorithm:

- Random Forest Classifier

Input Features:

- Rule Description
- Alert Severity Level

Prediction:

- Assigned SOC Analyst

---

## Future Improvements

- Save trained models using Joblib
- Support additional machine learning algorithms
- Integrate with Wazuh API
- Integrate with TheHive
- Automate incident assignment using SOAR
- Real-time alert prediction

---

## License

This project is licensed under the MIT License.
