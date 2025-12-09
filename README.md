# Python_USP

Resumo
- Coleção de exercícios e pequenos programas em Python (módulos, testes e scripts) usados em aulas/treinos.

Estrutura (resumida)
- modulo_4/ — exercícios e testes do módulo 4 (ex.: teste.py, primalidade.py, scripts de jogo).
- .gitignore — ignora ambientes virtuais e arquivos temporários.
- README.md — este arquivo.

Requisitos
- macOS com Python 3.8+ instalados.
- pytest para testes (opcional, recomendado).

Configurar ambiente (macOS)
1. Criar e ativar venv:
    python3 -m venv venv
    source venv/bin/activate
2. Instalar dependências (se houver):
    pip install -r requirements.txt

Obs: o diretório venv já está listado em .gitignore para não comitar o ambiente.

Executar scripts
- Rodar um script qualquer:
    python3 modulo_4/teste.py
- Exemplo (primalidade):
    python3 modulo_4/primalidade.py
  Forneça a entrada quando solicitado no terminal.

Testes (pytest)
- Rodar todos os testes:
    python3 -m pytest -q
- Rodar um arquivo de teste específico:
    python3 -m pytest -q modulo_4/test_fatorial.py
- Se pytest reportar "collected 0 items", verifique se o arquivo contém funções cujo nome começa com `test_`.

Boas práticas
- Não usar prompts no input() para códigos que serão avaliados automaticamente (usar `input()` sem string).
- Funções devem ser testáveis sem depender de input()/print() — separar lógica e I/O facilita testes.

Contribuição
- Criar branch, adicionar testes para nova funcionalidade e abrir PR.
- Antes de commitar, certifique-se de que venv não está no índice do Git:
    git rm -r --cached venv
    git add .gitignore
    git commit -m "Ignore venv"

Contato
- Arquivos e dúvidas: inspecione os testes e scripts em `modulo_4/`.
