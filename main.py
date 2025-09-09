from menus.menu_principal import mostrarIngresarMenuLogin, mostrarIngresarMenuPrincipal

# Programa Principal

login_exitoso = mostrarIngresarMenuLogin()

if login_exitoso:
    mostrarIngresarMenuPrincipal()
print("Fin programa")