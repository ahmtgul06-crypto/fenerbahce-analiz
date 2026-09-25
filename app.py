import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Sayfa Yapılandırması
st.set_page_config(page_title="Fenerbahçe Oyuncu Analiz Raporu", layout="centered", page_icon="💛🔵")

# Üst Başlık ve Oyuncu Kartı Bölümü
st.markdown("<h1 style='text-align: center;'>💛🔵 Vedat Muriqi</h1>", unsafe_allow_html=True)

col_info, col_dots = st.columns([1, 1])

with col_info:
    st.markdown("""
    **Yaş:** 32  
    **Pozisyon:** ST (Santrfor)  
    **Takım:** Fenerbahçe SK  
    **Üle:** Kosova 🇽🇰
    """)

with col_dots:
    # Görseldeki yuvarlak skor göstergelerinin taklidi
    st.markdown("""
    🟡🟡🟡🟡🟡🟡🟡🟡🟡⚪ **Target Man**  
    🟡🟡🟡🟡🟡🟡🟡🟡⚪⚪ **Aerial Dominance**  
    🟡🟡🟡🟡🟡🟡🟡⚪⚪⚪ **Finishing**  
    🟡🟡🟡🟡🟡🟡🟡🟡🟡⚪ **Link-up Play**
    """)

st.markdown("---")

# 1. BÖLÜM: Pozisyonel Sorumluluk Analizi (Yatay Bar Grafik)
st.subheader("Pozisyonel Sorumluluk Analizi")
st.caption("Süper Lig'deki diğer santrforlara göre yüzdelik (Percentile) başarı sıralaması")

# Görseldeki yatay bar grafiğinin birebir yapısı
bar_data = {
    "Yetenek Alanı": [
        "Hava Topu Kazanma", 
        "Ceza Sahası Aksiyonları", 
        "Pres ve Savunma Katkısı", 
        "Sırtı Dönük Top Saklama", 
        "Gol Vuruşu Kalitesi", 
        "Bağlantı Pasları"
    ],
    "Yüzdelik Dilim": [95, 82, 75, 88, 80, 78]
}
df_bar = pd.DataFrame(bar_data)

# Farklı renk paletiyle şık bir yatay bar grafik
fig_bar = px.bar(
    df_bar, 
    x="Yüzdelik Dilim", 
    y="Yetenek Alanı", 
    orientation='h',
    range_x=[0, 100],
    color="Yüzdelik Dilim",
    color_continuous_scale=["#1C3D5A", "#EAAA00"] # Fenerbahçe Lacivert & Altın Sarısı tonları
)
fig_bar.update_layout(showlegend=False, height=350, margin=dict(l=20, r=20, t=10, b=10))
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# 2. BÖLÜM: Detaylı Oyuncu Metrikleri (İki Adet Radar Grafik)
st.subheader("Detaylı Oyuncu Metrikleri")
st.caption("Seçili performans alanlarındaki mikro istatistik kırılımları")

col_radar1, col_radar2 = st.columns(2)

# Radar 1: Hücum & Bitiricilik
with col_radar1:
    st.markdown("<h4 style='text-align: center;'>Hücum & Bitiricilik</h4>", unsafe_allow_html=True)
    
    categories1 = ['Gol / 90', 'Beklenen Gol (xG)', 'Şut İsabeti %', 'Ceza Sahasında Buluşma', 'Kilit Pas']
    values1 = [85, 90, 75, 88, 70]
    
    fig_radar1 = go.Figure()
    fig_radar1.add_trace(go.Scatterpolar(
        r=values1 + [values1[0]],
        theta=categories1 + [categories1[0]],
        fill='toself',
        fillcolor='rgba(234, 170, 0, 0.4)',
        line=dict(color='#EAAA00')
    ))
    fig_radar1.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False, height=300, margin=dict(l=40, r=40, t=20, b=20)
    )
    st.plotly_chart(fig_radar1, use_container_width=True)

# Radar 2: Fiziksel & Bağlantı Oyunu
with col_radar2:
    st.markdown("<h4 style='text-align: center;'>Fiziksel & Bağlantı Oyunu</h4>", unsafe_allow_html=True)
    
    categories2 = ['Hava Topu %', 'Top Saklama', 'İleride Basma', 'Pas İsabet %', 'Faul Alma']
    values2 = [95, 90, 80, 72, 85]
    
    fig_radar2 = go.Figure()
    fig_radar2.add_trace(go.Scatterpolar(
        r=values2 + [values2[0]],
        theta=categories2 + [categories2[0]],
        fill='toself',
        fillcolor='rgba(28, 61, 90, 0.4)',
        line=dict(color='#1C3D5A')
    ))
    fig_radar2.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False, height=300, margin=dict(l=40, r=40, t=20, b=20)
    )
    st.plotly_chart(fig_radar2, use_container_width=True)

# Alt Bilgi Notu (Görseldeki gibi)
st.markdown("---")
st.info("💡 Bu panel Eylül 2026 Süper Lig verileri temel alınarak hazırlanmıştır.")
