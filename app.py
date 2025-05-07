import streamlit as st
from solver import WaterJugSolver
import time

st.set_page_config(page_title="💧 AI Water Jug Solver", layout="wide")

st.markdown(
    """
    <style>
        .step-box {
            padding: 1rem;
            margin-bottom: 0.5rem;
            border-radius: 10px;
            background-color: #f0f2f6;
            border-left: 5px solid #6c63ff;
            font-size: 1.1rem;
            color: black; /* ✅ Make text black */
        }
        .end-box {
            background-color: #d1f3d1;
            border-left: 5px solid #2ecc71;
        }
    </style>
    """, unsafe_allow_html=True
)


st.title("💧 AI-based Water Jug Problem Solver")
st.write("Solve the classic **Water Jug Problem** using Artificial Intelligence search techniques like A*, BFS, and DFS.")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    jug1 = st.slider("Jug 1 Capacity", min_value=1, max_value=10, value=4)
    jug2 = st.slider("Jug 2 Capacity", min_value=1, max_value=10, value=3)
    target = st.slider("Target Amount", min_value=1, max_value=10, value=2)
    algo = st.radio("🔍 Search Algorithm", ["A*", "BFS", "DFS"])
    visualize = st.checkbox("📽️ Animate Steps")
    solve_button = st.button("🚀 Solve Now")

if solve_button:
    st.subheader("🧪 Solving Problem...")
    solver = WaterJugSolver(jug1, jug2, target)

    with st.spinner(f"Running {algo} algorithm..."):
        if algo == "BFS":
            path = solver.bfs()
        elif algo == "DFS":
            path = solver.dfs()
        else:
            path = solver.a_star()

    if not path:
        st.error("❌ No solution found. Try changing the target or jug capacities.")
    else:
        st.success(f"✅ Solution found in {len(path) - 1} steps!")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric("🔢 Steps", len(path) - 1)
            st.metric("🎯 Target Achieved", f"{target} Liters")
            st.metric("🧠 Algorithm", algo)
        with col2:
            st.write("### 🪜 Solution Path:")

            container = st.container()
            if visualize:
                for i, (x, y) in enumerate(path):
                    css_class = "step-box end-box" if i == len(path) - 1 else "step-box"
                    container.markdown(f"""
                        <div class="{css_class}">Step {i}: Jug 1 = {x}L, Jug 2 = {y}L</div>
                    """, unsafe_allow_html=True)
                    time.sleep(0.5)
            else:
                for i, (x, y) in enumerate(path):
                    css_class = "step-box end-box" if i == len(path) - 1 else "step-box"
                    container.markdown(f"""
                        <div class="{css_class}">Step {i}: Jug 1 = {x}L, Jug 2 = {y}L</div>
                    """, unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Solution",
            data="\n".join([f"Step {i}: Jug1 = {x}L, Jug2 = {y}L" for i, (x, y) in enumerate(path)]),
            file_name="water_jug_solution.txt",
            mime="text/plain"
        )
