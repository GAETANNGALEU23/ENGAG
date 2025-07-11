# import streamlit as st
# import streamlit.components.v1 as components
# import json
# import os
# import pandas as pd
# import io
# import sys
# import uuid
# from datetime import datetime
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from reportlab.lib import colors
# # import Pipeline  # Importer Pipeline.py
# pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PIPELINE_COMPLET"))
# sys.path.append(pipeline_path)
# from Pipeline import execute_pipeline
# import shutil
# import time

# def clean_old_sessions(base_dir="tmp_sessions", max_age_minutes=60):
#     """
#     Supprime les dossiers de session plus vieux que `max_age_minutes`.
#     """
#     now = time.time()
#     if not os.path.exists(base_dir):
#         return  # Aucun dossier à nettoyer
#     for folder in os.listdir(base_dir):
#         folder_path = os.path.join(base_dir, folder)
#         if os.path.isdir(folder_path):
#             last_modified = os.path.getmtime(folder_path)
#             age_minutes = (now - last_modified) / 60
#             if age_minutes > max_age_minutes:
#                 try:
#                     shutil.rmtree(folder_path)
#                     print(f"Dossier de session supprimé : {folder_path}")
#                 except Exception as e:
#                     print(f"Erreur lors de la suppression de {folder_path} : {e}")


# # Configuration de la page
# st.set_page_config(
#     page_title="Afriland First Bank - Reporting",
#     page_icon="🏦",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS pour un design épuré et élégant
# st.markdown("""
#     <style>
#         /* Police et style général */
#         @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
#         body {
#             font-family: 'Roboto', sans-serif;
#             background-color: #f5f5f5;
#             color: #333333;
#         }
#         /* Conteneur principal */
#         .main {
#             background-color: #ffffff;
#             border-radius: 10px;
#             padding: 20px;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             max-width: 1000px;
#             margin: 0 auto;
#         }
#         /* En-tête */
#         .header {
#             background-color: #c8102e;
#             color: #ffffff;
#             padding: 20px;
#             text-align: center;
#             border-radius: 8px 8px 0 0;
#             font-size: 24px;
#             font-weight: 700;
#         }
#         /* Zone de chat */
#         .chat-container {
#             max-height: 500px;
#             overflow-y: auto;
#             padding: 20px;
#             background-color: #f9f9f9;
#             border-radius: -great
#             margin: 20px 0;
#         }
#         .user-message {
#             background-color: #c8102e;
#             color: #ffffff;
#             padding: 10px 15px;
#             border-radius: 15px 15px 0 15px;
#             margin: 10px 0;
#             max-width: 70%;
#             margin-left: auto;
#             text-align: right;
#         }
#         .bot-message {
#             background-color: #ffffff;
#             color: #333333;
#             padding: 10px 15px;
#             border-radius: 15px 15px 15px 0;
#             margin: 10px 0;
#             max-width: 70%;
#             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
#         }
#         /* Input texte */
#         .stTextInput > div > div > input {
#             border: 2px solid #c8102e;
#             border-radius: 8px;
#             padding: 10px;
#             font-size: 16px;
#         }
#         /* Boutons */
#         .stButton > button {
#             background-color: #c8102e;
#             color: #ffffff;
#             border: none;
#             border-radius: 8px;
#             padding: 10px 20px;
#             font-size: 16px;
#             font-weight: 700;
#             transition: background-color 0.3s ease;
#         }
#         .stButton > button:hover {
#             background-color: #a00d24;
#         }
#         /* Sidebar */
#         .css-1d391main {
#             background-color: #ffffff;
#             border-right: 2px solid #c8102e;
#         }
#         .sidebar-content {
#             padding: 20px;
#         }
#         .sidebar-title {
#             color: #c8102e;
#             font-size: 20px;
#             font-weight: 700;
#             margin-bottom: 20px;
#         }
#         /* Footer */
#         .footer {
#             text-align: center;
#             color: #666666;
#             font-size: 14px;
#             margin-top: 20px;
#         }
#         /* Boutons de téléchargement */
#         .download-buttons {
#             display: flex;
#             gap: 10px;
#             margin-top: 10px;
#         }
#     </style>
# """, unsafe_allow_html=True)
# import streamlit as st
# # En-tête
# st.markdown('<div class="header">... OUvronFranchissons ensemble un nouveau cap </div>', unsafe_allow_html=True)
# # Reste du code de votre application Streamlit
# # ...
# # Initialisation de l'historique du chat
# # if "messages" not in st.session_state:
# #     st.session_state.messages = []
# # Initialisation de l'historique du chat et session unique
# if "messages" not in st.session_state:
#     st.session_state.messages = []
    
