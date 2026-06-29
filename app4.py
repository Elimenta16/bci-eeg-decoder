import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="BCI EEG Decoder", layout="wide")

# Estilos CSS para darle la vibra de terminal médica futurista
st.markdown("""
    <style>
    .reportview-container { background: #0a0e17; }
    .big-title { font-size:40px !important; font-weight: bold; color: #00ffcc; text-shadow: 0 0 10px #00ffcc; }
    .panel-box { padding: 20px; background-color: #111726; border-radius: 10px; border: 1px solid #00ffcc; }
    .cmd-box { padding: 30px; background-color: #1a0f2e; border-radius: 10px; border: 2px dashed #9900ff; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🧠 BCI NEURAL DECODER & INTERFACE</p>', unsafe_allow_html=True)
st.caption("Córtex Motor - Sistema de Decodificación de Microtensiones en Tiempo Real para Soporte de Autonomía Motriz")
st.markdown("---")

# --- DISEÑO DEL LAYOUT EN COLUMNAS (Estilo Centro de Control) ---
col_control, col_grafica, col_comando = st.columns([1.5, 2.5, 2.0])

with col_control:
    st.markdown("### 🎛️ Configuración y Señal")
    archivo_cargado = st.file_uploader("Cargar Registro EEG (.xlsx, .csv):", type=["xlsx", "csv"])
    
    if archivo_cargado is not None:
        try:
            if archivo_cargado.name.endswith('.xlsx'):
                df = pd.read_excel(archivo_cargado)
            else:
                df = pd.read_csv(archivo_cargado)
                
            st.success(f"⚡ Enlace Neuronal Establecido: {len(df)} frames.")
            
            # Verificar estructura
            columnas = ['Timestamp', 'Canal_C3_uV', 'Canal_C4_uV', 'Canal_Cz_uV', 'Tipo_Onda_Dominante']
            if all(c in df.columns for c in columnas):
                # Tomar la última lectura simulando tiempo real
                ultima_lectura = df.iloc[-1]
                
                st.markdown("---")
                st.markdown("**Estatus de Electrodos (10-20):**")
                st.info(f"📍 Canal C3 (Izquierdo): {ultima_lectura['Canal_C3_uV']} μV")
                st.info(f"📍 Canal C4 (Derecho): {ultima_lectura['Canal_C4_uV']} μV")
                st.info(f"📍 Canal Cz (Central): {ultima_lectura['Canal_Cz_uV']} μV")
                
            else:
                st.error("❌ Columnas incompatibles con la matriz motriz.")
                df = None
        except Exception as e:
            st.error(f"Error de telemetría: {e}")
            df = None
    else:
        st.warning("💤 Esperando flujo de datos EEG...")
        df = None

with col_grafica:
    st.markdown("### 📈 Osciloscopio de Ondas Cerebrales")
    if df is not None:
        # Gráfica de líneas interactiva de las microtensiones
        fig_lineas = go.Figure()
        fig_lineas.add_trace(go.Scatter(x=df['Timestamp'], y=df['Canal_C3_uV'], name='C3 (Mano Der.)', line=dict(color='#00ffcc', width=2)))
        fig_lineas.add_trace(go.Scatter(x=df['Timestamp'], y=df['Canal_C4_uV'], name='C4 (Mano Izq.)', line=dict(color='#ff007f', width=2)))
        fig_lineas.add_trace(go.Scatter(x=df['Timestamp'], y=df['Canal_Cz_uV'], name='Cz (Freno/Relajación)', line=dict(color='#9900ff', width=2)))
        
        fig_lineas.update_layout(
            template="plotly_dark",
            xaxis_title="Tiempo (s)",
            yaxis_title="Potencial (μV)",
            margin=dict(l=20, r=20, t=20, b=20),
            height=380
        )
        st.plotly_chart(fig_lineas, use_container_width=True)
    else:
        st.info("Sube el archivo para inicializar el osciloscopio.")

with col_comando:
    st.markdown("### 🤖 Procesamiento y Comando")
    if df is not None:
        # Lógica de decodificación del último pensamiento detectado
        onda = ultima_lectura['Tipo_Onda_Dominante']
        c3 = ultima_lectura['Canal_C3_uV']
        c4 = ultima_lectura['Canal_C4_uV']
        cz = ultima_lectura['Canal_Cz_uV']
        
        comando = "🔒 MODO ESPERA / SISTEMA NEUTRO"
        color_alert = "#9900ff"
        
        if onda == 'Theta':
            comando = "💤 ALERTA: PACIENTE DORMIDO"
            color_alert = "#ffaa00"
        elif onda == 'Alfa':
            comando = "🛑 COMANDO: DETENER MOTOR"
            color_alert = "#ff0000"
        elif onda == 'Beta':
            if c3 > c4:
                comando = "➡️ COMANDO: MOVER MANO DERECHA"
                color_alert = "#00ffcc"
            elif c4 > c3:
                comando = "⬅️ COMANDO: MOVER MANO IZQUIERDA"
                color_alert = "#ff007f"

        # Caja de salida gigante tipo Cyberpunk
        st.markdown(f"""
            <div class="cmd-box" style="border-color: {color_alert};">
                <p style="color: #ffffff; font-size: 14px; margin: 0;">INTENCIÓN NEUROLÓGICA TRADUCIDA:</p>
                <p style="color: {color_alert}; font-size: 24px; font-weight: bold; margin: 10px 0 0 0;">{comando}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Gráfica complementaria de distribución de ritmo dominante
        st.markdown("<br>", unsafe_allow_html=True)
        fig_pie = px.pie(df, names='Tipo_Onda_Dominante', hole=0.4,
                         color_discrete_sequence=['#00ffcc', '#9900ff', '#ffaa00'])
        fig_pie.update_layout(template="plotly_dark", height=200, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_pie, use_container_width=True)
