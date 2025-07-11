
import json
import os
import config
import statistics
import numpy as np
import matplotlib.pyplot as plt

ALL_CONFIGS = set(config.VARYING_CONST + config.VARYING_WEIGHT)

files = [file for file in os.listdir("results_original/results") if "_e50_err0" in file]

# Group disagreement values by config
disagreement_by_config = {config: [] for config in ALL_CONFIGS}

for file in files:
    for config in ALL_CONFIGS:
        if f"_{config}_" in f"_{file}_":  # to match exactly like "_c1p1t1_"
            with open(os.path.join("results_original/results", file)) as json_file:
                data = json.load(json_file)
                disagreements = data["median_disagreements"]
                disagreement_by_config[config].extend(disagreements)


# Compute median disagreement for each config
median_disagreements = {}
iqr_disagrements = {}

for config, disagreements in disagreement_by_config.items():
    median_disagreements[config] = statistics.median(disagreements)

sorted_medians = sorted(median_disagreements.items(), key=lambda x: x[1])

print("Median Disagreement:")
for config, value in sorted_medians:
    print(f"{config}: {value}")

print("\n\n")
for config, medians in disagreement_by_config.items():
    q1 = np.percentile(medians, 25)
    q3 = np.percentile(medians, 75)
    iqr = q3-q1
    iqr_disagrements[config] = iqr

print("IQR:")
sorted_iqr = sorted(iqr_disagrements.items(), key=lambda x: x[1])
for config, value in sorted_iqr:
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


import json
import os
import config
import statistics
import numpy as np
import matplotlib.pyplot as plt

ALL_CONFIGS = set(config.VARYING_CONST + config.VARYING_WEIGHT)

files = [file for file in os.listdir("results_original/results") if "_e50_err0" in file]

# Group disagreement values by config
disagreement_by_config = {config: [] for config in ALL_CONFIGS}

for file in files:
    for config in ALL_CONFIGS:
        if f"_{config}_" in f"_{file}_":  # to match exactly like "_c1p1t1_"
            with open(os.path.join("results_original/results", file)) as json_file:
                data = json.load(json_file)
                disagreements = data["median_disagreements"]
                disagreement_by_config[config].extend(disagreements)


# Compute median disagreement for each config
median_disagreements = {}
iqr_disagrements = {}

for config, disagreements in disagreement_by_config.items():
    median_disagreements[config] = statistics.median(disagreements)

sorted_medians = sorted(median_disagreements.items(), key=lambda x: x[1])

print("Median Disagreement:")
for config, value in sorted_medians:
    print(f"{config}: {value}")

print("\n\n")
for config, medians in disagreement_by_config.items():
    q1 = np.percentile(medians, 25)
    q3 = np.percentile(medians, 75)
    iqr = q3-q1
    iqr_disagrements[config] = iqr

print("IQR:")
sorted_iqr = sorted(iqr_disagrements.items(), key=lambda x: x[1])
for config, value in sorted_iqr:
    print(f"{config}: {value}")


import matplotlib.pyplot as plt

# Extract data for plotting
median_configs = [item[0] for item in sorted_medians]
median_values = [item[1] for item in sorted_medians]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot Median Disagreement
ax1.plot(median_configs, median_values, marker='o', linestyle='-', color='black', linewidth=2, markersize=6)
for i, val in enumerate(median_values):
    ax1.text(i, val + 1, f"{val:.1f}", ha='center', va='bottom', fontsize=9)
ax1.set_ylabel("Median Disagreement")
ax1.set_title("Median Disagreement by Constraint Configuration")
ax1.grid(True, axis='y', linestyle='--', linewidth=0.5)

# Extract data for IQR
iqr_configs = [item[0] for item in sorted_iqr]
iqr_values = [item[1] for item in sorted_iqr]

plt.figure(figsize=(10, 4))

# Plot line with markers
plt.plot(iqr_configs, iqr_values, marker='o', linestyle='-', color='darkblue', linewidth=2, markersize=6)

# Add value annotations
for i, (config, val) in enumerate(zip(iqr_configs, iqr_values)):
    plt.text(i, val + 1, f"{val:.1f}", ha='center', va='bottom', fontsize=9)

plt.ylabel("IQR of Disagreement")
plt.xlabel("Constraint Configuration")

plt.title("IQR of Disagreement by Constraint Configuration")

plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.savefig("results/constraint_iqr_disagreement_plot.pdf")
plt.show()
plt.close()




