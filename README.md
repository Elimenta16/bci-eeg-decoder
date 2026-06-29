# Brain-Computer Interface (BCI) Neural Decoder 🧠✨

A futuristic, cyberpunk-styled Streamlit dashboard built to simulate a Brain-Computer Interface. It processes real-time EEG microvolt ($\mu V$) signals from the motor cortex and translates neurological intentions into robotic control commands.

## 🚀 Live Demo
🔗 [Check out the live neuro-link here!](PASTE_YOUR_STREAMLIT_URL_HERE)

## 🌌 Layout & Architecture (Control Center Style)
Unlike traditional stacked applications, this dashboard features a **three-panel mission control layout** optimized for widescreen monitoring:
1. **🎛️ Telemetry & Signal Input (Left Panel):** Handles the EEG data stream upload and monitors physical microvoltage across specific international 10-20 system nodes (**C3**, **C4**, **Cz**).
2. **📈 Brainwave Oscilloscope (Center Panel):** An interactive, dark-themed real-time multi-channel line chart mapping continuous potential changes ($\mu V$) over time.
3. **🤖 Cyberpunk Command Core (Right Panel):** A dynamic interface that runs a decoding algorithm to translate dominant wave rhythms into robotic output, altering UI glow colors based on current mental states.

## 🧠 Decoding Logic
The core Python script interprets motor cortex activity by analyzing specific frequencies:
* **High Beta ($\beta$) on C3 Node:** Decodes left-hemisphere motor intent $\rightarrow$ `➡️ COMANDO: MOVER MANO DERECHA` (Cyan glow)
* **High Beta ($\beta$) on C4 Node:** Decodes right-hemisphere motor intent $\rightarrow$ `⬅️ COMANDO: MOVER MANO IZQUIERDA` (Pink glow)
* **High Alpha ($\alpha$) on Cz Node:** Decodes relaxation/blink baseline $\rightarrow$ `🛑 COMANDO: DETENER MOTOR` (Red glow)
* **Dominant Theta ($\theta$) Rhythm:** Detects microsleep/drowsiness $\rightarrow$ `💤 ALERTA: PACIENTE DORMIDO` (Amber warning)

## 🧰 Tech Stack
* **Language:** Python
* **UI Framework:** Streamlit (Custom CSS injection for Cyberpunk UI)
* **Signal Visuals:** Plotly Graph Objects & Plotly Express
* **Data Matrix:** Pandas & OpenPyXL
