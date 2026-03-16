import os
import shutil
from docx import Document

project_name = "star"

base_path = r"C:\Users\Lenovo\Downloads"
template_path = r"C:\Users\Lenovo\my-project\template"

project_path = os.path.join(base_path,project_name)
analysis_folder = os.path.join(project_path, "Analysis")

def find_scope_document(folder, subfolder):
    search_path = os.path.join(folder,subfolder)
    if not os.path.exists(search_path):
        return None
    for file in os.listdir(search_path):
        if "scope" in file.lower() and file.endswith(".docx"):
            return os.path.join(search_path, file)
    return None

def copy_matching_sql_files(keyword, source_folder, destination_folder):
    copied_any = False
    for root, dirs, files in os.walk(source_folder): 
        for file in files:
            if file.endswith(".sql") and keyword in file.lower():
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_folder, file)
                if os.path.exists(destination_file):
                    print(f"skipping (already exists): {file}")
                else:
                    shutil.copy2(source_file,destination_file)
                    copied_any = True
    return copied_any



scope_doc_path = find_scope_document(project_path, "Management Information")

if not scope_doc_path:
    print("No scope document found.")
    exit()

doc = Document(scope_doc_path)
full_text = "\n".join([para.text for para in doc.paragraphs]).lower()


if "rules-based attribution" in full_text:
    print("📊 Rules-Based Attribution found in scope doc")
    copied = copy_matching_sql_files("rules", template_path, analysis_folder)
    if copied:
        print(f"Rules-based attribution scripts copied to: {analysis_folder}")
    else:
        print("No new rules-based attribution files were copied.")


if "keyword insights" in full_text:
    print("📊 keyword insights found in scope doc")
    copied = copy_matching_sql_files("rules", template_path, analysis_folder)
    if copied:
        print(f"keyword insights scripts copied to: {analysis_folder}")
    else:
        print("No new keyword insights files were copied.")





"""

python project_setup.py

pip install python-docx

"""