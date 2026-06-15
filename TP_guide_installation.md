# TP — Mini Moteur MapReduce : MPI vs Apache Spark
## Guide d'installation et d'exécution complet

---

## ÉTAPE 1 — Installer WSL2 (Ubuntu sur Windows)

Ouvre **PowerShell en tant qu'administrateur** et tape :
```powershell
wsl --install
```

Si tu as une erreur réseau, installe Ubuntu via le **Microsoft Store** :
1. Ouvre Microsoft Store
2. Recherche **Ubuntu 24.04**
3. Clique sur **Installer** puis **Ouvrir**
4. Crée ton nom d'utilisateur et mot de passe Linux

> ⚠️ Quand tu tapes le mot de passe, rien ne s'affiche — c'est normal !

---

## ÉTAPE 2 — Mettre à jour Ubuntu

Dans le terminal Ubuntu :
```bash
sudo apt update
```

---

## ÉTAPE 3 — Installer Python, pip et les outils système

```bash
sudo apt install -y python3 python3-pip mpich
```

---

## ÉTAPE 4 — Remplacer MPICH par OpenMPI

MPICH ne fonctionne pas bien sur WSL. Il faut utiliser OpenMPI :
```bash
sudo apt remove mpich -y
sudo apt install openmpi-bin libopenmpi-dev -y
```

---

## ÉTAPE 5 — Installer Java (requis pour Spark)

```bash
sudo apt install default-jdk -y
```

Vérifier :
```bash
java -version
```

---

## ÉTAPE 6 — Aller dans le dossier du projet

Remplace `TonNom` par ton nom d'utilisateur Windows :
```bash
cd "/mnt/c/Users/TonNom/Desktop/P4_mapreduce_project"
```

---

## ÉTAPE 7 — Créer l'environnement virtuel Python

```bash
python3 -m venv venv
source venv/bin/activate
```

> Tu dois voir `(venv)` apparaître devant ton terminal.

---

## ÉTAPE 8 — Installer les dépendances Python

```bash
pip install mpi4py pyspark
pip install matplotlib --timeout 120
pip install jupyter pandas --timeout 120
```

Vérifier :
```bash
python -c "from mpi4py import MPI; print('MPI OK')"
python -c "import pyspark; print('Spark OK')"
```

---

## ÉTAPE 9 — Créer un lien symbolique pour MPI

MPI ne fonctionne pas depuis `/mnt/c/` (chemin Windows avec espaces).
On crée un raccourci dans le home Linux :
```bash
ln -s "/mnt/c/Users/TonNom/Desktop/P4_mapreduce_project" ~/proj
cd ~/proj
source venv/bin/activate
```

---

## ÉTAPE 10 — Tester MPI

```bash
mpirun -n 4 python mpi/mapreduce.py data/big_input.txt
```

Tu dois voir les 4 processus travailler en parallèle :
```
[MAP] Processus 0 : 4 mots uniques
[MAP] Processus 1 : 5 mots uniques
[MAP] Processus 2 : 4 mots uniques
[MAP] Processus 3 : 5 mots uniques
[SHUFFLE] ...
[REDUCE] ...
✅ TERMINÉ
```

---

## ÉTAPE 11 — Lancer Jupyter Notebook

```bash
cd ~/proj
source venv/bin/activate
jupyter notebook
```

Ouvre le lien `http://localhost:8888/...` dans ton navigateur.
Clique sur **mapreduce_project.ipynb** et exécute les cellules avec `Shift + Enter`.

---

## Résumé — Toutes les commandes en ordre

```bash
# 1. Mettre à jour Ubuntu
sudo apt update

# 2. Installer les outils
sudo apt install -y python3 python3-pip
sudo apt remove mpich -y
sudo apt install -y openmpi-bin libopenmpi-dev
sudo apt install -y default-jdk

# 3. Aller dans le projet (remplace TonNom)
cd "/mnt/c/Users/TonNom/Desktop/P4_mapreduce_project"

# 4. Créer le venv et installer les dépendances
python3 -m venv venv
source venv/bin/activate
pip install mpi4py pyspark
pip install matplotlib --timeout 120
pip install jupyter pandas --timeout 120

# 5. Créer le lien symbolique (remplace TonNom)
ln -s "/mnt/c/Users/TonNom/Desktop/P4_mapreduce_project" ~/proj
cd ~/proj
source venv/bin/activate

# 6. Tester MPI
mpirun -n 4 python mpi/mapreduce.py data/big_input.txt

# 7. Lancer Jupyter
jupyter notebook : Executer les cellules et compare MPI (mpi4py) et Apache Spark (PySpark) sur le problème WordCount.
```

---

## Structure du projet

```
P4_mapreduce_project/
├── data/
│   ├── input.txt
│   └── big_input.txt
├── mpi/
│   ├── mapreduce.py
│   └── benchmark.py
├── spark/
│   ├── wordcount_spark.py
│   └── benchmark_spark.py
├── results/
│   ├── bench_mpi.csv
│   ├── bench_spark.csv
│   └── comparison.png
└── mapreduce_project.ipynb
```

---

## En cas de problème

**pip timeout lors du téléchargement :**
```bash
pip install <package> --timeout 120
```

**MPI affiche seulement Processus 0 :**
```bash
sudo apt remove mpich -y
sudo apt install openmpi-bin libopenmpi-dev -y
pip install --force-reinstall mpi4py
```

**Java non trouvé pour Spark :**
```bash
sudo apt install default-jdk -y
```

**Erreur "No such file or directory" avec mpirun :**
Le chemin contient des espaces — utilise le lien symbolique :
```bash
ln -s "/mnt/c/Users/TonNom/Desktop/P4_mapreduce_project" ~/proj
cd ~/proj
```
