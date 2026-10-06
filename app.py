import streamlit as st

st.set_page_config(
    page_title="Delivery Control",
    page_icon="🚚",
    layout="wide"
)

st.markdown("""
<style>

/* Paksa container penuh */
.block-container {
    max-width: 100% !important;
    padding: 0px !important;
}

/* Hilangkan jarak bawaan */
.main {
    padding: 0px !important;
}

/* Header biru */
.header {
    width: 100%;
    background: #0078D4;
    color: white;
    text-align: center;
    padding: 20px;
    font-size: 28px;
    font-weight: bold;
}

/* Card */
.card {
    width: calc(100% - 20px);
    margin: 10px;
    background: white;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

.title {
    font-size: 20px;
    color: #666;
}

.value {
    font-size: 40px;
    font-weight: bold;
    color: #0078D4;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
🚚 DELIVERY CONTROL
</div>

<div class="card">
    <div class="title">🚚 TOTAL TRUCK</div>
    <div class="value">25</div>
</div>

<div class="card">
    <div class="title">📦 TOTAL OUTER</div>
    <div class="value">1500</div>
</div>

<div class="card">
    <div class="title">✅ VERIFICATION</div>
    <div class="value">100</div>
</div>

<div class="card">
    <div class="title">⚠️ OUTSTANDING</div>
    <div class="value">5</div>
</div>
""", unsafe_allow_html=True)