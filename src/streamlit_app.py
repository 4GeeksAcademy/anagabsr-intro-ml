import streamlit as st

st.set_page_config(page_title="Calculadora de Gross Profit", layout="centered")

st.title("🧮 Calculadora de Gross Profit")
st.write("Introduce los valores para obtener el Gross Profit, el margen actual y compararlo con tu margen objetivo.")

# Columnas revenue y COGS
col1, col2 = st.columns(2)

with col1:
    revenue = st.number_input("Revenue (Ingresos)", min_value=0.0, step=100.0)
with col2:
    cogs = st.number_input("COGS (Coste de bienes vendidos)", min_value=0.0, step=100.0)

st.divider()

#target margin

target_margin = st.number_input(
    "Margen bruto objetivo (%)",
    min_value=0.0,
    max_value=100.0,
    value=30.0,
    step=1.0,
    help="Introduce el margen bruto que te gustaría conseguir sobre el revenue."
)

if revenue == 0:
    st.info("Introduce un Revenue mayor que 0 para calcular los indicadores.")
else:
    gross_profit = revenue - cogs
    gross_margin = (gross_profit / revenue) * 100

    st.subheader("📊 Resultados actuales")
    col_r1, col_r2, col_r3 = st.columns(3)
    with col_r1:
        st.metric("Gross Profit", f"{gross_profit:,.2f} €")
    with col_r2:
        st.metric("Gross Margin actual", f"{gross_margin:.2f} %")
    with col_r3:
        st.metric("Margen objetivo", f"{target_margin:.2f} %")

    if cogs > revenue:
        st.warning(
            "El COGS es mayor que el Revenue, el Gross Profit es negativo. "
            "Revisa precios, descuentos o estructura de costes."
        )

    if gross_margin < target_margin:
        st.error(
            f"El margen actual ({gross_margin:.2f} %) está por debajo del margen objetivo ({target_margin:.2f} %)."
        )
    else:
        st.success(
            f"El margen actual ({gross_margin:.2f} %) está en línea o por encima del objetivo ({target_margin:.2f} %)."
        )

    st.divider()

cogs_max_for_target = revenue * (1 - target_margin / 100)

st.subheader("🔍 Análisis de margen objetivo")

col_a1, col_a2 = st.columns(2)
with col_a1:
        st.write(f"**COGS actual:** {cogs:,.2f} €")
        st.write(f"**COGS máximo para margen objetivo:** {cogs_max_for_target:,.2f} €")
with col_a2:
        diff_cogs = cogs - cogs_max_for_target
        if diff_cogs > 0:
            st.write(
                f"Para alcanzar el margen objetivo, deberías reducir el COGS en aproximadamente "
                f"**{diff_cogs:,.2f} €** o aumentar precios."
            )
        else:
            st.write(
                "Con el COGS actual estás dentro del rango para cumplir o superar el margen objetivo."
            )

