import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Sayfa Genişlik Ayarı
st.set_page_config(page_title="Fenerbahçe Oyuncu Analiz Raporu", layout="centered", page_icon="💛")

# --- 1. OYUNCU KİMLİK BİLGİLERİ (HEADER) ---
st.title("💛💙 Ederson Moraes")
col_info, col_roles = st.columns(2)

with col_info:
    st.markdown("""
    **Yaş:** 33  
    **Pozisyon:** GK (Kaleci)  
    **Takım:** Fenerbahçe SK  
    **Ülke:** Brezilya 🇧🇷
    """)

with col_roles:
    # Oyuncu Rol Değerlendirmesi (Fenerbahçe Sarısı Boncuklar)
    st.markdown("""
    🟡🟡🟡🟡🟡🟡🟡🟡🟡⚪ **Sweeper Keeper**  
    🟡🟡🟡🟡🟡🟡🟡🟡⚪⚪ **Shot Stopper**  
    🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡 **Ball Distribution**  
    🟡🟡🟡🟡🟡🟡⚪⚪⚪⚪ **Penalty Saver**  
    """)

st.markdown("---")

# --- 2. POZİSYONEL SORUMLULUKLAR (YATAY BAR GRAFİĞİ) ---
st.subheader("Pozisyonel Sorumluluk Analizi")
st.caption("Süper Lig'deki diğer kalecilere göre yüzdeklik (Percentile) başarı sıralaması")

# Ederson'un Yetenek Verileri
responsibilities_data = {
    "Yetenek Alanı": [
        "Ayakla Oyun (Passing)", 
        "Kurtarış Refleksleri", 
        "Ceza Sahası Hakimiyeti", 
        "Uzun Pas İsabeti", 
        "Bire Bir Pozisyonlar", 
        "Yan Top Kontrolü"
    ],
    "Yüzdelik Dilim": [95, 82, 79, 91, 85, 76]
}
df_resp = pd.DataFrame(responsibilities_data)

# Fenerbahçe Laciverti ve Sarısı ile Yatay Bar Grafik
fig_bar = px.bar(
    df_resp, 
    x="Yüzdelik Dilim", 
    y="Yetenek Alanı", 
    orientation='h',
    range_x=[0, 100],
    color="Yüzdelik Dilim",
    color_continuous_scale=["#002F6C", "#FFD100"] # Lacivert -> Sarı Geçişi
)
fig_bar.update_layout(
    showlegend=False, 
    height=350, 
    coloraxis_showscale=False,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)"
)
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# --- 3. SORUMLULUK DETAYLARI (DAİRESEL / RADAR GRAFİKLER) ---
st.subheader("Detaylı Kaleci Metrikleri")
st.caption("Seçili performans alanlarındaki mikro istatistik kırılımları")

col_chart1, col_chart2 = st.columns(2)

# Grafik 1: Kurtarış ve Defansif Aksiyonlar
with col_chart1:
    st.markdown("<h4 style='text-align: center; color: #002F6C;'>Kurtarış & Çizgi</h4>", unsafe_allow_html=True)
    
    categories = ['Kurtarış Yüzdesi', 'Refleksler', 'Ceza Sahası Dışı Koşu', 'Yenilen Gol (Maç Başı)', 'Penaltı Kurtarma']
    values = [79, 85, 90, 45, 60] # Simüle edilen metrik yüzdeleri
    
    fig_radar1 = go.Figure()
    fig_radar1.add_trace(go.Scatterpolar(
          r=values + [values[0]],
          theta=categories + [categories[0]],
          fill='toself',
          fillcolor='rgba(255, 209, 0, 0.4)', # Şeffaf Sarı dolgu
          line=dict(color='#002F6C', width=2)   # Lacivert çizgi
    ))
    fig_radar1.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])), 
        showlegend=False, 
        height=320
    )
    st.plotly_chart(fig_radar1, use_container_width=True)

# Grafik 2: Dağıtım ve Oyun Kurma (Ederson'un En Güçlü Yönü)
with col_chart2:
    st.markdown("<h4 style='text-align: center; color: #002F6C;'>Oyun Kurma & Dağıtım</h4>", unsafe_allow_html=True)
    
    categories2 = ['Kısa Pas İsabeti', 'Uzun Top İsabeti', 'Asist Beklentisi (xA)', 'Baskı Altında Karar', 'Hızlı Hücum Başlatma']
    values2 = [98, 88, 75, 94, 92]
    
    fig_radar2 = go.Figure()
    fig_radar2.add_trace(go.Scatterpolar(
          r=values2 + [values2[0]],
          theta=categories2 + [categories2[0]],
          fill='toself',
          fillcolor='rgba(0, 47, 108, 0.4)',  # Şeffaf Lacivert dolgu
          line=dict(color='#FFD100', width=2)   # Sarı çizgi
    ))
    fig_radar2.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])), 
        showlegend=False, 
        height=320
    )
    st.plotly_chart(fig_radar2, use_container_width=True)

st.info("💡 Bu panel Eylül 2026 Süper Lig verileri temel alınarak hazırlanmıştır.")
