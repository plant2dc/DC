import streamlit as st

# =====================================
# KONFIGURASI
# =====================================

st.set_page_config(
    page_title="Delivery Control",
    page_icon="🚚",
    layout="wide"
)

# =====================================
# CSS MOBILE STYLE
# =====================================

st.markdown("""
<style>

.block-container{
    padding-top:10px;
    padding-left:10px;
    padding-right:10px;
    padding-bottom:10px;
}

.card{
    background:white;
    border-radius:15px;
    padding:20px;
    margin-bottom:15px;
    box-shadow:0 2px 8px rgba(0,0,0,0.15);
    text-align:center;
}

.judul{
    font-size:18px;
    color:#666666;
}

.nilai{
    font-size:36px;
    font-weight:bold;
    color:#0078D4;
}

div.stButton > button{
    width:100%;
    height:50px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# USER LOGIN
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
# HALAMAN LOGIN
# =====================================

if not st.session_state.login:

    st.markdown(
        "<h1 style='text-align:center'>🚚 DELIVERY CONTROL</h1>",
        unsafe_allow_html=True
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("LOGIN"):

        if (
            username in users and
            users[username] == password
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

    st.markdown(
        "<h1 style='text-align:center'>🚚 DELIVERY CONTROL</h1>",
        unsafe_allow_html=True
    )

    st.success(
        f"Selamat datang {st.session_state.user}"
    )

    st.markdown("""
    <div class="card">
        <div class="judul">🚚 Total Truck</div>
        <div class="nilai">25</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="judul">📦 Total Outer</div>
        <div class="nilai">1500</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="judul">✅ Verification</div>
        <div class="nilai">100</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="judul">⚠️ Outstanding</div>
        <div class="nilai">5</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("LOGOUT"):

        st.session_state.login = False
        st.session_state.user = ""

        st.rerun()