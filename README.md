# Happy Gilmore
##Golf Club Trajectory Visualizations

This Python script visualizes typical golf ball flight paths and approximate carry distances by club type. Two visualizations are produced:

1. **Standard Trajectory Plot** – Shows the height (vertical trajectory) and distance (yardage) for 8 common types of golf clubs.
2. **Trajectory Plot with Shaded Carry Zones** – Adds shaded distance bands to group clubs by typical carry zones to show ideal distance ranges (Wedges, Irons, Fairway Woods, Driver).

Both visualizations are generated in Google Colab and exported as high-resolution PNG images.

---

## Key Features

- **Illustrative trajectories** for 8 club types:
  - Driver
  - 3-Wood
  - 5-Iron
  - 7-Iron
  - 9-Iron
  - Pitching Wedge
  - Sand Wedge
  - Lob Wedge
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

## How It Works

Each club’s flight path is modeled with a parabolic equation:

![Trajectory Formula](https://latex.codecogs.com/svg.image?\dpi{150}&space;\text{height}(x)&space;=&space;\text{apex}&space;\cdot&space;\left(1&space;-&space;\frac{(x&space;-&space;\text{midpoint})^2}{\text{midpoint}^2}\right))

The following variables define the parameters of this equation.

### 🔍 Variable Definitions

| Variable      | Definition                                                                 |
|---------------|------------------------------------------------------------------------------|
| `height(x)`   | Height of the golf ball (in feet) at a given horizontal position `x`.        |
| `x`           | Horizontal distance (in yards) from the starting point of the shot.          |
| `apex`        | Maximum height (in feet) reached by the ball at the peak of its trajectory.  |
| `midpoint`    | Horizontal midpoint (in yards) of the ball's carry, calculated as `distance / 2`. |

This equation produces a symmetric parabolic arc that peaks at the midpoint of the carry distance and returns to ground level at the expected landing point to essentially approximate the natural arc of a ball in flight, from launch to landing.

---

## Getting Started

1. Open the Colab notebook
2. Run all cells to generate the visualizations
3. Visualizations should be generated inline at the end of the script

---

## Output Files

The following PNG files are generated for download:

- `golf_ball_trajectory_by_club_type.png`
- `golf_ball_trajectory_with_carry_zones.png`

Both are available for download within the Colab notebook after execution.

---

# "So long, sucker!"
