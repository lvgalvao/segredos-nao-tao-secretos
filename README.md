# Projeto de Gerenciamento de Variáveis Sensíveis

Este projeto demonstra três abordagens diferentes para gerenciar informações sensíveis em aplicações Python:

## Descrição das Abordagens

1. **Versão Hardcode (main.py)**
    
    Nesta versão, as variáveis sensíveis como chaves, senhas e outras informações são hardcoded diretamente no código. Esta prática não é recomendada, pois expõe informações valiosas e dificulta a manutenção e a portabilidade do código.
    
2. **Versão Export (main_02.py)**
    
    Aqui, as variáveis sensíveis são definidas através do comando `export` no terminal, tornando-as variáveis de ambiente da sessão atual. Esta abordagem é mais segura do que o hardcoding, mas as variáveis precisam ser redefinidas sempre que uma nova sessão é iniciada.
    
    Exemplo:
    
    ```bash
    export VARIAVEL_SECRETA="meu_valor_secreto"
    ```
    
3. **Versão dotenv (main_03.py)**
    
    Esta é uma abordagem popular e recomendada para gerenciar informações sensíveis. Utiliza a biblioteca `dotenv` para carregar variáveis de um arquivo `.env` no diretório do projeto. Este arquivo não deve ser incluído no controle de versão (ex.: git), garantindo a segurança das informações.
    
    Exemplo de arquivo `.env`:
    
    ```makefile
    VARIAVEL_SECRETA=meu_valor_secreto
    OUTRA_VARIAVEL=outro_valor
    ```
    
    No código, as variáveis são carregadas através da biblioteca `dotenv`.
    

## Recomendações

* Nunca faça commit do arquivo `.env` ou de qualquer arquivo que contenha informações sensíveis em repositórios públicos.
* Utilize sempre uma abordagem segura para gerenciar informações sensíveis. A versão `dotenv` é altamente recomendada para muitos projetos.
* Evite o uso de hardcoding para variáveis sensíveis em todos os momentos.