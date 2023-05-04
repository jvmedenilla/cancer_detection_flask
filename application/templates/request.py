import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'radius_mean':0.5, 'perimeter_mean': 0.5, 'area_mean':0.5, 'concavity_mean': 0.5,
                      'concave points_mean': 0.5, 'radius_worst': 0.5, 'perimeter_worst': 0.5,
                      'area_worst': 0.5, 'concave points_worst': 0.5})

print(r.json())