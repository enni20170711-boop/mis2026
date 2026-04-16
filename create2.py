import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "name": "呂恩妮",
  "mail": "enni20170711@gmail.com",
  "lab": 864
}

doc_ref = db.collection("靜宜資管2026B")
doc_ref.add(doc)
