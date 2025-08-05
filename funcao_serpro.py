import os 
import shutil 
import subprocess

def instalar_serpro():
    letra_pen = "E:"
    nome = "InstaladorCertificadoSerpro-1.1.0.exe"
    caminhoorigem = os.path.join(letra_pen, nome)
    caminho_destino = os.path.join("C:\\temp", nome)

    if not os.path.exists("C:\\temp"):
        os.makedirs("C:\\temp")

    if os.path.exists(caminhoorigem):
        print(f"Instalador encontrado no pendrive ({caminhoorigem}).")
        confirmar = input("Deseja copiar e instalar o certificado Serpro? (s/n): ").strip().lower()

        if confirmar == 's':
            print("Copiando o instalador para o computador...")
            shutil.copy(caminhoorigem, caminho_destino)
            print(f"Instalador copiado para {caminho_destino}.")

            print("Executando o instalador...")
            try:
                subprocess.run([caminho_destino], check=True)
                print("Instalação concluída com sucesso.")
            except subprocess.CalledProcessError:
                print("Erro ao executar o instalador.")
        else:
            print("Instalação cancelada pelo usuário.")
    else:
        print("Arquivo não encontrado no pendrive. Verifique a letra da unidade.")
