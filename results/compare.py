import csv
import matplotlib.pyplot as plt

# Lire bench_mpi.csv
mpi_procs = []
mpi_times = []
with open("results/bench_mpi.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        mpi_procs.append(int(row["processus"]))
        mpi_times.append(float(row["temps_secondes"]))

# Temps Spark (big_input)
spark_time = 5.317

# Graphique
plt.figure(figsize=(10, 6))
plt.plot(mpi_procs, mpi_times, 'o-', color='purple', label='MPI (big_input)')
plt.axhline(y=spark_time, color='orange', linestyle='--', label=f'Spark (big_input) = {spark_time}s')
plt.xlabel("Nombre de processus MPI")
plt.ylabel("Temps (secondes)")
plt.title("Comparaison MPI vs Spark — WordCount")
plt.legend()
plt.grid(True)
plt.xticks([1, 2, 4])
plt.savefig("results/comparison.png")
plt.show()
print(" Graphique sauvegardé dans results/comparison.png")