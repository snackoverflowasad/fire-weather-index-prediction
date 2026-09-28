# Algerian Forest Fire Prediction

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Application-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit--learn](https://img.shields.io/badge/scikit--learn-Ridge%20Regression-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
![License](https://img.shields.io/badge/License-Not%20Specified-lightgrey)

A Flask-based machine learning application that predicts the **Fire Weather Index (FWI)** from environmental and fire-weather measurements associated with Algerian forest-fire data.

The application loads a trained Ridge Regression model and its corresponding feature scaler from the `models/` directory. Users enter the required measurements through a web form, and the application returns the predicted FWI value.

## Project Overview

The project includes the complete workflow used to prepare and serve the prediction model:

- Exploratory data analysis and feature engineering notebooks
- Original and cleaned Algerian forest-fire datasets
- A trained Ridge Regression model
- A persisted `StandardScaler` used during inference
- A Flask application for browser-based predictions
- HTML templates for the landing page and prediction form

## Key Features

- Browser-based Fire Weather Index prediction
- Ridge Regression inference using persisted model artifacts
- Consistent feature scaling during prediction
- Nine-input prediction form
- Responsive HTML interface for desktop and mobile screens
- Reproducible local setup using `requirements.txt`

## Technology Stack

| Area | Technology |
| --- | --- |
| Language | Python |
| Web framework | Flask |
| Data processing | Pandas, NumPy |
| Machine learning | scikit-learn |
| Model | Ridge Regression |
| Frontend | HTML and CSS with Jinja templates |
| Development environment | Jupyter notebooks |

## Repository Structure

```text
algerian-fire/
├── application.py                         # Flask application and prediction route
├── requirements.txt                        # Python dependencies
├── data/
│   ├── Algerian_forest_fires_dataset_UPDATE.csv
│   └── Algerian_forest_fires_dataset_cleaned.csv
├── models/
│   ├── ridge_model.pkl                    # Trained Ridge Regression model
│   └── scaler.pkl                         # Fitted StandardScaler
├── notebooks/
│   ├── eda-and-fe.ipynb                   # Exploratory analysis and feature engineering
│   └── model_training.ipynb                # Model training workflow
└── templates/
    ├── home.html                           # Prediction form and result view
    └── index.html                          # Application landing page
```

## Requirements

- Python 3.9 or newer
- pip
- A supported operating system such as Windows, macOS, or Linux

The application uses the following Python packages:

- Flask
- NumPy
- Pandas
- scikit-learn

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/snackoverflowasad/algerian-forest-fire-prediction.git
   cd algerian-forest-fire-prediction
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS or Linux**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Running the Application

Run the application from the project root so the relative paths to `models/ridge_model.pkl` and `models/scaler.pkl` resolve correctly:

```bash
python application.py
```

The development server listens on port `5000` and is configured to accept connections on all host interfaces. Open the following URL in a browser:

```text
http://localhost:5000
```

The application exposes these routes:

| Method | Route | Purpose |
| --- | --- | --- |
| `GET` | `/` | Displays the landing page |
| `GET` | `/predictdata` | Displays the prediction form |
| `POST` | `/predictdata` | Processes form values and returns the prediction |

## Prediction Inputs

The prediction form accepts the following numeric values in the same order expected by the scaler and model:

| Field | Description |
| --- | --- |
| `Temperature` | Ambient temperature in degrees Celsius |
| `RH` | Relative humidity percentage |
| `Ws` | Wind speed measurement |
| `Rain` | Rainfall measurement in millimeters |
| `FFMC` | Fine Fuel Moisture Code |
| `DMC` | Duff Moisture Code |
| `ISI` | Initial Spread Index |
| `Classes` | Encoded fire class value |
| `Region` | Encoded region value |

All values are submitted as numeric form fields. The application converts the submitted values to floating-point numbers before applying the saved scaler.

## Prediction Workflow

1. The user opens the prediction form at `/predictdata`.
2. The user enters the nine required environmental and fire-weather values.
3. Flask reads the submitted form data.
4. Pandas constructs a one-row input DataFrame with the expected feature names.
5. The persisted `StandardScaler` transforms the input data.
6. The persisted Ridge Regression model generates the FWI prediction.
7. The result is rendered in the prediction page to two decimal places.

## Model Development

The notebooks contain the analysis and training workflow used to prepare the model artifacts:

- `notebooks/eda-and-fe.ipynb` contains exploratory analysis and feature-engineering work.
- `notebooks/model_training.ipynb` contains the model training workflow.
- `data/Algerian_forest_fires_dataset_UPDATE.csv` contains the source dataset.
- `data/Algerian_forest_fires_dataset_cleaned.csv` contains the cleaned dataset used for model development.

The trained model and scaler are stored as pickle files under `models/` and are loaded when `application.py` starts.

## Configuration Notes

- The server runs with Flask debug mode enabled in the current development configuration.
- The application binds to `0.0.0.0` and uses port `5000`.
- The model and scaler are loaded at application startup.
- The application must be started from the repository root unless the model paths in `application.py` are changed.

For production deployment, disable debug mode and use a production WSGI server such as Gunicorn or Waitress.

## Limitations

- The application does not currently validate numeric ranges or provide custom form-error messages.
- The prediction endpoint returns an HTML page rather than a JSON API response.
- Model performance metrics are not exposed by the Flask application.
- The serialized model artifacts must be present locally before the application starts.
- Pickle files should only be loaded from trusted sources.

## Author

Developed by [Asad Hussain](https://asadhussain.in).

- GitHub: [snackoverflowasad](https://github.com/snackoverflowasad)
- Project repository: [algerian-forest-fire-prediction](https://github.com/snackoverflowasad/algerian-forest-fire-prediction)