# if "pipeline_executed" not in st.session_state:
#     st.session_state.pipeline_executed = False

# if "last_output_path" not in st.session_state:
#     st.session_state.last_output_path = None

# if "summary_html_path" not in st.session_state:
#     st.session_state.summary_html_path = None

# if "last_user_input" not in st.session_state:
#     st.session_state.last_user_input = None

# if "query_count" not in st.session_state:
#     st.session_state.query_count = 0

# if "query_logs" not in st.session_state:
#     st.session_state.query_logs = []


# if "session_id" not in st.session_state:
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     random_token = str(uuid.uuid4())[:8]
#     st.session_state.session_id = f"{timestamp}_{random_token}"

# # Définir et créer le répertoire de session
# base_session_dir = "tmp_sessions"
# session_dir = os.path.join(base_session_dir, st.session_state.session_id)
# os.makedirs(session_dir, exist_ok=True)
# # Nettoyage automatique des anciennes sessions (plus vieilles que 60 minutes)
# clean_old_sessions(base_dir=base_session_dir, max_age_minutes=1440)



# # Sidebar pour l'historique uniquement
# with st.sidebar:
#     # st.markdown('<div class="sidebar-title">Historique des requêtes</div>', unsafe_allow_html=True)
#     st.markdown(f"🆔 **Session ID :** `{st.session_state.session_id}`")
#     if st.button("Effacer l'historique"):
#         st.session_state.messages = []
#     if st.session_state.pipeline_executed:
#         # st.markdown("✅ Pipeline exécuté.")
#         st.markdown(f"📄 Rapport : `{os.path.basename(st.session_state.summary_html_path)}`")
#     if st.session_state.last_user_input:
#         st.markdown(f"📝 Dernière requête : *{st.session_state.last_user_input}*")
#     if st.session_state.query_logs:
#         st.markdown("### 📚 Requêtes précédentes :")
#         for log in st.session_state.query_logs[::-1]:  # dernière requête en premier
#             st.markdown(
#                 f"- [{log['id']}] *{log['phrase']}*  \n🕒 {log['timestamp']}"
#             )



# # Conteneur principal du chat
# st.markdown('<div class="main">', unsafe_allow_html=True)
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # Affichage des messages du chat
# for message in st.session_state.messages:
#     if message["role"] == "user":
#         st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
#     else:
#         st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)
#         # Afficher les rapports générés
#         if "Rapport généré avec succès" in message["content"]:
#             # Affichage des visualisations PNG
#             visual_dir = st.session_state.get("visualisation_dir")
#             if visual_dir and os.path.exists(visual_dir):
#                 image_files = [f for f in os.listdir(visual_dir) if f.endswith(".png")]
#                 for image_file in sorted(image_files):  # tri facultatif
#                     image_path = os.path.join(visual_dir, image_file)
#                     st.image(image_path, caption=image_file, use_column_width=True)
#             else:
#                 st.warning("Aucune visualisation PNG trouvée.")
#             st.markdown("---")
#             st.write("Aperçu du rapport généré :")
#             # output_file = "output/summary_simple_table.html"
#             summary_html_path = st.session_state.get("summary_html_path")
            


