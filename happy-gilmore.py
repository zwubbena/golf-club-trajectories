# ==========================================
# Happy Gilmore: 
# Golf Ball Trajectory Visualizations
# ==========================================

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import FileLink, display

# ---- CONFIGURATION ----
# List of clubs with (Name, Carry Distance in Yards, Apex Height in Feet)
clubs = [
    ("Driver", 230, 80),
    ("3-Wood", 215, 85),
    ("5-Iron", 180, 90),
    ("7-Iron", 160, 100),
    ("9-Iron", 140, 110),
    ("Pitching Wedge", 120, 115),
    ("Sand Wedge", 100, 120),
    ("Lob Wedge", 80, 125),
]

# Assign colors: Red = longest (driver), Green = shortest (lob wedge), Gray = others
colors = ["red"] + ["gray"] * (len(clubs) - 2) + ["green"]

# Shared horizontal range (distance in yards)
x_vals = np.linspace(0, 250, 500)

# ==============================
# Plot 1: Standard Trajectory Chart
# ==============================
fig1, ax1 = plt.subplots(figsize=(12, 6))

for (club, distance, apex_height), color in zip(clubs, colors):
    mid = distance / 2
    height_vals = apex_height * (1 - ((x_vals - mid) ** 2) / (mid ** 2))
    height_vals = np.clip(height_vals, 0, None)
    ax1.plot(x_vals, height_vals, label=f"{club} ({distance} yds)", color=color)

# Flagstick at 240 yards
ax1.axvline(x=240, color="black", linestyle="--", alpha=0.6)
ax1.text(240, 5, "Flagstick", rotation=90, verticalalignment='bottom', horizontalalignment='right')

# Styling
ax1.set_title("Golf Ball Trajectory by Club Type", fontsize=14)
ax1.set_xlabel("Distance (Yards)")
ax1.set_ylabel("Height (Feet)")
ax1.set_xlim(0, 250)
ax1.set_ylim(0, 140)
ax1.grid(True, linestyle='--', alpha=0.4)
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()

# Save and display download link
file1 = "golf_ball_trajectory_by_club_type.png"
fig1.savefig(file1, format='png', dpi=300)
display(FileLink(file1))

# ==============================
# Plot 2: Trajectory with Carry Zones
# ==============================
fig2, ax2 = plt.subplots(figsize=(12, 6))

for (club, distance, apex_height), color in zip(clubs, colors):
    mid = distance / 2
    height_vals = apex_height * (1 - ((x_vals - mid) ** 2) / (mid ** 2))
    height_vals = np.clip(height_vals, 0, None)
    ax2.plot(x_vals, height_vals, label=f"{club} ({distance} yds)", color=color)

# Shaded carry zones
ax2.axvspan(70, 130, color='green', alpha=0.1, label='Zone A: Wedges')
ax2.axvspan(130, 170, color='blue', alpha=0.1, label='Zone B: Short–Mid Irons')
ax2.axvspan(170, 210, color='orange', alpha=0.1, label='Zone C: Long Irons/FW')
ax2.axvspan(210, 250, color='red', alpha=0.1, label='Zone D: Driver Zone')

# Flagstick
ax2.axvline(x=240, color="black", linestyle="--", alpha=0.6)
ax2.text(240, 5, "Flagstick", rotation=90, verticalalignment='bottom', horizontalalignment='right')

# Styling
ax2.set_title("Golf Ball Trajectory by Club Type with Carry Zones", fontsize=14)
ax2.set_xlabel("Distance (Yards)")
ax2.set_ylabel("Height (Feet)")
ax2.set_xlim(0, 250)
ax2.set_ylim(0, 140)
ax2.grid(True, linestyle='--', alpha=0.4)
ax2.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()

# Save and generate download link
file2 = "golf_ball_trajectory_with_carry_zones.png"
fig2.savefig(file2, format='png', dpi=300)
display(FileLink(file2))
