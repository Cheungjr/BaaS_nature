import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.array([
    [8, 13, 6, 5, 6, 4],
    [0, 4, 7, 4, 7, 2],
    [0, 0, 11, 3, 4, 5],
    [0, 0, 0, 9, 2, 3],
    [0, 0, 0, 0, 6, 2],
    [0, 0, 0, 0, 0, 9]
])

# label
latest_age_labels = ["<20", "20-30", "30-40", "40-50", "50-60", "60+"]

# heatmap
mask_updated = np.zeros_like(data, dtype=bool)
for i in range(mask_updated.shape[0]):
    for j in range(mask_updated.shape[1]):
        if i > j:
            mask_updated[i, j] = True

# mask
plt.figure(figsize=(8, 6))
sns.heatmap(data, annot=True, cmap="YlGnBu", xticklabels=latest_age_labels, yticklabels=latest_age_labels, mask=mask_updated)
plt.title('Heatmap of Order Volume with vs. without BaaS')
plt.xlabel('Order Volume Using BaaS')
plt.ylabel('Order Volume Without BaaS')
plt.savefig("survey_heatmap.png")  # save img
plt.show()
