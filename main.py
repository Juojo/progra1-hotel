from menus import mostrarIngresarMenuLogin, mostrarIngresarMenuPrincipal

# Datos predefinidos

usuarios = [
    ["recepcionista1", "123"],
    ["", ""]
]

# Programa Principal

login_exitoso = mostrarIngresarMenuLogin(usuarios)

if login_exitoso:
    mostrarIngresarMenuPrincipal()
print("Fin programa")