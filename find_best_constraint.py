import json
import os
import config
import statistics
import matplotlib.pyplot as plt

ALL_CONFIGS = set(config.VARYING_CONST + config.VARYING_WEIGHT)

files = [file for file in os.listdir("results") if "_e50_err0" in file]

# Group disagreement values by config
disagreement_by_config = {config: [] for config in ALL_CONFIGS}

for file in files:
    for config in ALL_CONFIGS:
        if f"_{config}_" in f"_{file}_":  # to match exactly like "_c1p1t1_"
            with open(os.path.join("results", file)) as json_file:
                data = json.load(json_file)
                disagreements = data["median_disagreements"]
                disagreement_by_config[config].extend(disagreements)

# Compute median disagreement for each config
median_disagreements = {}

for config, disagreements in disagreement_by_config.items():
    median_disagreements[config] = statistics.median(disagreements)

sorted_medians = sorted(median_disagreements.items(), key=lambda x: x[1])

for config, value in sorted_medians:
    print(f"{config}: {value}")


# Extract data
configs = [item[0] for item in sorted_medians]
values = [item[1] for item in sorted_medians]

plt.figure(figsize=(10, 4))

# Plot line with markers
plt.plot(configs, values, marker='o', linestyle='-', color='black', linewidth=2, markersize=6)

# Add value annotations
for i, (config, val) in enumerate(zip(configs, values)):
    plt.text(i, val + 1, f"{val:.1f}", ha='center', va='bottom', fontsize=9)

plt.ylabel("Median Disagreement")
plt.xlabel("Constraint Configuration")

plt.title("Median Disagreement by Constraint Configuration")

plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.savefig("results/constraint_median_disagreement_plot.pdf")
plt.show()
plt.close()

