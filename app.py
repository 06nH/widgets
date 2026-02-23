import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 1. Setup Page and Sliders
st.title("Interactive I-Profile Section")
st.sidebar.header("Parameters (mm)")

h = st.sidebar.slider("Total Height (H)", 50, 500, 200)
w = st.sidebar.slider("Flange Width (W)", 50, 300, 150)
tf = st.sidebar.slider("Flange Thickness (tf)", 5, 50, 15)
tw = st.sidebar.slider("Web Thickness (tw)", 5, 50, 10)

# 2. Calculations
# Area = (2 * Flange Area) + (Web Area)
area = (2 * w * tf) + ((h - 2 * tf) * tw)

# 3. Drawing the Profile
fig, ax = plt.subplots(figsize=(6, 8))

# Define the coordinates for the three rectangles
# Bottom Flange: (x, y), width, height
bottom_flange = patches.Rectangle((-w/2, 0), w, tf, color="skyblue", ec="black")
# Web: Centered at x=0
web = patches.Rectangle((-tw/2, tf), tw, h - 2*tf, color="skyblue", ec="black")
# Top Flange
top_flange = patches.Rectangle((-w/2, h - tf), w, tf, color="skyblue", ec="black")

# Add patches to plot
ax.add_patch(bottom_flange)
ax.add_patch(web)
ax.add_patch(top_flange)

# 4. Dimension Lines & Annotations
# Height Label
ax.annotate('', xy=(w/2 + 20, 0), xytext=(w/2 + 20, h),
            arrowprops=dict(arrowstyle='<->', color='red'))
ax.text(w/2 + 25, h/2, f'H: {h}mm', color='red', va='center')

# Width Label
ax.annotate('', xy=(-w/2, h + 20), xytext=(w/2, h + 20),
            arrowprops=dict(arrowstyle='<->', color='green'))
ax.text(0, h + 30, f'W: {w}mm', color='green', ha='center')

# Thickness Labels
ax.text(-w/2 + 5, tf/2, f'tf: {tf}', fontsize=8, va='center')
ax.text(0, h/2, f'tw: {tw}', fontsize=8, ha='center', backgroundcolor="white")

# Plot Formatting
ax.set_xlim(-w - 50, w + 100)
ax.set_ylim(-50, h + 100)
ax.set_aspect('equal')
ax.axis('off')

# 5. Display Results
st.pyplot(fig)
st.metric("Total Cross-Sectional Area", f"{area:,} mm²")