#             if summary_html_path and os.path.exists(summary_html_path):
#                 # Afficher le tableau interactif
#                 with open(summary_html_path, "r", encoding="utf-8") as f:
#                     html_content = f.read()
#                 try:
#                     df = pd.read_html(io.StringIO(html_content.replace("'", '"')))[0]
#                     st.dataframe(df, use_container_width=True)
                    
#                     # Boutons de téléchargement
#                     st.markdown('<div class="download-buttons">', unsafe_allow_html=True)
#                     # Téléchargement HTML
#                     with open(summary_html_path, "rb") as f:
#                         st.download_button(
#                             label="Télécharger (HTML)",
#                             data=f,
#                             file_name="rapport_afriland.html",
#                             mime="text/html",
#                             key="html_download"
#                         )
#                     # Téléchargement Excel
#                     buffer_excel = io.BytesIO()
#                     with pd.ExcelWriter(buffer_excel, engine='openpyxl') as writer:
#                         df.to_excel(writer, index=False, sheet_name='Rapport')
#                     st.download_button(
#                         label="Télécharger (Excel)",
#                         data=buffer_excel.getvalue(),
#                         file_name="rapport_afriland.xlsx",
#                         mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#                         key="excel_download"
#                     )
#                     # Téléchargement PDF
#                     buffer_pdf = io.BytesIO()
#                     doc = SimpleDocTemplate(buffer_pdf, pagesize=letter)
#                     table_data = [df.columns.tolist()] + df.values.tolist()
#                     table = Table(table_data)
#                     table.setStyle(TableStyle([
#                         ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#c8102e')),
#                         ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
#                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                         ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
#                         ('FONTSIZE', (0, 0), (-1, -1), 12),
#                         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                         ('BACKGROUND', (0, 1), (-1, -1), colors.white),
#                         ('GRID', (0, 0), (-1, -1), 1, colors.black)
#                     ]))
#                     elements = [table]
#                     doc.build(elements)
#                     st.download_button(
#                         label="Télécharger (PDF)",
#                         data=buffer_pdf.getvalue(),
#                         file_name="rapport_afriland.pdf",
#                         mime="application/pdf",
#                         key="pdf_download"
#                     )
#                     st.markdown('</div>', unsafe_allow_html=True)
#                 except Exception as e:
#                     st.error(f"Erreur lors de la lecture du tableau HTML : {str(e)}")
#             else:
#                 st.error("Le fichier de rapport (summary_simple_table.html) n'a pas été généré.")

# st.markdown('</div>', unsafe_allow_html=True)

# # Entrée utilisateur
# user_input = st.text_input("Posez votre question ou décrivez le rapport souhaité :")
# if st.button("Envoyer"):
#     if user_input:
#         # Ajouter le message de l'utilisateur à l'historique
#         st.session_state.messages.append({"role": "user", "content": user_input})

#         # Incrémenter le compteur de requête
#         st.session_state.query_count += 1
#         query_id = f"{st.session_state.query_count:04d}"  # exemple: '0001'

#         # Créer un sous-dossier pour cette requête dans la session
#         query_dir = os.path.join(session_dir, query_id)
#         os.makedirs(query_dir, exist_ok=True)
        
        




#         # Créer un fichier JSON temporaire pour la requête
#         # input_json_path = "input_phrases.json"
#         input_json_path = os.path.join(query_dir, "input_phrases.json")
#         output_path = os.path.join(query_dir, "merged_output.json")
#         summary_html_path = os.path.join(query_dir, "summary_simple_table.html")
#         visualisation_dir = os.path.join(query_dir, "visualisations")
#         st.session_state.visualisation_dir = visualisation_dir

        


