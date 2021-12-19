from flask import Flask, request, render_template, jsonify, redirect
from firebase_admin import credentials, firestore, initialize_app
import pandas as pd
from datetime import datetime
import pickle

# Flask App
app = Flask(__name__)

# Memuat data model yang sudah simpan
model = pickle.load(open('gnb.pkl', 'rb'))

# Inisialisasi database firestore
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
history_ref = db.collection('histories')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/feature")
def feature():
    return render_template('feature.html')

@app.route("/history", methods=['GET'])
def history():
    """
        read() : Fetches documents from Firestore collection as JSON
        todo : Return document that matches query ID
        all_todos : Return all documents
    """
    try:
        histories = [doc.to_dict() for doc in history_ref.stream()]
        histories.sort(key=lambda item:item['created_at'], reverse=True)
        return render_template('history.html', histories=histories)
    except Exception as e:
        return f"An Error Occured: {e}"

    

@app.route("/predict", methods=['POST'])
def predict():
    data =  {   
        'hemo': [request.form['hemo']],
        'al': [request.form['al']],
        'rbcc': [request.form['rbcc']],
        'sc': [request.form['sc']],
        'rbc': [request.form['rbc']],
        'bp': [request.form['bp']],
        'su': [request.form['su']],
        'age': [request.form['age']],
        'dm': [request.form['dm']], 
        'ba': [request.form['ba']],
        'pcc': [request.form['pcc']],
        'pc': [request.form['pc']],
        'sg': [request.form['sg']],
        'sod': [request.form['sod']],
        'bu': [request.form['bu']],
        'pot': [request.form['pot']],
        'cad': [request.form['cad']],
        'htn': [request.form['htn']],
        'ane': [request.form['ane']],
        'bgr': [request.form['bgr']],
        'pe': [request.form['pe']], 
    }
    
    df = pd.DataFrame(data)
    
    prediction = model.predict(df)
    if prediction == 1:
        output = 'Gagal ginjal kronik'
    else :
        output = 'Gagal ginjal akut'

    data['prediction'] = output
    data['created_at'] = datetime.now()

    """
        create() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:        
        history_ref.document().set(data)
        return redirect('/history')
    except Exception as e:
        return f"An Error Occured: {e}"
    
# @app.route('/history/update', methods=['POST', 'PUT'])
# def update():
#     """
#         update() : Update document in Firestore collection with request body
#         Ensure you pass a custom ID as part of json body in post request
#         e.g. json={'id': '1', 'title': 'Write a blog post today'}
#     """
#     try:
#         id = request.json['id']
#         history_ref.document(id).update(request.json)
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"

# @app.route('/history/delete', methods=['GET', 'DELETE'])
# def delete():
#     """
#         delete() : Delete a document from Firestore collection
#     """
#     try:
#         # Check for ID in URL query
#         history_id = request.args.get('id')
#         history_ref.document(history_id).delete()
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"

# if __name__ == "__main__":
#     app.run(debug=True)

# port = int(os.environ.get('PORT', 8080))
# if __name__ == '__main__':
#     app.run(threaded=True, host='0.0.0.0', port=port)