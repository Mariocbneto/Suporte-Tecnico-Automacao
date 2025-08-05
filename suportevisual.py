import sys
from funcao_reiniciar import reiniciar
from funcao_flushdns import flush_dns
from funcao_ipconfig import mostrar_ipconfig
from funcao_java import atualizar_java
from funcao_vpn import abrir_portal_vpn
from funcao_serpro import instalar_serpro
from funcao_daruma import instalar_daruma
from funcao_impressora import adicionar_impressora 
from funcao_planner import abrir_planner

def menu():
    while True:
        print("\n============= Menu Suporte Técnico ==============")
        print("1. Reiniciar o computador")
        print("2. Limpar cache DNS")
        print("3. IpConfig")
        print("4. Atualizar Java")
        print("5. Ver situação da VPN")
        print("6. Baixar Daruma")
        print("7. Instalar CertificadoSerpro")
        print("8. Adicionar Impressora")
        print("9. Abrir Planner")
        print("10. Sair")
        print("==================================================")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            reiniciar()
        elif opcao == '2':
            flush_dns()
        elif opcao == '3':
            mostrar_ipconfig()
        elif opcao == '4':
            print("Atualizar Java...")
            atualizar_java()
        elif opcao == '5':
            abrir_portal_vpn()
        elif opcao == '6':
            instalar_daruma()
        elif opcao == '7':
            instalar_serpro()
        elif opcao == '8':
            adicionar_impressora()
        elif opcao == '9':
            abrir_planner()
        elif opcao == '10':
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

menu()
