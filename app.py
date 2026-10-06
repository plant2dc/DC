import streamlit as st

# =====================================
# PENGATURAN HALAMAN
# =====================================

st.set_page_config(
    page_title="Delivery Control",
    page_icon="🚚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =====================================
# CSS MOBILE FRIENDLY
# =====================================

st.markdown("""
<style>
.block-container {
    max-width: 100% !important;
    padding-top: 1rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

div.stButton > button {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# =====================================
# DATA USER
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

    st.title("🔐 Login Delivery Control")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("LOGIN"):

        if (
            username in users
            and users[username] == password
        ):

            st.session_state.login = True
            st.session_state.user = username
            st.rerun()

        else:

            st.error(
                "Username atau Password salah"
            )

# =====================================
# DASHBOARD
# =====================================

else:

    st.title("🚚 DELIVERY CONTROL")

    st.success(
        f"Selamat datang {st.session_state.user}"
    )

    st.markdown("---")

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

    st.markdown("---")

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

    st.markdown("---")

    if st.button("LOGOUT"):

        st.session_state.login = False
        st.session_state.user = ""
        st.rerun()