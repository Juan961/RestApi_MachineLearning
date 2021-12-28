# REST API - Machine Learning 

### 📖 Description

REST API built with Flask that makes use of the sklearn library with which an artificial intelligence model is trained in order to define given some data if a person is prone to having heart disease.

### 📋 Dataset

The dataset was obtained from the kaggle platform, afterwards a cleaning was carried out to obtain the one in the data folder with the name "heart.csv" [Original dataset](https://www.kaggle.com/c/SAheart)

### 🔧 Tools
- Flask
- Sklearn

### 🚀 Start

Install dependencies

```console
foo@bar:~$ pip install -r requirements.txt
```

Train the model (To see the score of the model, uncomment the line 42 if the file api_train_model.py)

```console
foo@bar:~$ python api_train_model.py
```

Start the server

```console
foo@bar:~$ python main.py
```

### Routes

Endpoint: http://localhost:5000

- http://localhost:5000/predict

Method POST

#### Input

This route receives the following parameters through the body using json.

- age: Age in years of the patient
- sex: 1 - Man, 2 - Woman
- cp: Type of value in the chest among 4 possible values. (1 - Angina - typical, 2 - Atypical angina, 3 - Non-anginal pain, 4 - Asymptomatic pain)
- trestbps: Resting blood pressure
- chol: Cholesterol measurement
- fbs: Fasting blood sugar
- restcg: Electrocardiography results at rest
- thalach: Maximum heart rate reached
- exang: Did you develop angina after exercising?
- oldpeak: Exercise-Induced ST Depression Relative to Rest (More - information here. https://litfl.com/st-segment-ecg-library/)
- slope: Slope of the ST segment peak
- ca: Number of major blood vessels colored by fluoroscopy
- thal: Thalassemia: 1 - Normal, 2 - Fixed defect, 3 - Reversible defect


Example 
```json
{
    "age": 13,
    "sex": 1,
    "cp":  1,
    "trestbps": 140,
    "chol": 221,
    "fbs": 0,
    "restcg": 1,
    "thalach": 164,
    "exang": 1,
    "oldpeak": 0.0,
    "slope": 2,
    "ca": 0,
    "thal": 2
}
```

#### Output
The data of the input with a new key called target that is the value of the prediction.

target: Presence of cardiac pathology 1 or 0 (True or False).

Model score: 0.98
