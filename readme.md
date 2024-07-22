## QuickWebPrototype

Um script Python simples para criar e buildar protótipos web rápidos com Bootstrap 5.

### Funcionalidades

- **Criação de projetos:** Gere um novo projeto com estrutura de pastas básica e arquivos HTML, CSS e JavaScript.
- **Bootstrap 5:** Inclui o Bootstrap 5 no projeto para um desenvolvimento front-end mais rápido.
- **Minificação:** Minifica arquivos HTML, CSS e JavaScript durante o processo de build para melhor desempenho.
- **Interface de linha de comando:** Use comandos simples para criar e buildar seus projetos.

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/QuickWebPrototype.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

### Utilização

1. **Criar um novo projeto:**
   ```bash
   python QuickWebPrototype.py criar nome-do-projeto
   ```
   Substitua `nome-do-projeto` pelo nome desejado para o seu projeto.

2. **Buildar o projeto:**
   ```bash
   python QuickWebPrototype.py buildar nome-do-projeto
   ```
   Substitua `nome-do-projeto` pelo nome do projeto que você deseja buildar.

### Estrutura de pastas

```
projetos/
  nome-do-projeto/
    src/
      css/
        style.css
      js/
        script.js
      index.html
    dist/
      # Arquivos minificados
```

### Personalização

- **HTML, CSS e JavaScript:** Adicione seu próprio código HTML, CSS e JavaScript nos arquivos `index.html`, `style.css` e `script.js` dentro da pasta `src`.
- **Bootstrap:** Personalize o Bootstrap 5 modificando o arquivo `style.css` ou adicionando seus próprios estilos.

### Contribuindo

Sinta-se à vontade para contribuir com o projeto! Abra um problema ou envie um pull request com suas sugestões.

### Licença

Este projeto está licenciado sob a licença MIT.

**Observações:**

- Substitua `seu-usuario` no link do repositório pelo seu nome de usuário do GitHub.
- Crie um arquivo chamado `requirements.txt` na raiz do projeto com o seguinte conteúdo:
  ```
  htmlmin
  cssmin
  jsmin
  ```
- Renomeie o arquivo do script para `QuickWebPrototype.py`.

