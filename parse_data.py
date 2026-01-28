import csv
import json

files = ['Chamadas - Provão Paulista_1ª CHAMADA_Tabela.csv', 'Chamadas - Provão Paulista_2ª CHAMADA_Tabela.csv']
data = {}

def clean_school_name(name):
    return name.strip().upper()

for fpath in files:
    try:
        with open(fpath, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                school = clean_school_name(row['Escola'])
                if school not in data:
                    data[school] = []
                
                course_full = row['Curso']
                # Try to clean up course name if needed, or keep full
                # Format: "Code - Name - Shift - Fatec..."
                # Let's keep it full or split? User asked for "Curso". Full string gives all info.
                
                student = {
                    'name': row['Nome do aluno'].title(),
                    'course': row['Curso'],
                    'ies': row['IES']
                }
                data[school].append(student)
    except FileNotFoundError:
        print(f"File not found: {fpath}")

with open('schools_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
