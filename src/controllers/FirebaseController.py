from .BaseController import BaseController
from firebase_admin import credentials, firestore, initialize_app
import os

class FirebaseController(BaseController):
    def __init__(self):
        super().__init__()
        cred = credentials.Certificate(os.getenv('FIREBASE_CREDENTIALS_PATH'))
        initialize_app(cred)
        self.db = firestore.client()

    def get_firebase_data(self):
        docs = self.db.collection('destinations').stream()
        extracted_data = []

        for doc in docs:
            data = doc.to_dict()
            extracted_info = {
                'document_id': doc.id,
                'description': data.get('description'),
                'image': data.get('image'),
                'gallary_image1': data.get('gallary_image1'),
                'gallary_image2': data.get('gallary_image2'),
                'gallary_image3': data.get('gallary_image3')
            }
            extracted_data.append(extracted_info)

        return extracted_data
