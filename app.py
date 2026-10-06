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

.block-container{
    max-width:100%;
    width:100%;
    padding-top:10px;
    padding-left:10px;
    padding-right:10px;
    padding-bottom:10px;
}

/* Card Dashboard */
.card{
    background:#ffffff;
    border-radius:20px;
    padding:20px;
    margin-bottom:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.15);
    text-align:center;
}

/* Judul Card */
.title-card{
    font-size:20px;
    color:#666666;
    margin-bottom:10px;
}

/* Nilai Card */
.value-card{
    font-size:42px;
    font-weight:bold;
    color:#0078D4;
}

/* Tombol */
div.stButton > button{
    width:100%;
    height:55px;
    font-size:18px;
    border-radius:10px;
}

/* Input */
.stTextInput input{
    font-size:18px;
}

/* Hilangkan jarak berlebih */
h1{
    text-align:center;
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
# LOGIN PAGE
# =====================================

if not st.session_state.login:

    st.markdown(
        "<h1>🚚 DELIVERY CONTROL</h1>",
        unsafe_allow_html=True
    )

    st.write("")

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

    st.markdown(
        "<h1>🚚 DELIVERY CONTROL</h1>",
        unsafe_allow_html=True
    )

    st.success(
        f"Selamat datang {st.session_state.user}"
    )

    st.markdown("""

    <div class="card">
        <div class="title-card">
            🚚 TOTAL TRUCK
        </div>
        <div class="value-card">
            25
        </div>
    </div>

    <div class="card">
        <div class="title-card">
            📦 TOTAL OUTER
        </div>
        <div class="value-card">
            1500
        </div>
    </div>

    <div class="card">
        <div class="title-card">
            ✅ VERIFICATION
        </div>
        <div class="value-card">
            100
        </div>
    </div>

    <div class="card">
        <div class="title-card">
            ⚠️ OUTSTANDING
        </div>
        <div class="value-card">
            5
        </div>
    </div>

    """, unsafe_allow_html=True)

    if st.button("LOGOUT"):

        st.session_state.login = False
        st.session_state.user = ""

        st.rerun()