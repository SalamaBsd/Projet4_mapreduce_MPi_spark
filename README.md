Copie-colle exactement ce texte dans GitHub :


#  Mini Moteur MapReduce — MPI vs Apache Spark

Implementation of a mini MapReduce engine from scratch using Python and MPI (mpi4py), covering the three core phases: **Map**, **Shuffle**, and **Reduce**. Compared to Apache Spark (PySpark) on a WordCount benchmark.

> M2 — Parallel Programming & Distributed Systems



##  Objectif

Implémenter un moteur MapReduce parallèle avec MPI et comparer ses performances avec Apache Spark sur le problème WordCount.



##  Structure du projet
```

P4_mapreduce_project/
├── data/
│   ├── input.txt              ← Données de test (petit)
│   └── big_input.txt          ← Données de test (grand)
├── mpi/
│   ├── mapreduce.py           ← Map + Shuffle + Reduce avec MPI
│   └── benchmark.py           ← Benchmark MPI (1, 2, 4 processus)
├── spark/
│   ├── wordcount_spark.py     ← WordCount avec PySpark
│   └── benchmark_spark.py     ← Benchmark Spark
├── results/
│   ├── bench_mpi.csv          ← Temps d'exécution MPI
│   ├── bench_spark.csv        ← Temps d'exécution Spark
│   └── comparison.png         ← Graphique de comparaison
├── mapreduce_project.ipynb    ← Notebook principal
└── TP_guide_installation.md   ← Guide d'installation complet

```


##  Installation

### Cloner le projet
```bash
git clone https://github.com/SalamaBsd/Projet4_mapreduce_MPi_spark.git
cd Projet4_mapreduce_MPi_spark
```

### Installer les dépendances système
```bash
sudo apt update
sudo apt install -y python3 python3-pip openmpi-bin libopenmpi-dev default-jdk
```

### Créer l'environnement virtuel
```bash
python3 -m venv venv
source venv/bin/activate
pip install mpi4py pyspark matplotlib jupyter pandas --timeout 120
```

### Créer le lien symbolique (important pour MPI)
```bash
ln -s "/mnt/c/Users/TonNom/Desktop/Projet4_mapreduce_MPi_spark" ~/proj
cd ~/proj
source venv/bin/activate
```

>  Remplace `TonNom` par ton nom d'utilisateur Windows

---

##  Exécution

### Lancer MPI avec 4 processus
```bash
mpirun -n 4 python mpi/mapreduce.py data/big_input.txt
```

### Lancer Jupyter Notebook
```bash
jupyter notebook
```
Ouvre `mapreduce_project.ipynb` et exécute les cellules avec `Shift + Enter`.

---

##  Résultats

| Outil | Temps |
|---|---|
| MPI 1 processus | ~0.83s |
| MPI 2 processus | ~1.08s |
| MPI 4 processus | ~1.15s |
| Spark (big file) | ~5.32s |

---

##  Technologies

![Python](https://img.shields.io/badge/Python-3.12-blue)
![MPI](https://img.shields.io/badge/MPI-OpenMPI-teal)
![Spark](https://img.shields.io/badge/Apache-Spark-orange)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![WSL2](https://img.shields.io/badge/WSL2-Ubuntu_24.04-purple)
```
