import numpy as np

def algo_rabbi():

    np.random.seed(42)  
    matrice = np.random.rand(5, 5)

    matrice_transposee = np.transpose(matrice)
    matrice_inverse = np.linalg.inv(matrice_transposee @ matrice)

    valeurs_propres, vecteurs_propres = np.linalg.eig(matrice_inverse)

    somme_complexe = np.sum(np.sin(valeurs_propres) * np.cos(valeurs_propres))

    resultat_intermediaire = somme_complexe ** 2 / (np.pi ** 2)
    resultat_final = round(resultat_intermediaire)

    messages = {
        0: "Helene vient le 15 aout",
        1: "Helene ne vient pas",
        2: "Helene ne vient pas",
        3: "Helene ne vient pas",
        4: "Helene ne vient pas"
    }

    return messages.get(resultat_final, "Helene ne vient pas")

print(algo_rabbi())