

class Admin:
    def delete_admin(self, admn_id):
        cred = credentials.Certificate('firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json')
        firebase_admin.initialize_app(cred)

        db = firestore.client()
        # Reference to the 'admin' collection in Firebase
        admin_ref = db.collection('admins')
        # Check if the entered old_admin_id exists in the admin table
        query = admin_ref.where('id', '==', str(admn_id)).get()
        if len(query) != 1:
            print("Wrong old admin id .")
        else:
            for doc in query:
                doc.reference.delete()
                print("We will delete ",doc.to_dict())
                print("Admin deleted successfully.")


    def add_admin(self, old_admin_id, password, email, name):
        cred = credentials.Certificate('7oty hna zai aly kan mawgood')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        # Reference to the 'admin' collection in Firebase
        admin_ref = db.collection('admins')
        # Check if the entered old_admin_id exists in the admin table
        query = admin_ref.where('old_admin_id', '==', old_admin_id).get()
        for res in query:
            print(res.to_dict())

        if not len(query) > 0:
            print("Old admin not found.")
        else:
            # Check if the entered ID already exists in any admin entry
            query = admin_ref.where('id', '==', old_admin_id+1).limit(1).get()
            if len(query) > 0:
                print("ID must be unique. ID already exists.")
            else:
                # Create a new admin entry with the provided data
                admin_data = {
                    'email': email,
                    'id': old_admin_id+1,
                    'name': name,
                    'old_admin_id': old_admin_id,
                    'password': password
                }
                admin_ref.add(admin_data)
                print("Admin added successfully.")

