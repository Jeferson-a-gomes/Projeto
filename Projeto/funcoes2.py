#Microatividade 6: utilização de funções
def loginUsuario(perfil):
    perfil = input("Digite seu usuário:").lower()
    if perfil =='admin':
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usuário")

#fora da função
perfil=''
loginUsuario(perfil)
