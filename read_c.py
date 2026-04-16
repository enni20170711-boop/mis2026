import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

keyword = "楊"
collection_ref = db.collection("靜宜資管2026B")
#docs = collection_ref.where(filter=FieldFilter("mail","==", "enni20170711@gmail.com")).get()
#docs = collection_ref.where(filter=FieldFilter("lab",">", 579)).get()
docs = collection_ref.order_by("lab",direction=firestore.Query.DESCENDING).limit(5).get()
for doc in docs:
 teacher=doc.to_duct()
 if keyword in teacher["name"]
  primt(teacher)
  