#         try:
#             with open(input_json_path, "w", encoding="utf-8") as f:
#                 json.dump({"phrases": [user_input]}, f, ensure_ascii=False, indent=2)
#         except Exception as e:
#             st.error(f"Erreur lors de la création du fichier input_phrases.json : {str(e)}")
#             st.session_state.messages.append({"role": "bot", "content": f"Erreur lors de la création du fichier d'entrée : {str(e)}"})
#             st.markdown('</div>', unsafe_allow_html=True)
#             st.markdown('<div class="footer">© 2025 Afriland First Bank - Powered by xAI</div>', unsafe_allow_html=True)
#             st.markdown('</div>', unsafe_allow_html=True)
#             st.stop()

#         # Indicateur de chargement
#         with st.spinner("Traitement de votre requête en cours..."):
#             try:
#                 # Vérifier les dépendances du pipeline
#                 config = {
#                     "model_path": "../AGENT1/custom_ner_model",
#                     "terms_dict_path": "../AGENT1/bank_terms_dictionary.json",
#                     "chroma_db_path": "../AGENT1/chroma_db",
#                     "df_engagements_path": "../Doc_DF/Pipeline/output/DF_ENGAGEMENTS_030725_UTF8_results.json"
#                 }
#                 missing_files = [path for path in config.values() if not os.path.exists(path)]
#                 if missing_files:
#                     raise FileNotFoundError(f"Fichiers manquants : {', '.join(missing_files)}")
                
#                 # Appeler le pipeline
#                 execute_pipeline(output_directory=query_dir)


                
#                 # Vérifier si le fichier de sortie existe
#                 # output_path = "output/merged_output.json"
                

#                 if os.path.exists(output_path):
#                     with open(output_path, "r", encoding="utf-8") as f:
#                         result = json.load(f)
#                     bot_response = f"Analyse de votre requête : '{user_input}'. Rapport généré avec succès."
#                         # Mettre à jour l'état de session
#                     st.session_state.pipeline_executed = True
#                     st.session_state.last_output_path = output_path
#                     st.session_state.summary_html_path = summary_html_path
#                     st.session_state.query_logs.append({
#                         "id": query_id,
#                         "phrase": user_input,
#                         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                         "dir": query_dir
#                     })

#                     st.session_state.last_user_input = user_input

#                 else:
#                     bot_response = "Erreur : Le fichier de sortie (merged_output.json) n'a pas été généré."
                
#                 # Nettoyer le fichier temporaire
#                 if os.path.exists(input_json_path):
#                     os.remove(input_json_path)
                    
#             except Exception as e:
#                 bot_response = f"Erreur lors du traitement : {str(e)}"
#                 # Nettoyer le fichier temporaire en cas d'erreur
#                 if os.path.exists(input_json_path):
#                     os.remove(input_json_path)
        
#         # Ajouter la réponse du bot à l'historique
#         st.session_state.messages.append({"role": "bot", "content": bot_response})

# # Footer
# st.markdown('<div class="footer">© 2025 Afriland First Bank - Powered by xAI</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)























































import streamlit as st
import streamlit.components.v1 as components
import json
import os
import pandas as pd
import io
import sys
import uuid
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import shutil
import time

# Importer le pipeline
pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PIPELINE_COMPLET"))
sys.path.append(pipeline_path)
from Pipeline import execute_pipeline

# Configuration page Streamlit
st.set_page_config(page_title="Afriland First Bank - Reporting", page_icon="🏦", layout="wide")

# Nettoyage des anciennes sessions
def clean_old_sessions(base_dir="tmp_sessions", max_age_minutes=60):
    now = time.time()
    if not os.path.exists(base_dir):
        return
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            age_minutes = (now - os.path.getmtime(folder_path)) / 60
            if age_minutes > max_age_minutes:
                try:
                    shutil.rmtree(folder_path)
                except Exception as e:
                    print(f"Erreur suppression : {e}")

# Initialiser la session Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pipeline_executed" not in st.session_state:
    st.session_state.pipeline_executed = False
