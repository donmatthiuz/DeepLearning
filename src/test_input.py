from InputController import InputController # si lo guardas en otro archivo
# o simplemente pega la clase arriba y sigue

ctrl = InputController(delay=0.1, verbose=True)

print("Tienes 3 segundos para abrir el bloc de notas...")
ctrl.wait(3)

ctrl.write("Hola, esto fue escrito usando InputController!")
ctrl.enter()
ctrl.write("Prueba exitosa ✅")
ctrl.enter()
