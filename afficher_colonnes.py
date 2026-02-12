import os
import pandas as pd

# Chemin vers le dossier 2012
dossier_2012 = r"c:\Users\matte\Desktop\dataset_mspr\recensement\2012"

# Lister tous les fichiers XLS
fichiers = [f for f in os.listdir(dossier_2012) if f.endswith('.xls')]

print("=" * 80)
print("COLONNES DE CHAQUE FICHIER - RECENSEMENT 2012")
print("=" * 80)

for fichier in sorted(fichiers):
    chemin_fichier = os.path.join(dossier_2012, fichier)
    print(f"\n📄 {fichier}")
    print("-" * 80)
    
    try:
        # Lire le fichier XLS avec les colonnes à la ligne 11
        df = pd.read_excel(chemin_fichier, sheet_name=0, header=10)
        colonnes = df.columns.tolist()
        
        print(f"Nombre de colonnes : {len(colonnes)}")
        print(f"Nombre de lignes : {len(df)}\n")
        print("Colonnes :")
        for i, col in enumerate(colonnes, 1):
            print(f"  {i:2d}. {col}")
            
    except Exception as e:
        print(f"⚠️  Erreur lors de la lecture : {e}")

print("\n" + "=" * 80)
