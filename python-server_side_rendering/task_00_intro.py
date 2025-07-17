import os 

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Erreur : Le modèle (template) doit être une chaîne de caractères.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Erreur : La liste des invités doit être une liste de dictionnaires.")
        return

    if template.strip() == "":
        print("Template est vide, aucun fichier généré.")
        return

    if len(attendees) == 0:
        print("Aucune donnée fournie, aucun fichier généré.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        invitation_text = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"

            invitation_text = invitation_text.replace(f"{{{key}}}", str(value))
        filename = f"output_{idx}.txt" 
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(invitation_text)
        except Exception as e:
            print(f"Erreur lors de l'écriture du fichier {filename} : {e}")
