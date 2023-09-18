# Projeto de Gerenciamento de Variáveis Sensíveis

## Case

Link: [Ei, posso te contar um segredo?](https://www.linkedin.com/posts/lucianovasconcelosf_armazene-e-gerencie-segredos-como-chaves-activity-7109479947571769344-ptQe?utm_source=share&utm_medium=member_desktop)

Este projeto demonstra três abordagens diferentes para gerenciar informações sensíveis em aplicações Python:

## Descrição das Abordagens

1. **Versão Hardcode (main.py)**
    
    Nesta versão, as variáveis sensíveis como chaves, senhas e outras informações são hardcoded diretamente no código. Esta prática não é recomendada, pois expõe informações valiosas e dificulta a manutenção e a portabilidade do código.

    ```python
    #DADOS SENSÍVEIS
    EMAIL = 'lvgalvaofilho@gmail.com'
    PASSWORD = 'senha123'

    #MEUS SEGREDOS
    OPENAI_KEY = "openai-XYZABCDE"
    AWS_SECRET = "aws-s3cr3tk3y"
    
    #MEU APP
    print(f"Meu email: {EMAIL}")
    print(f"Minha senha: {PASSWORD}")
    print(f"Minha Key Open AI: {OPENAI_KEY}")
    print(f"Minha AWS Key: {AWS_SECRET}")
    ```
    
2. **Versão Export (main_02.py)**
    
    Aqui, as variáveis sensíveis são definidas através do comando `export` no terminal, tornando-as variáveis de ambiente da sessão atual. Esta abordagem é mais segura do que o hardcoding, mas as variáveis precisam ser redefinidas sempre que uma nova sessão é iniciada.
    
    Exemplo:
    
    ```bash
    export EMAIL=lvgalvaofilho@gmail.com
    export PASSWORD=senha123
    export AWS_SECRET=aws-s3cr3tk3y
    export OPENAI_KEY=openai-XYZABCDE
    ```

    ```python
    import os

    #DADOS SENSÍVEIS
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    #MEUS SEGREDOS
    openai_key = os.getenv('OPENAI_KEY')
    aws_secret = os.getenv('AWS_SECRET')
    
    #MEU APP
    print(f"Meu email: {email}")
    print(f"Minha senha: {password}")
    print(f"Minha Key Open AI: {openai_key}")
    print(f"Minha AWS Key: {aws_secret}")
    ```
    
3. **Versão dotenv (main_03.py)**
    
    Esta é uma abordagem popular e recomendada para gerenciar informações sensíveis. Utiliza a biblioteca `dotenv` para carregar variáveis de um arquivo `.env` no diretório do projeto. Este arquivo não deve ser incluído no controle de versão (ex.: git), garantindo a segurança das informações.
    
    Exemplo de arquivo `.env`:
    
    ```makefile
    EMAIL=lvgalvaofilho@gmail.com
    PASSWORD=senha123
    AWS_SECRET=aws-s3cr3tk3y
    OPENAI_KEY=openai-XYZABCDE
    ```
    
    ```python
    import os
    from dotenv import load_dotenv

    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # DADOS SENSÍVEIS
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    # MEUS SEGREDOS
    openai_key = os.getenv('OPENAI_KEY')
    aws_secret = os.getenv('AWS_SECRET')
    
    #MEU APP
    print(f"Meu email: {email}")
    print(f"Minha senha: {password}")
    print(f"Minha Key Open AI: {openai_key}")
    print(f"Minha AWS Key: {aws_secret}")
    ```
    
    No código, as variáveis são carregadas através da biblioteca `dotenv`.
    

## Recomendações

* Nunca faça commit do arquivo `.env` ou de qualquer arquivo que contenha informações sensíveis em repositórios públicos.
* Utilize sempre uma abordagem segura para gerenciar informações sensíveis. A versão `dotenv` é altamente recomendada para muitos projetos.
* Evite o uso de hardcoding para variáveis sensíveis em todos os momentos.
