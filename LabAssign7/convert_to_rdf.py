import pandas as pd
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD, RDFS
from datetime import datetime

# Define namespaces
TB = Namespace("http://example.org/tb/")
SCHEMA = Namespace("http://schema.org/")

# Initialize RDF Graph
g = Graph()
g.bind("tb", TB)
g.bind("schema", SCHEMA)

# Read CSV file
df = pd.read_csv('Tb disease symptoms.csv')

# Process symptoms (note trailing spaces in some column names)
symptoms = [
    'fever for two weeks',
    'coughing blood',
    'sputum mixed with blood',
    'night sweats ',
    'chest pain',
    'back pain in certain parts ',
    'shortness of breath',
    'weight loss ',
    'body feels tired',
    'lumps that appear around the armpits and neck',
    'cough and phlegm continuously for two weeks to four weeks',
    'swollen lymph nodes',
    'loss of appetite'
]

for _, row in df.iterrows():
    patient_id = str(row['id']).strip()
    patient_uri = URIRef(TB[f"patient/{patient_id}"])
    
    # Add patient details
    g.add((patient_uri, SCHEMA.name, Literal(row['name'])))
    g.add((patient_uri, SCHEMA.gender, Literal(row['gender'])))

    # Handle date (MM/DD/YYYY → YYYY-MM-DD)
    try:
        date_str = datetime.strptime(row['date'], "%m/%d/%Y").strftime("%Y-%m-%d")
        g.add((patient_uri, SCHEMA.date, Literal(date_str, datatype=XSD.date)))
    except ValueError:
        print(f"Invalid date format for patient {patient_id}: {row['date']}")

    # Handle time (h:mm AM/PM → HH:MM:SS)
    try:
        time_obj = datetime.strptime(row['time'], "%I:%M %p").time()
        g.add((patient_uri, TB.time, Literal(time_obj.isoformat(), datatype=XSD.time)))
    except ValueError:
        print(f"Invalid time format for patient {patient_id}: {row['time']}")

    # Process symptoms
    for symptom_col in symptoms:
        if row.get(symptom_col.strip()) == 1:  # Handle trailing spaces in column names
            symptom_slug = symptom_col.strip().replace(' ', '_').replace('/', '_').lower()
            symptom_uri = URIRef(TB[f"symptom/{symptom_slug}"])
            g.add((symptom_uri, RDF.type, TB.Symptom))
            g.add((patient_uri, TB.hasSymptom, symptom_uri))

# Serialize the graph
g.serialize('tb_symptoms.ttl', format='turtle')
