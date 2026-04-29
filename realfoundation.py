import streamlit as st
import numpy as np

# ------------------ CSS ------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    font-size: 32px;
    font-weight: bold;
    color: #1f4e79;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}
.result {
    font-size: 20px;
    color: #0a7d5e;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Title ------------------
st.markdown('<div class="title">Pile Foundation Design (Eccentric Load - Terzaghi)</div>', unsafe_allow_html=True)

# ------------------ Input ------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

P = st.number_input("Axial Load P (kN)", value=1000.0)
M = st.number_input("Moment M (kN-m)", value=200.0)

n = st.number_input("Number of Piles", value=4)

c = st.number_input("Cohesion c (kPa)", value=25.0)
gamma = st.number_input("Unit Weight γ (kN/m³)", value=18.0)
Df = st.number_input("Foundation Depth Df (m)", value=1.5)
B = st.number_input("Footing Width B (m)", value=2.0)

Nc = st.number_input("Nc", value=30.0)
Nq = st.number_input("Nq", value=18.0)
Ng = st.number_input("Nγ", value=15.0)

st.markdown('</div>', unsafe_allow_html=True)

# ------------------ Calculation ------------------

# Terzaghi Bearing Capacity
qu = c*Nc + gamma*Df*Nq + 0.5*gamma*B*Ng

# Pile coordinates (สมมติเป็นสี่เหลี่ยม)
x = np.array([-1, 1, -1, 1])
y = np.array([-1, -1, 1, 1])

sum_x2 = np.sum(x**2)

# Load per pile
Qi = (P / n) + (M * x / sum_x2)

# ------------------ Output ------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown(f'<div class="result">Ultimate Bearing Capacity (qu) = {qu:.2f} kPa</div>', unsafe_allow_html=True)

for i, q in enumerate(Qi):
    st.write(f"Pile {i+1} Load = {q:.2f} kN")

if max(Qi) > qu:
    st.error("❌ Foundation NOT SAFE")
else:
    st.success("✅ Foundation SAFE")

st.markdown('</div>', unsafe_allow_html=True)
