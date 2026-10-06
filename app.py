import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Delivery Control",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================
# CSS MOBILE
# =====================================

st.markdown("""
<style>

/* Gunakan seluruh lebar layar */
.block-container {
    max-width: 100% !important;
    width: 100% !important;
    padding-top: 5px !important;
    padding-bottom: 5px !important;
    padding-left: 5px !important;
    padding-right: 5px !important;
}

/* Hilangkan ruang kosong berlebihan */
.main {
    width: 100% !important;
}

/* Input lebih besar */
.stTextInput input {
    font-size: 18px !important;
}

/* Tombol full layar */
.stButton > button {
    width: 100% !important;
    height: 50px !important;
    font-size: 18px !important;
}

/* Kartu metric */
[data-testid="metric-container"] {
    border: 1px solid #dddddd;
    border-radius: 10px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# USER
# =====================================

users = {
    "fani": "12345",
    "DC": "54321"
}

# =====================================
# SESSION
# =====================================

if "login" not in st.session_state:
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = ""

# =====================================
# LOGIN
# =====================================

if not st.session_state.login:

    st.title("🚚 DELIVERY CONTROL")

    st.subheader("Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("LOGIN"):

        if username in users and users[username] == password:

            st.session_state.login = True
            st.session_state.user = username

        else:

            st.error(
                "Username atau Password salah"
            )

# =====================================
# DASHBOARD
# =====================================

if st.session_state.login:

    st.title("🚚 DELIVERY CONTROL")

    st.success(
        f"Selamat datang {st.session_state.user}"
    )

    st.divider()

    plan = st.number_input(
        "📦 Plan Delivery",
        min_value=0,
        value=0
    )

    actual = st.number_input(
        "✅ Actual Delivery",
        min_value=0,
        value=0
    )

    if plan > 0:

        progress = actual / plan

        st.metric(
            "📊 Progress",
            f"{progress:.0%}"
        )

        st.progress(
            min(progress, 1.0)
        )

    st.divider()

    st.metric(
        "🚚 Total Truck",
        "25"
    )

    st.metric(
        "📦 Total Outer",
        "1500"
    )

    st.metric(
        "✅ Verification",
        "100"
    )

    st.metric(
        "⚠️ Outstanding",
        "5"
    )

    st.divider()

    if st.button("LOGOUT"):

        st.session_state.login = False
        st.session_state.user = ""