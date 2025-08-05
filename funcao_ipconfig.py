import subprocess

def mostrar_ipconfig():
    print("Exibindo informações de IPConfig...")
    subprocess.run("ipconfig", shell=True)
    print("Informações de IPConfig exibidas com sucesso!")