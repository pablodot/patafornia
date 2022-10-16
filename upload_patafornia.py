from firebase_admin import credentials, initialize_app, storage
import glob
import os

cred = credentials.Certificate("patafornia-firebase-adminsdk-x8kpi-e0c09c8662.json")
initialize_app(cred, {'storageBucket': 'patafornia.appspot.com'})

files =glob.glob('/home/pablo/beach/*.jpg')
bucket = storage.bucket()


for file in files:
	print(file)
	blob = bucket.blob(os.path.basename(file))
	if not blob.exists():
	    blob.upload_from_filename(file)
	    blob.make_public()
	    print("url", blob.public_url)
	else:
	    print(blob.name, 'ya existe')
