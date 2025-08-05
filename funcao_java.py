import os
import subprocess
import urllib.request

java_versao = "8" #Pode ser alterado junto da URL
java_url = "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=247917_4d5417147a92418ea8b615e228bb6935"
java_instalador = "java_installer.exe"

def atualizar_java():
    print("\nVerificando se o Java esta instalado...")
    try:
        output = subprocess.check_output("java -version", shell=True, stderr=subprocess.STDOUT)
        output = output.decode('utf-8')
        if java_versao in output:
            print("Java já está instalado.")
            atualizar = input("Deseja atualizar o Java? (s/n): ")
            if atualizar != 's':
                return
        else:
            print("Java está destualizado. Atualizando...")
    except subprocess.CalledProcessError:
            print("Java não está instalado. Será feita a instalação...")


    print("Baixando o instalador do Java...")
    urllib.request.urlretrieve(java_url, java_instalador)
    print("Download concluído.")

    print("Instalando o Java...")
    try:
        subprocess.run([java_instalador, "/s"], check=True)
        print("Java atualizado com sucesso.")
    except subprocess.CalledProcessError:
        print("Erro ao instalar o Java.")

    if os.path.exists(java_instalador):
        os.remove(java_instalador)
    
