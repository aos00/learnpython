#!/usr/bin/python3.5

import subprocess

try:
    retorno = subprocess.run("./dormir.out", stdout=subprocess.PIPE, timeout=5)
except subprocess.TimeoutExpired:
    print("Erro timeout")
else:
    msg = retorno.stdout
    cod_retorno = retorno.returncode
    print("Codigo de retorno:", cod_retorno)
    print("Mensagem de retorno:", msg)
