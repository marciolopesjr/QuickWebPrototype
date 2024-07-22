import os
import shutil
import htmlmin
import cssmin
import jsmin
import argparse

# Configuração dos diretórios
diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
diretorio_projetos = os.path.join(diretorio_raiz, "projetos")

# Função para minificar HTML
def minificar_html(conteudo):
    return htmlmin.minify(conteudo, remove_comments=True, collapse_whitespace=True)

# Função para minificar CSS
def minificar_css(conteudo):
    return cssmin.cssmin(conteudo)

# Função para minificar JavaScript
def minificar_js(conteudo):
    return jsmin.jsmin(conteudo)

# Função para processar arquivos
def processar_arquivo(arquivo, caminho_origem, caminho_destino):
    with open(caminho_origem, 'r', encoding='utf-8') as arquivo_origem:
        conteudo = arquivo_origem.read()

    if arquivo.endswith(".html"):
        conteudo = minificar_html(conteudo)
    elif arquivo.endswith(".css"):
        conteudo = minificar_css(conteudo)
    elif arquivo.endswith(".js"):
        conteudo = minificar_js(conteudo)

    with open(caminho_destino, 'w', encoding='utf-8') as arquivo_destino:
        arquivo_destino.write(conteudo)

# Função para criar um novo projeto
def criar_projeto(nome_projeto):
    diretorio_projeto = os.path.join(diretorio_projetos, nome_projeto)
    diretorio_src = os.path.join(diretorio_projeto, "src")

    # Criar os diretórios do projeto
    os.makedirs(diretorio_projeto)
    os.makedirs(os.path.join(diretorio_src, "css"))
    os.makedirs(os.path.join(diretorio_src, "js"))

    # Criar arquivo index.html com Bootstrap 5
    with open(os.path.join(diretorio_src, "index.html"), 'w') as f:
        f.write("""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Novo Projeto</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MX9ukpa0CIzCxMJj20f3W8SlCRtx" crossorigin="anonymous">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>Olá, mundo!</h1>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT8cxR5BNqE+WXoNA2jlpyT5o+f0zIzsX/ykjobe9T5qnxK" crossorigin="anonymous"></script>
    <script src="js/script.js"></script>
</body>
</html>""")

    # Criar arquivo css/style.css
    with open(os.path.join(diretorio_src, "css", "style.css"), 'w') as f:
        f.write("/* Estilos personalizados aqui */")

    # Criar arquivo js/script.js
    with open(os.path.join(diretorio_src, "js", "script.js"), 'w') as f:
        f.write("// JavaScript personalizado aqui")

    print(f"Projeto '{nome_projeto}' criado com sucesso em: {diretorio_projeto}")

# Função para buildar um projeto existente
def buildar_projeto(nome_projeto):
    diretorio_projeto = os.path.join(diretorio_projetos, nome_projeto)
    diretorio_origem = os.path.join(diretorio_projeto, "src")
    diretorio_destino = os.path.join(diretorio_projeto, "dist")

    # Criar o diretório de destino se ele não existir
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Percorrer os arquivos e diretórios na pasta de origem
    for pasta_raiz, _, arquivos in os.walk(diretorio_origem):
        pasta_relativa = os.path.relpath(pasta_raiz, diretorio_origem)
        nova_pasta = os.path.join(diretorio_destino, pasta_relativa)

        # Criar a pasta no diretório de destino se ela não existir
        if not os.path.exists(nova_pasta):
            os.makedirs(nova_pasta)

        for arquivo in arquivos:
            caminho_origem = os.path.join(pasta_raiz, arquivo)
            caminho_destino = os.path.join(nova_pasta, arquivo)

            # Processar e copiar o arquivo
            processar_arquivo(arquivo, caminho_origem, caminho_destino)

    print(f"Build do projeto '{nome_projeto}' finalizado em: {diretorio_destino}")

# Função para analisar argumentos da linha de comando
def analisar_argumentos():
    parser = argparse.ArgumentParser(description="Crie e faça o build de protótipos web rápidos com Bootstrap 5.")
    subparsers = parser.add_subparsers(dest="comando", required=True, help="Comando para executar")

    # Comando "criar"
    parser_criar = subparsers.add_parser("criar", help="Crie um novo projeto")
    parser_criar.add_argument("nome_projeto", help="Nome do projeto")

    # Comando "buildar"
    parser_buildar = subparsers.add_parser("buildar", help="Faça o build de um projeto existente")
    parser_buildar.add_argument("nome_projeto", help="Nome do projeto")

    return parser.parse_args()

# Função principal
def main():
    args = analisar_argumentos()

    if args.comando == "criar":
        criar_projeto(args.nome_projeto)
    elif args.comando == "buildar":
        buildar_projeto(args.nome_projeto)

if __name__ == "__main__":
    main()