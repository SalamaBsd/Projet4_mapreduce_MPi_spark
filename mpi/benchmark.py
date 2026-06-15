import subprocess
import csv
import time

python_path = "python"
script = "mpi/mapreduce.py"
data = "data/big_input.txt"

results = []
for n in [1, 2, 4]:
    start = time.time()
    subprocess.run(
        ["mpirun", "-n", str(n), python_path, script, data],
        capture_output=True
    )
    duration = round(time.time() - start, 3)
    results.append((n, duration))
    print(f"MPI avec {n} processus : {duration} secondes")

with open("results/bench_mpi.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["processus", "temps_secondes"])
    writer.writerows(results)

print("Benchmark sauvegardé dans results/bench_mpi.csv")