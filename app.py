import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Banking Cup", page_icon="🏆", layout="wide")

# --- INITIALISATION DE LA NAVIGATION ---
if 'etape' not in st.session_state:
    st.session_state.etape = 'bienvenue'

def aller_au_mode_demploi():
    st.session_state.etape = 'manuel'

def lancer_le_jeu():
    st.session_state.etape = 'jeu'

# --- 1. ÉCRAN DE BIENVENUE ---
if st.session_state.etape == 'bienvenue':
    st.markdown("<br><br>", unsafe_allow_html=True)
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
    
    Hub de pilotage divisé en 3 zones distinctes :
    * 🟠 **La ZONE ORANGE (Décisions)** : C'est votre levier de gestion, de management et de prix. **C'est la seule partie à remplir avec des chiffres.** Complétez la colonne de l'année en cours, validez, et prévenez le Maître du Jeu.
    * 🔵 **La ZONE BLEUE (Résultats)** : Elle vous permet d'analyser vos actions passées et de visualiser les indicateurs financiers de votre banque.
    * 🟡 **La ZONE JAUNE (Marché)** : Indispensable pour situer votre banque vis-à-vis de vos concurrents et adapter votre stratégie pour le tour suivant.
    
    ⚠️ **Attention à rester cohérent dans vos choix !**
    """)
    st.button("J'ai compris, accéder au tableau de bord de la banque 🚀", on_click=lancer_le_jeu, use_container_width=True)

# --- 3. L'INTERFACE DE JEU COMPLÈTE ---
elif st.session_state.etape == 'jeu':
    if st.sidebar.button("⬅️ Relire le mode d'emploi"):
        st.session_state.etape = 'manuel'
        st.rerun()

    st.title("🏢 Tableau de Bord de la Banque")
    
    # Simulateur de verrouillage du MJ
    manche_verrouillee = st.sidebar.toggle("🔒 Verrouillage MJ", value=False)
    
    if manche_verrouillee:
        st.error("🔒 MANCHE CLÔTURÉE : Le Maître du Jeu calcule les résultats de la manche.")
    else:
        st.success("🔓 MANCHE OUVERTE : Saisie de l'Anée N+1 en cours.")

    # Organisation en 3 grands onglets (Orange, Bleu, Jaune) comme ton règlement !
    onglet_orange, onglet_bleu, onglet_jaune = st.tabs(["🟠 ZONE ORANGE : Vos Décisions", "🔵 ZONE BLEUE : Vos Résultats", "🟡 ZONE JAUNE : Analyse Marché"])

    with onglet_orange:
        st.write("### Remplissez vos variables pour l'Année N+1")
        st.caption("💡 Les valeurs de l'Année N sont affichées à titre de rappel juste au-dessus de chaque case.")
        
        # Section 1: Agences
        with st.expander("🏢 1. Gestion du Réseau d'Agences", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.caption("Année N — Urbaines : 112")
                urbaine = st.number_input("Agences Urbaines (Année N+1)", min_value=0, value=112, disabled=manche_verrouillee)
            with col2:
                st.caption("Année N — Rurales : 121")
                rurale = st.number_input("Agences Rurales (Année N+1)", min_value=0, value=121, disabled=manche_verrouillee)

        # Section 2: Effectifs
        with st.expander("👥 2. Gestion des Effectifs (RH)", expanded=False):
            c1, c2 = st.columns(2)
            with c1:
                st.caption("Année N — Conseiller Pro : 120")
                c_pro = st.number_input("Conseiller professionnel", min_value=0, value=120, disabled=manche_verrouillee)
                
                st.caption("Année N — Conseiller Particulier : 816")
                c_part = st.number_input("Conseiller particulier", min_value=0, value=816, disabled=manche_verrouillee)
                
                st.caption("Année N — Directeur d'agence : 195")
                dir_ag = st.number_input("Directeur d'agence", min_value=0, value=195, disabled=manche_verrouillee)
            with c2:
                st.caption("Année N — Gestion de Patrimoine : 116")
                c_patr = st.number_input("Conseiller en gestion de patrimoine", min_value=0, value=116, disabled=manche_verrouillee)
                
                st.caption("Année N — Collaborateur CRC : 25")
                col_crc = st.number_input("Collaborateur CRC", min_value=0, value=25, disabled=manche_verrouillee)

        # Section 3: Budgets
        with st.expander("💰 3. Budgets & Investissements Généraux (€)", expanded=False):
            b1, b2 = st.columns(2)
            with b1:
                st.caption("Année N : 3 000 000 €")
                renov = st.number_input("Rénovation / Investissement (€)", min_value=0, value=3000000, step=50000, disabled=manche_verrouillee)
                
                st.caption("Année N : 2 000 000 €")
                pub = st.number_input("Campagne publicitaire (€)", min_value=0, value=2000000, step=50000, disabled=manche_verrouillee)
            with b2:
                st.caption("Année N : 1 000 000 €")
                qualite = st.number_input("Création de service qualité (€)", min_value=0, value=1000000, step=50000, disabled=manche_verrouillee)
                
                st.caption("Année N : 2 500 000 €")
                it = st.number_input("Optimisation IT (€)", min_value=0, value=2500000, step=50000, disabled=manche_verrouillee)

        # Section 4: Formations
        with st.expander("🎓 4. Budgets Formations Collaborateurs (€)", expanded=False):
            f1, f2 = st.columns(2)
            with f1:
                st.caption("Année N — Réglementaire : 1 000 000 €")
                f_reg = st.number_input("Formation Réglementaire (€)", min_value=0, value=1000000, step=10000, disabled=manche_verrouillee)
                
                st.caption("Année N — Conquête : 900 000 €")
                f_conq = st.number_input("Formation Conquête (€)", min_value=0, value=900000, step=10000, disabled=manche_verrouillee)
                
                st.caption("Année N — Multi-vente : 650 000 €")
                f_multi = st.number_input("Formation Multi-vente (€)", min_value=0, value=650000, step=10000, disabled=manche_verrouillee)
            with f2:
                st.caption("Année N — Management : 800 000 €")
                f_mgmt = st.number_input("Formation Management (€)", min_value=0, value=800000, step=10000, disabled=manche_verrouillee)
                
                st.caption("Année N — Crédit : 500 000 €")
                f_cred = st.number_input("Formation Crédit (€)", min_value=0, value=500000, step=10000, disabled=manche_verrouillee)
                
                st.caption("Année N — Épargne : 800 000 €")
                f_epargne = st.number_input("Formation Épargne (€)", min_value=0, value=800000, step=10000, disabled=manche_verrouillee)

        # Section 5: Tarification
        with st.expander("📉 5. Tarification Clientèle (Taux, Packs & Assurances)", expanded=False):
            st.write("#### 🏦 Crédits (Taux offerts aux clients en %)")
            t1, t2 = st.columns(2)
            with t1:
                st.caption("Année N — Consommation : 6.00 %")
                tx_conso = st.number_input("Consommation (%)", min_value=0.0, max_value=20.0, value=6.00, step=0.05, disabled=manche_verrouillee)
                
                st.caption("Année N — Immobilier : 4.20 %")
                tx_immo = st.number_input("Immobilier (%)", min_value=0.0, max_value=20.0, value=4.20, step=0.05, disabled=manche_verrouillee)
            with t2:
                st.caption("Année N — Court terme Pro : 7.00 %")
                tx_ct_pro = st.number_input("Court terme Pro (%)", min_value=0.0, max_value=20.0, value=7.00, step=0.05, disabled=manche_verrouillee)
                
                st.caption("Année N — Moyen Terme Pro : 5.20 %")
                tx_mt_pro = st.number_input("Moyen Terme Pro (%)", min_value=0.0, max_value=20.0, value=5.20, step=0.05, disabled=manche_verrouillee)

            st.write("---")
            st.write("#### 📦 Produits et Services (Tarifs annuels des Packs en €)")
            p1, p2 = st.columns(2)
            with p1:
                st.caption("Année N — Pack Niv 1 : 80 €")
                pack_1 = st.number_input("Pack Niveau 1 (€)", min_value=0, value=80, disabled=manche_verrouillee)
                
                st.caption("Année N — Pack Niv 2 : 160 €")
                pack_2 = st.number_input("Pack Niveau 2 (€)", min_value=0, value=160, disabled=manche_verrouillee)
                
                st.caption("Année N — Pack Niv 3 : 240 €")
                pack_3 = st.number_input("Pack Niveau 3 (€)", min_value=0, value=240, disabled=manche_verrouillee)
            with p2:
                st.caption("Année N — Pack Pro 1 : 400 €")
                pack_pro1 = st.number_input("Pack Pro 1 (€)", min_value=0, value=400, disabled=manche_verrouillee)
                
                st.caption("Année N — Pack Pro 2 : 3 500 €")
                pack_pro2 = st.number_input("Pack Pro 2 (€)", min_value=0, value=3500, disabled=manche_verrouillee)

            st.write("---")
            st.write("#### 🛡️ Assurances (Cotisations annuelles en €)")
            a1, a2 = st.columns(2)
            with a1:
                st.caption("Année N — Auto Niv 1 : 75 €")
                auto_1 = st.number_input("Auto Niveau 1 (€)", min_value=0, value=75, disabled=manche_verrouillee)
                
                st.caption("Année N — Auto Niv 2 : 150 €")
                auto_2 = st.number_input("Auto Niveau 2 (€)", min_value=0, value=150, disabled=manche_verrouillee)
                
                st.caption("Année N — Prévoyance : 180 €")
                prev = st.number_input("Prévoyance (€)", min_value=0, value=180, disabled=manche_verrouillee)
            with a2:
                st.caption("Année N — MH Niv 1 (Habitation) : 75 €")
                mh_1 = st.number_input("MH Niveau 1 (€)", min_value=0, value=75, disabled=manche_verrouillee)
                
                st.caption("Année N — MH Niv 2 (Habitation) : 150 €")
                mh_2 = st.number_input("MH Niveau 2 (€)", min_value=0, value=150, disabled=manche_verrouillee)

            st.write("---")
            st.write("#### 💰 Épargne (Taux proposés aux clients)")
            e1, e2 = st.columns(2)
            with e1:
                st.caption("Année N — Livrets : 2.50 %")
                tx_livret = st.number_input("Livrets (%)", min_value=0.0, value=2.50, step=0.05, disabled=manche_verrouillee)
            with e2:
                st.caption("Année N — Structurés (tx de marge) : 2.80 %")
                tx_struct = st.number_input("Structurés (tx marge %)", min_value=0.0, value=2.80, step=0.05, disabled=manche_verrouillee)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 Soumettre les décisions de la banque", use_container_width=True, disabled=manche_verrouillee):
            st.balloons()
            st.success("✅ Vos décisions pour l'Année N+1 ont été enregistrées avec succès ! Prévenez le Maître du Jeu.")

    with onglet_bleu:
        st.write("### 🔵 Vos Comptes et Indicateurs de Rentabilité")
        st.info("Les tableaux de résultats de votre agence s'afficheront ici de manière dynamique dès que le Maître du Jeu aura calculé la clôture de la manche.")

    with onglet_jaune:
        st.write("### 🟡 Analyse et Positionnement sur le Marché")
        st.info("Retrouvez ici les graphiques comparatifs de vos parts de marché face aux banques concurrentes après la clôture de la manche.")
