import subprocess
def flush_dns():
    print("Limpando cache DNS...")
    subprocess.run("ipconfig /flushdns", shell=True)
    print("Cache DNS limpo com sucesso!")