import streamlit as st

st.set_page_config(
    page_title="TEST FULL HP",
    layout="wide"
)

st.markdown("""
<style>

html, body, [data-testid="stAppViewContainer"] {
    margin: 0;
    padding: 0;
}

.block-container {
    max-width: 100% !important;
    width: 100% !important;
    padding: 0 !important;
}

.fullscreen {
    width: 100vw;
    min-height: 100vh;
    background: #0078D4;
    color: white;
    text-align: center;
    padding-top: 50px;
    box-sizing: border-box;
}

.title {
    font-size: 40px;
    font-weight: bold;
}

.value {
    font-size: 80px;
    margin-top: 30px;
}

</style>

<div class="fullscreen">
    <div class="title">
        🚚 DELIVERY CONTROL
    </div>

    <div class="value">
        1500
    </div>

    <div>
        FULL SCREEN TEST
    </div>
</div>

""", unsafe_allow_html=True)