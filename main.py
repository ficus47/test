import cv2
import streamlit as st

def prendre_photo(nom_fichier):
    # Ouvrir la webcam (0 est l'ID par défaut de la webcam)
    cap = cv2.VideoCapture(0)

    # Vérifier si la webcam s'est ouverte correctement
    if not cap.isOpened():
        print("Erreur : Impossible d'ouvrir la webcam")
        return

    # Lire une frame de la webcam
    ret, frame = cap.read()

    if ret:
        # Sauvegarder l'image capturée
        cv2.imwrite(nom_fichier, frame)
        print(f"Photo prise et enregistrée sous {nom_fichier}")
    else:
        print("Erreur : Impossible de capturer l'image")

    # Libérer les ressources
    cap.release()
    cv2.destroyAllWindows()

# Exemple d'utilisation de la fonction
prendre_photo('photo.jpg')
st.image("photo.jpg")
