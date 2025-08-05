import os
import shutil
import subprocess

def instalar_daruma():
    pendrive = "E:"
    arquivos = ["Driver_Daruma_S700.exe", "Driver_Spooler_700.exe"]
    destino = "C:\\temp"

    if not os.path.exists(destino):
        os.makedirs(destino)

    for i, arquivo in enumerate(arquivos):
        origem = os.path.join(pendrive, arquivo)
        destino_arquivo = os.path.join(destino, arquivo)

        if os.path.exists(origem):
            print(f"\nArquivo encontrado: {arquivo}")
            confirmar = input(f"Você deseja copiar {arquivo} para {destino}? (s/n): ").strip().lower()

            if confirmar == 's':
                print("Copiando instalador...")
                shutil.copy(origem, destino_arquivo)
                print(f"Instalador copiado para {destino_arquivo}")

                print("Executando o instalador...")
                try:
                    subprocess.run([destino_arquivo], check=True)
                except subprocess.CalledProcessError:
                    print(f"Erro ao instalar {arquivo}.")

                if i == 0:
                    mostrar_instrucao_primeiro()
                else:
                    mostrar_instrucao_segundo()
            else:
                print(f"Instalação de {arquivo} cancelada.")
        else:
            print(f"Arquivo {arquivo} não encontrado no pendrive {pendrive}.")

def mostrar_instrucao_primeiro():
    print("\n--- INSTRUÇÕES PARA O PRIMEIRO INSTALADOR ---")
    print("1. Quando abrir, clique em 'Impressora conectada'.")
    print("2. Depois clique em 'Avançar'.")
    print("3. Aguarde a instalação terminar.")
    input("\nPressione Enter quando terminar para continuar para o próximo instalador...")

def mostrar_instrucao_segundo():
    print("\n--- INSTRUÇÕES PARA O SEGUNDO INSTALADOR ---")
    print("1. Clique em 'A impressora que eu quero não está na lista'.")
    print("2. Escolha 'Adicionar uma impressora local' (última opção).")
    print("3. Selecione uma porta COM (COM1 a COM4).")
    print("4. No Gerenciador de Dispositivos do Windows, verifique qual COM está sendo usada.")
    print("5. Se necessário, desconecte alguma porta antes de conectar a Daruma.")
    input("\nPressione Enter para finalizar...")

