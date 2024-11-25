import requests
 
url = 'http://localhost:9696/predict'
 
patient_id = 'Jane Doe'
patient = {
    "Age": 65,
    "Race": "White",
    "Marital Status": "Married",
    "T Stage": "T1",
    "N Stage": "N1",
    "6th Stage": "IIA",
    "differentiate": "Poorly differentiated",
    "Grade": "3	",
    "A Stage": "Regional",
    "Tumor Size": 4,
    "Estrogen Status": "Positive",
    "Progesterone Status": "Positive",
    "Regional Node Examined	": 24,
    "Reginol Node Positive	": 1,
    "Survival Months": 60
}
 
response = requests.post(url, json=patient).json()
print(response)
 
if response['alive'] == True:
    print('Patient with following name is ALIVE: %s' % patient_id)
else:
    print('Patient with follwong name is DEAD: %s' % patient_id)
