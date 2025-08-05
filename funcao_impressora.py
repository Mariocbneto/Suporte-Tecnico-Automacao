import subprocess

def adicionar_impressora():
    ip = (input("Digite o IP da impressora: ")).strip()
    nome_impressora = (input("Digite o nome da impressora: ")).strip()

    porta = f"IP_{ip}"

    cmd_porta = [
        "cscript", "C:\\Windows\\System32\\Printing_Admin_Scripts\\pt-BR\\prnport.vbs",
        "-a", "-r", porta, "-h", ip, "-o", "raw", "-n", "9100"]
    
    cmd_impressora = [
        "rundll32", "printui.dll,PrintUIEntry",
        "/if",
        f"/b", nome_impressora,
        "/r", porta,
        "/m", "Genérico / Somente texto",
        "/z", "/u" ]
    
    try:
        print("Adicionando porta da impressora...")
        subprocess.run(cmd_porta, check=True)
        print("Porta adicionada com sucesso.")

        print("Adicionando impressora...")
        subprocess.run(cmd_impressora, check=True)
        print(f"Impressora '{nome_impressora}' adicionada com sucesso.")
    except subprocess.CalledProcessError:
        print("Erro ao adicionar impressora.")

