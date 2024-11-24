import pickle
from sklearn.preprocessing import LabelEncoder

fields = [
    "DevOps", 
    "Data Analysis", 
    "Front-End Development", 
    "UI/UX Design", 
    "Embedded Systems", 
    "Game Development", 
    "Back-End Development", 
    "AI and Machine Learning", 
    "Cybersecurity"
]

label_encoder = LabelEncoder()
label_encoder.fit(fields)

with open("label_encoder.pkl", "wb") as file:
    pickle.dump(label_encoder, file)
