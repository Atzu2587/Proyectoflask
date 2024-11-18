from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el formulario de ejercicio 1 (Notas)
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    aprobado = None
    if request.method == 'POST':
        # Recibimos las notas y asistencia desde el formulario
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Realizamos el cálculo promedio
        promedio = (nota1 + nota2 + nota3) / 3
        aprobado = promedio >= 40 and asistencia >= 75  # Regla de aprobación

    # Renderizamos la plantilla con los resultados
    return render_template('ejercicio1.html',
                           promedio=promedio,
                           aprobado=aprobado)

# Ruta para el formulario de ejercicio 2 (Nombres)
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    cantidad_caracteres = None
    if request.method == 'POST':
        # Recibimos los nombres desde el formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Determinamos el nombre con más caracteres
        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mayor)

    # Renderizamos la plantilla con los resultados
    return render_template('ejercicio2.html',
                           nombre_mayor=nombre_mayor,
                           cantidad_caracteres=cantidad_caracteres)

if __name__ == '__main__':
    app.run(debug=True)
