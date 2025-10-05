import matplotlib.pyplot as plt
import os

# Datos simulados
etiquetas = ['Compactación', 'Incineración', 'Energía', 'Reutilización']
valores = [40, 25, 20, 15]
colores = ['#0d6efd', '#dc3545', '#ffc107', '#198754']

# Ruta absoluta al archivo de salida
output_path = os.path.join(
    'regroup_web', 'residuos_no_reciclables', 'static', 'residuos_no_reciclables', 'img', 'distribucion_residuos_no_reciclables.png'
)

# Crear gráfico
plt.figure(figsize=(6, 6))
plt.pie(valores, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Estrategias de Tratamiento')
plt.tight_layout()
plt.savefig(output_path)
