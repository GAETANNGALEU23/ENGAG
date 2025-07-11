import streamlit as st
import streamlit.components.v1 as components
import json
import os
import pandas as pd
import io
import sys
import uuid
from datetime import datetime
#from reportlab.lib.pagesizes import letter
#from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
#from reportlab.lib import colors
import shutil
import time

# Importer le pipeline
pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "PIPELINE_COMPLET"))
sys.path.append(pipeline_path)
#from Pipeline import execute_pipeline
#from PIPELINE_COMPLET.Pipeline import execute_pipeline


# Configuration page Streamlit
st.set_page_config(page_title="Afriland First Bank - Reporting", page_icon="🏦", layout="wide")

# Style CSS personnalisé
st.markdown("""
    <style>
        /* Style général */
        .main { background-color: #f8f9fa; }
        
        /* Messages utilisateur */
        .user-message {
            background-color: #c8102e;
            color: white;
            padding: 10px 15px;
            border-radius: 15px 15px 0 15px;
            margin: 5px 0;
            max-width: 80%;
            float: right;
            clear: both;
        }
        
        /* Messages bot */
        .bot-message {
            background-color: #f0f0f0;
            color: #333;
            padding: 10px 15px;
            border-radius: 15px 15px 15px 0;
            margin: 5px 0;
            max-width: 80%;
            float: left;
            clear: both;
        }
        
        /* Sidebar */
        .sidebar .sidebar-content {
            background-color: #002d72;
            color: white;
        }
        
        /* Boutons */
        .stButton>button {
            background-color: #c8102e;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
        }
        
        .stButton>button:hover {
            background-color: #a00d26;
            color: white;
        }
        
        /* Input */
        .stTextInput>div>div>input {
            border-radius: 5px;
            border: 1px solid #c8102e;
        }
        
        /* Logo dans la sidebar */
        .logo-container {
            text-align: center;
            padding: 20px 0;
        }
        
        .logo-img {
            max-width: 80%;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

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

# Sidebar avec logo
with st.sidebar:
    st.markdown("""
        <div class="logo-container">
            <h3>Afriland First Bank</h3>
            <!-- Remplacez 'logo_afriland.jpg' par le chemin de votre image -->
            <img src="Capture d’écran 2025-06-25 191500.png" class="logo-img" alt="Logo Afriland First Bank">
            <img src="C:\Users\HP X360 G6\Desktop\Dashboard\Capture d’écran 2025-06-25 191500.png" class="logo-img" alt="Logo Afriland First Bank">
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("**Session ID:**")
    st.code(st.session_state.session_id)
    
    if st.session_state.query_logs:
        st.markdown("**Historique des requêtes:**")
        for log in st.session_state.query_logs[-5:]:  # Affiche les 5 dernières requêtes
            st.markdown(f"🔹 {log['phrase'][:30]}...")


# ... (le reste de votre code reste inchangé jusqu'à la partie sidebar)

# Sidebar avec logo et historique
with st.sidebar:
    
    # Section Historique
    st.markdown("**Historique des requêtes**")
    
    if st.session_state.query_logs:
        # Afficher les 10 dernières requêtes (les plus récentes en premier)
        for i, log in enumerate(reversed(st.session_state.query_logs[-10:])):
            # Créer des colonnes pour le numéro et le contenu
            col1, col2 = st.columns([0.1, 0.9])
            with col1:
                st.markdown(f"**{len(st.session_state.query_logs)-i}.**")
            with col2:
                # Bouton cliquable pour recharger une ancienne requête
                if st.button(log['phrase'][:50] + ("..." if len(log['phrase'])>50 else ""), 
                           key=f"hist_{log['id']}",
                           help="Cliquez pour recharger cette requête"):
                    st.session_state.messages.append({"role": "user", "content": log['phrase']})
                    st.rerun()
                    
            st.markdown(f"<small>{log['timestamp']}</small>", unsafe_allow_html=True)
            st.markdown("---")
    else:
        st.markdown("<small>Aucune requête enregistrée</small>", unsafe_allow_html=True)
    
    # Bouton pour vider l'historique
    if st.session_state.query_logs and st.button("🧹 Vider l'historique"):
        st.session_state.query_logs = []
        st.rerun()

# ... (le reste de votre code)









# Bandeau principal
st.markdown("""
    <div style="background-color:#002d72;padding:15px;border-radius:10px;color:white;text-align:center;">
        <h2 style="color:white;margin:0;">Afriland First Bank - IA Reporting</h2>
        <p style="margin:0;">Générez des rapports automatisés à partir de vos requêtes</p>
    </div>
""", unsafe_allow_html=True)

# Espacement
st.markdown("<br>", unsafe_allow_html=True)

# Affichage des messages
for message in st.session_state.messages:
    role_class = "user-message" if message["role"] == "user" else "bot-message"
    st.markdown(f'<div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)

# Entrée utilisateur
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input("Posez votre question ou décrivez le rapport souhaité :", label_visibility="collapsed", placeholder="Ex: Analyse des transactions du mois dernier")
with col2:
    if st.button("Envoyer", use_container_width=True) and user_input:
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

        with st.spinner("Analyse en cours... Veuillez patienter."):
            try:
                execute_pipeline(output_directory=query_dir)

                if os.path.exists(merged_output_path):
                    with open(merged_output_path, "r", encoding="utf-8") as f:
                        result = json.load(f)
                    bot_response = f"✅ Analyse terminée pour : '{user_input}'"
                    st.session_state.pipeline_executed = True
                    st.session_state.last_output_path = merged_output_path
                    st.session_state.last_user_input = user_input
                    st.session_state.query_logs.append({
                        "id": query_id,
                        "phrase": user_input,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "dir": query_dir
                    })

                    # Affichage immédiat du résultat
                    st.success(bot_response)

                    # Visualisations PNG
                    if os.path.exists(visualisation_dir):
                        image_files = [f for f in os.listdir(visualisation_dir) if f.endswith(".png")]
                        for image_file in sorted(image_files):
                            st.image(os.path.join(visualisation_dir, image_file), caption=image_file, use_column_width=True)
                    else:
                        st.warning("Aucune visualisation trouvée.")

                    # Tableau HTML
                    if os.path.exists(summary_html_path):
                        with open(summary_html_path, "r", encoding="utf-8") as f:
                            html_content = f.read()
                        try:
                            df = pd.read_html(io.StringIO(html_content.replace("'", '"')))[0]
                            st.markdown("### 📊 Aperçu du rapport généré :")
                            st.dataframe(df, use_container_width=True)
                        except Exception as e:
                            st.error(f"Erreur affichage tableau : {e}")
                    else:
                        st.warning("Le fichier summary_simple_table.html est introuvable.")

                else:
                    st.error("Le fichier de sortie n'a pas été généré.")

            except Exception as e:
                st.error(f"Erreur exécution pipeline : {e}")
