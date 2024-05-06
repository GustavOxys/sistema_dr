# DASHBOARD PARA CONSULTÓRIO MÉDICO

**Este é um projeto de dashboard para um consultório médico, desenvolvido utilizando Django no backend e HTML, CSS e JavaScript para o frontend. Este foi meu primeiro projeto, onde aprendi muitas coisas por conta própria.**

## VISÃO GERAL

O dashboard oferece uma interface intuitiva para gerenciamento de pacientes, consultas, prontuários e convênios de um consultório médico. Os usuários podem se registrar, fazer login e acessar várias funcionalidades do sistema.

## FUNCIONALIDADES PRINCIPAIS

- **Autenticação de Usuário**: Os usuários podem se registrar e fazer login para acessar o sistema.
- **Gestão de Pacientes**: Os usuários podem cadastrar novos pacientes e visualizar informações dos pacientes existentes.
- **Agendamento de Consultas**: É possível agendar consultas para os pacientes, definindo data, horário e informações relevantes.
- **Criação de Prontuários**: Durante a consulta, os usuários podem criar prontuários detalhados para os pacientes.
- **Gestão de Convênios**: Os usuários podem adicionar e gerenciar informações sobre convênios médicos.
- **Dashboard Estatístico**: O painel exibe informações como atendimentos diários e mensais, agendamentos diários e receita mensal com base nos valores adicionados nos convênios.

## ESTADO DO PROJETO

Este projeto ainda está em desenvolvimento e pode conter bugs. Sinta-se à vontade para usar e explorar as funcionalidades disponíveis. Qualquer feedback ou contribuição é bem-vindo!

## INSTALAÇÃO E USO

1. Crie uma Virtual Environment (venv) para o projeto:
    ```
    python -m venv myenv
    ```

2. Ative a venv:
    - No Windows:
        ```
        myenv\Scripts\activate
        ```
    - No Linux/Mac:
        ```
        source myenv/bin/activate
        ```

3. Clone este repositório em sua máquina local:
    ```
    git clone <URL do Repositório>
    ```

4. Navegue até o diretório do projeto:
    ```
    cd nome_do_projeto
    ```

5. Certifique-se de ter o Python e o Django instalados na sua venv:
    ```
    pip install django
    ```

6. Instale as dependências do projeto:
    ```
    pip install -r requirements.txt
    ```

7. Execute as migrações do banco de dados:
    ```
    python manage.py migrate
    ```

8. Inicie o servidor de desenvolvimento:
    ```
    python manage.py runserver
    ```

9. Acesse o dashboard em seu navegador, geralmente em `http://localhost:8000`.

## CONTRIBUIÇÃO

Se você deseja contribuir para este projeto, por favor, abra uma issue para discutir suas ideias ou envie uma solicitação de pull request com suas alterações propostas. Todas as contribuições são bem-vindas!

## CONTATO

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato comigo através do email gustavohzmdev@gmail.com
