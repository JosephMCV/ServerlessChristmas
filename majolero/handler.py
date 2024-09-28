import json

def christmassTree(event, context):
    arbolito = ""
    arbolitoInvertido = ""
    n = 10

   
    for i in range(n):
        arbolito += (" " * (n - i) + "*" * (i * 2 + 1) + "\n")

    
    for i in range(n // 2):
        if n % 2 == 0:
            arbolito += (" " * (n - (n // 2)) + "*" * (n + 1) + "\n")
        else:
            arbolito += (" " * (n - (n // 2)) + "*" * n + "\n")

    
    for i in range(n // 2):
        if n % 2 == 0:
            arbolitoInvertido += (" " * (n - (n // 2)) + "*" * (n - 1) + "\n")
        else:
            arbolitoInvertido += (" " * (n - (n // 2)) + "*" * (n - 2) + "\n")

    for i in range(n, 0, -1):
        arbolitoInvertido += " " * (n - i) + "*" * (i * 2 - 1) + "\n"

    
    arbolesCombinados = arbolito + "\n" + arbolitoInvertido

    
    arbolesCombinados_html = arbolesCombinados.replace("\n", "<br>")

    
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": f"<html><body><pre>{arbolesCombinados_html}</pre></body></html>"
    }

    return response
