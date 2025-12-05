# analysis.py
# Author: Dhyey Pithadia
# Contact (required by grader): 23f2001472@ds.study.iitm.ac.in
#
# This Marimo notebook demonstrates:
#  - cell dependencies (variables created in earlier cells used later)
#  - an interactive slider widget
#  - dynamic markdown output that updates when the slider changes
#  - comments documenting the dataflow between cells

# %% cell 1
# Create a simple dataset and expose it to downstream cells.
# Dataflow: cell 2 and cell 3 depend on `x` and `y`.
import numpy as np

# x and y are the base variables for the notebook
x = np.linspace(0, 10, 200)
y = np.sin(x) + 0.5 * np.cos(2 * x)

# Small helper: combine into a 2D array for convenience downstream
data = np.column_stack((x, y))

# %% cell 2
# Create an interactive slider to choose the smoothing window size.
# Dataflow: this cell defines `window_size` which is used in cell 3 to compute a smoothed series.
import marimo as mo

# Slider: integer range [1, 20]. This is an interactive widget.
window_slider = mo.ui.slider(1, 20, value=3, description="Smoothing window")

# Expose a plain int for downstream use
window_size = window_slider.value

# Show the slider widget in the notebook UI (Marimo displays widgets automatically,
# but we call mo.ui to keep intent explicit). Downstream cells will re-run when
# `window_size` changes because Marimo tracks reactive dependencies.
window_slider

# %% cell 3
# Use variables from cell 1 (`x`, `y`) and cell 2 (`window_size`) to compute smoothed output.
# Dataflow: depends on x,y,window_size.
import numpy as np
import matplotlib.pyplot as plt

def moving_average(arr, w):
    if w <= 1:
        return arr
    # simple uniform moving average (centered)
    pad = w // 2
    padded = np.pad(arr, (pad, pad), mode="edge")
    kernel = np.ones(w) / w
    return np.convolve(padded, kernel, mode="valid")[: len(arr)]

# compute smoothed y using the selected window
smoothed_y = moving_average(y, window_size)

# Dynamic markdown: shows current widget state and a short summary.
mo.md(f"### Interactive smoothing\n- **Window size**: {window_size}\n- **Data points**: {len(x)}\n")

# Plot: shows original vs smoothed. Marimo will render matplotlib output in the notebook.
plt.figure(figsize=(8, 3.5))
plt.plot(x, y, label="Original", alpha=0.5)
plt.plot(x, smoothed_y, label=f"Smoothed (w={window_size})", linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()

# %% cell 4 (optional)
# Additional dynamic summary that depends on smoothed_y.
# Dataflow: depends on smoothed_y produced in cell 3.
mean_val = float(np.mean(smoothed_y))
std_val = float(np.std(smoothed_y))

mo.md(f"**Smoothed series stats** — mean: {mean_val:.4f}, std: {std_val:.4f}")