if "last_output_path" not in st.session_state:
    st.session_state.last_output_path = None
if "summary_html_path" not in st.session_state:
    st.session_state.summary_html_path = None
if "last_user_input" not in st.session_state:
    st.session_state.last_user_input = None
if "query_count" not in st.session_state:
    st.session_state.query_count = 0
if "query_logs" not in st.session_state:
    st.session_state.query_logs = []
if "session_id" not in st.session_state:
    st.session_state.session_id = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{str(uuid.uuid4())[:8]}"

# Créer le dossier de session
base_session_dir = "tmp_sessions"
session_dir = os.path.join(base_session_dir, st.session_state.session_id)
os.makedirs(session_dir, exist_ok=True)
clean_old_sessions(base_session_dir, 1440)

# Bandeau
st.markdown('<div style="background-color:#c8102e;padding:15px;border-radius:10px;color:white;text-align:center;"><h2>Afriland First Bank - IA Reporting</h2></div>', unsafe_allow_html=True)

# Affichage des messages
for message in st.session_state.messages:
    role_class = "user-message" if message["role"] == "user" else "bot-message"
    st.markdown(f'<div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)

# Entrée utilisateur
user_input = st.text_input("Posez votre question ou décrivez le rapport souhaité :")
if st.button("Envoyer") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.query_count += 1
    query_id = f"{st.session_state.query_count:04d}"
    query_dir = os.path.join(session_dir, query_id)
    os.makedirs(query_dir, exist_ok=True)

    input_json_path = os.path.join(query_dir, "input_phrases.json")
    summary_html_path = os.path.join(query_dir, "summary_simple_table.html")
    visualisation_dir = os.path.join(query_dir, "visualisations")
    merged_output_path = os.path.join(query_dir, "merged_output.json")

    st.session_state.summary_html_path = summary_html_path
    st.session_state.visualisation_dir = visualisation_dir

    try:
        with open(input_json_path, "w", encoding="utf-8") as f:
            json.dump({"phrases": [user_input]}, f, ensure_ascii=False, indent=2)
    except Exception as e:
        st.error(f"Erreur création input : {e}")
        st.stop()

    with st.spinner("Analyse en cours..."):
        try:
            execute_pipeline(output_directory=query_dir)

            if os.path.exists(merged_output_path):
                with open(merged_output_path, "r", encoding="utf-8") as f:
                    result = json.load(f)
                bot_response = f"Analyse de votre requête : '{user_input}'. Rapport généré avec succès."
                st.session_state.pipeline_executed = True
                st.session_state.last_output_path = merged_output_path
                st.session_state.last_user_input = user_input
                st.session_state.query_logs.append({
                    "id": query_id,
                    "phrase": user_input,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "dir": query_dir
                })

                # ✅ Affichage immédiat du résultat
                st.success(bot_response)

                # 🖼️ Visualisations PNG
                if os.path.exists(visualisation_dir):
                    image_files = [f for f in os.listdir(visualisation_dir) if f.endswith(".png")]
                    for image_file in sorted(image_files):
                        st.image(os.path.join(visualisation_dir, image_file), caption=image_file, use_column_width=True)
                else:
                    st.warning("Aucune visualisation trouvée.")

                # 📊 Tableau HTML
                if os.path.exists(summary_html_path):
                    with open(summary_html_path, "r", encoding="utf-8") as f:
                        html_content = f.read()
                    try:
                        df = pd.read_html(io.StringIO(html_content.replace("'", '"')))[0]
                        st.markdown("### Aperçu du rapport généré :")
                        st.dataframe(df, use_container_width=True)
                    except Exception as e:
                        st.error(f"Erreur affichage tableau : {e}")
                else:
                    st.warning("Le fichier summary_simple_table.html est introuvable.")

            else:
                st.error("Le fichier de sortie n’a pas été généré.")

        except Exception as e:
            st.error(f"Erreur exécution pipeline : {e}")