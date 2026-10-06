import streamlit as st

# =========================
# DATA USER
# =========================

users = {
    "fani": "12345",
    "DC": "54321"
}

# =========================
# LOGIN
# =========================

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    st.title("🔐 Login Delivery Control")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username in users and users[username] == password:
            st.session_state.login = True
            st.session_state.user = username
            st.rerun()

        else:
            st.error("Username atau Password salah")

# =========================
# DASHBOARD
# =========================

else:

    st.title("🚚 DELIVERY CONTROL")

    st.success(
        f"Selamat datang {st.session_state.user}"
    )

    plan = st.number_input(
        "Plan Delivery",
        min_value=0
    )

    actual = st.number_input(
        "Actual Delivery",
        min_value=0
    )

    if plan > 0:

        progress = actual / plan

        st.metric(
            "Progress",
            f"{progress:.0%}"
        )

        st.progress(min(progress, 1.0))

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Jumlah Truk", 25)

    with col2:
        st.metric("Jumlah Outer", 1500)

    if st.button("Logout"):
        st.session_state.login = False
        st.rerun()