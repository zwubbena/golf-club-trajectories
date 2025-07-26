# Golf Club Trajectory Visualizations

This Python script visualizes typical golf ball flight paths and carry distances by club type. Two visualizations are produced:

1. **Standard Trajectory Plot** – Shows the height and distance for 8 common golf clubs.
2. **Trajectory Plot with Carry Zones** – Adds shaded distance bands to group clubs by typical carry ranges (Wedges, Irons, Fairway Woods, Driver).

Both visualizations are generated in Google Colab and exported as high-resolution PNG images.

---

## Key Features

- **Illustrative trajectories** for 8 club types:
  - Driver, 3-Wood, 5-Iron, 7-Iron, 9-Iron
  - Pitching Wedge, Sand Wedge, Lob Wedge
- **Realistic apex heights and distances**
- **Color-coded lines**:
  - 🔴 Red = Longest club (Driver)
  - 🟢 Green = Shortest club (Lob Wedge)
  - ⚪ Gray = All others
- **Carry zones overlaid** to visually segment:
  - Zone A (70–130 yds): Wedges
  - Zone B (130–170 yds): Short–Mid Irons
  - Zone C (170–210 yds): Long Irons / Fairway Woods
  - Zone D (210–250 yds): Driver

---

## Output Files

The following PNG files are generated:

- `golf_ball_trajectory_by_club_type.png`
- `golf_ball_trajectory_with_carry_zones.png`

Both are available for download within the Colab notebook after execution.

---

## How It Works

Each club’s flight path is modeled with a simple parabolic formula:

```math
\text{height}(x) = \text{apex} \cdot \left(1 - \frac{(x - \text{midpoint})^2}{\text{midpoint}^2}\right)

This approximates the natural arc of a ball in flight, from launch to landing.

---

## Getting Started

1. Open the Colab notebook.
2. Run all cells to generate the visualizations.
3. Visualizations should be generated inline at the end of the script. 
4. Download the PNG files using the provided download links.

---

# Enjoy! 
