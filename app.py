import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Banking Cup", page_icon="🏆", layout="centered")

# --- INITIALISATION DE LA NAVIGATION ---
# On crée une variable 'etape' dans la mémoire du navigateur s'il n'existe pas
if 'etape' not in st.session_state:
    st.session_state.etape = 'bienvenue'

# Fonctions pour changer de page
def aller_au_mode_demploi():
    st.session_state.etape = 'manuel'

def lancer_le_jeu():
    st.session_state.etape = 'jeu'

# --- 1. ÉCRAN DE BIENVENUE ---
if st.session_state.etape == 'bienvenue':
    st.markdown("<br><br>", unsafe_allow_html=True) # Un peu d'espace
    st.title("🏆 Bienvenue à Banking Cup")
    st.write("### Prêt à prendre les rênes de votre banque ?")
    st.info("Dans cette simulation, vous allez affronter d'autres directeurs d'agences pour conquérir le marché.")
    
    st.button("Découvrir mon objectif et le mode d'emploi ➡️", on_click=aller_au_mode_demploi, use_container_width=True)

# --- 2. ÉCRAN MODE D'EMPLOI ---
elif st.session_state.etape == 'manuel':
    st.title("📖 Mode d'emploi")
    
    st.markdown("""
    ### Votre objectif
    Vous êtes **Directeur d'une banque**, votre objectif : **faire un meilleur résultat net que vos concurrents.**
    
    ### Comment animer votre banque ?
    
    🟠 **La partie Orange (Décisions)** :  
    C'est votre levier de gestion, de management et de prix. **C'est la seule partie à remplir avec des chiffres.**
    * *Action* : Complétez la colonne de l'année en cours, validez, et prévenez le Maître du Jeu.
    * *Rythme* : L'opération se répète sur 5 ans. Le Maître du Jeu verrouille et déverrouille les accès à chaque manche.
    
    🔵 **La partie Bleue (Résultats)** :  
    Elle vous permet d'analyser vos actions passées et de visualiser les indicateurs financiers de votre banque.
    
    🟡 **La partie Jaune (Marché)** :  
    Indispensable pour situer votre banque vis-à-vis de vos concurrents et adapter votre stratégie pour le tour suivant.
    
    ⚠️ **Attention à rester cohérent dans vos choix !**
    """)
    
    st.warning("⚠️ Une fois vos décisions envoyées, vous ne pourrez plus les modifier pour la manche en cours.")
    
    st.button("J'ai compris, accéder au tableau de bord de la banque 🚀", on_click=lancer_le_jeu, use_container_width=True)

# --- 3. L'INTERFACE DE JEU (TON ANCIEN CODE) ---
elif st.session_state.etape == 'jeu':
    
    # Bouton retour (optionnel) pour relire le manuel
    if st.sidebar.button("⬅️ Relire le mode d'emploi"):
        st.session_state.etape = 'manuel'
        st.rerun()

    st.title("🏢 Tableau de Bord de la Banque")
    
    # Ici, on insère toute ta logique de saisie avec les expanders (ton code précédent)
    manche_verrouillee = st.sidebar.toggle("🔒 Verrouillage MJ", value=False)
    
    if manche_verrouillee:
        st.error("🔒 MANCHE CLÔTURÉE : Le Maître du Jeu calcule les résultats.")
    else:
        st.success("🔓 MANCHE OUVERTE : Saisie de l'Année N+1 en cours.")

    # --- REPRISE DE TES SECTIONS (Exemple simplifié, remets tes 32 variables ici) ---
    with st.expander("🟠 ZONE ORANGE : Vos Décisions", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            urbaine = st.number_input("Agences Urbaines", value=113, disabled=manche_verrouillee)
            tx_immo = st.number_input("Taux Immobilier (%)", value=3.70, step=0.05, disabled=manche_verrouillee)
        with col2:
            rurale = st.number_input("Agences Rurales", value=121, disabled=manche_verrouillee)
            pub = st.number_input("Budget Pub (€)", value=1000000, step=50000, disabled=manche_verrouillee)
    
    if st.button("🚀 Soumettre les décisions", use_container_width=True, disabled=manche_verrouillee):
        st.balloons()
        st.success("Décisions transmises au Maître du Jeu !")

    with st.expander("🔵 ZONE BLEUE : Vos Résultats"):
        st.write("Les résultats s'afficheront ici après validation du tour.")

    with st.expander("🟡 ZONE JAUNE : Analyse Marché"):
        st.write("Positionnement par rapport aux 4 autres banques.")
