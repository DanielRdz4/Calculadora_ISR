# Calculadora de ISR (Personas Físicas)

Este programa permite calcular la **tasa de ISR aplicable** a un contribuyente, de acuerdo con su **régimen fiscal**, considerando un **ingreso mensual**.

El objetivo es ofrecer una **herramienta simplificada** para entender y estimar el impuesto causado en un mes determinado.

---

## 📌 Alcance del programa

- Calcula el **ISR mensual causado**
- Determina la **tasa efectiva de ISR**
- Aplica la **tarifa mensual vigente**
- Funciona para distintos **regímenes fiscales**

---

## ⚠️ Aclaraciones clave

### 1️⃣ Regímenes fiscales
Para fines del programa:

- El régimen de **Asalariados**
- y el régimen de **Actividad Empresarial y Profesional**

se consideran **funcionalmente equivalentes**, ya que:

- El cálculo es **mensual**
- **No se considera PTU**, incluso en el caso de Actividad Empresarial

---

### 2️⃣ Ingreso mensual
La variable **ingreso mensual** representa:

- El **total de los ingresos percibidos en el mes**
- Sin distinguir su **origen** (salario, honorarios, ventas, etc.)

> Esta es una **simplificación**, ya que en la práctica el tratamiento fiscal
> puede variar según la fuente del ingreso.

---

### 3️⃣ Pagos previos de ISR
El cálculo:

- **No considera pagos provisionales anteriores**
- **No toma en cuenta retenciones previas**
- **No contempla pagos adelantados o parciales de ISR**

El resultado corresponde únicamente al **ISR causado en el mes**.

---

## 📉 Reglas de validación para deducciones

El programa aplica **restricciones lógicas de monto** para evitar valores
inconsistentes.

Regla general:
- **Deduciones =< Ingresos** 

Para asalariados:
- **Deduciones =< 5 UMAS**

---

## 🧠 Consideraciones finales

Este programa tiene fines **educativos y de estimación**.

No sustituye:
- La asesoría de un contador
- El cálculo oficial realizado ante el SAT
- La declaración mensual o anual formal

---

## 📂 Uso recomendado

Ideal para:
- Simulaciones
- Aprendizaje fiscal
- Automatización básica de cálculos
- Proyectos personales o académicos
