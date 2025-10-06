# Desafio de Estágio - Laboratório Vortex

Aplicação web de página única (SPA) que implementa um sistema de cadastro de usuários com pontuação por indicação, desenvolvida como parte do processo seletivo do Laboratório Vortex. O projeto foi construído do zero em aproximadamente 2 dias, com foco em boas práticas, resolução de problemas e habilidades fundamentais de desenvolvimento web.

---

## Funcionalidades

A aplicação implementa todos os requisitos funcionais solicitados no desafio:

-   **Cadastro de Usuários:** Formulário seguro para registro de novos usuários com nome, e-mail e senha.
-   **Validação Robusta:** Validação de dados tanto no front-end (para feedback imediato) quanto no back-end (para integridade dos dados), incluindo formato de e-mail e complexidade da senha.
-   **Página de Perfil:** Após o cadastro, o usuário acessa uma página de perfil que exibe dinamicamente seu nome, pontuação e link de indicação exclusivo.
-   **Sistema de Pontos por Indicação:** Um novo usuário que se cadastra através do link de outro concede 1 ponto ao indicador. A pontuação é refletida na página de perfil ao recarregá-la.
-   **Componente "Copiar Link":** Um botão funcional e estilizado que copia o link de indicação para a área de transferência do usuário.
-   **Design Responsivo e Moderno:** A interface foi construída com CSS puro, utilizando um tema escuro e se adaptando de forma fluida a desktops e dispositivos móveis.

---

## Tecnologias Utilizadas

As tecnologias foram selecionadas com base nos requisitos do desafio, focando em performance, segurança e uma base de código limpa.

### Back-end

-   **Python 3:** Linguagem escolhida pela sua sintaxe clara, vasta biblioteca padrão e forte ecossistema para desenvolvimento web.
-   **FastAPI:** Framework de alta performance para a construção da API REST. Foi escolhido para acelerar a curva de aprendizado em um novo framework (vindo de um background em Django e Streamlit), aproveitando sua documentação automática para testes e a validação nativa com Pydantic para um código mais seguro.
-   **SQLAlchemy:** ORM para a comunicação com o banco de dados, escolhido por sua flexibilidade e por abstrair o SQL, permitindo focar na lógica de negócio.
-   **SQLite:** Banco de dados relacional selecionado pela sua simplicidade, ideal para um ambiente de desenvolvimento ágil por não exigir um servidor separado.
-   **Passlib com PBKDF2_SHA256:** Biblioteca utilizada para a criptografia de senhas. O algoritmo `pbkdf2_sha256` foi uma escolha deliberada para garantir estabilidade, após serem encontrados desafios de compatibilidade com `bcrypt` no ambiente de desenvolvimento.

### Front-end

-   **HTML5 / CSS3 / JavaScript (Puro):** O front-end foi construído sem frameworks para atender à "Pegadinha 1" do desafio e demonstrar proficiência nas tecnologias fundamentais da web. Foram utilizadas features modernas como Variáveis CSS e Flexbox para criar uma interface responsiva e de fácil manutenção.

---

## Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação localmente.

**Pré-requisitos:**
-   [Python 3.10+](https://www.python.org/downloads/) instalado.
-   [Git](https://git-scm.com/downloads) instalado.

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Thales1914/vortex.git](https://github.com/Thales1914/vortex.git)
    cd vortex
    ```

2.  **Configure e rode o Back-end:**
    ```bash
    # Navegue para a pasta do back-end
    cd backend

    # Crie e ative um ambiente virtual
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate

    # Instale as dependências
    pip install -r requirements.txt

    # Inicie o servidor
    uvicorn app.main:app --reload
    ```
    O back-end estará rodando em `http://127.0.0.1:8000`.

3.  **Abra o Front-end:**
    -   Mantenha o terminal do back-end rodando.
    -   Abra a pasta do projeto no VS Code.
    -   Navegue até a pasta `frontend/`.
    -   Clique com o botão direito no arquivo `index.html` e o abra com a extensão **"Live Server"**.

---

## Colaboração com IA

Conforme encorajado no desafio, utilizei o Gemini como assistente de IA ao longo de todo o ciclo de vida deste projeto.

-   **Para quais partes do projeto você usou a IA?**
    1.  **Estruturação e Código Base:** Utilizei a IA para gerar a estrutura inicial do projeto em FastAPI — incluindo configuração de banco de dados e schemas Pydantic — para acelerar o desenvolvimento, dado meu background em outras ferramentas como Django e Streamlit.
    2.  **Debugging Intensivo e Resolução de Problemas:** Esta foi a colaboração mais crítica. A IA foi essencial para diagnosticar e resolver desafios técnicos, como o erro de `ValueError` causado pelo limite de 72 bytes do `bcrypt`. Após o diagnóstico, a IA sugeriu a troca do algoritmo de hashing para `pbkdf2_sha256`, o que resolveu o problema de forma robusta.
    3.  **Desenvolvimento do Front-end:** Tendo maior foco em back-end, utilizei a IA como uma "consultora de design" para a estilização com CSS. Ela foi fundamental para gerar o tema escuro, sugerir o uso de variáveis CSS para fácil manutenção e criar o componente do link de indicação com Flexbox, resultando em uma interface mais profissional do que eu conseguiria criar sozinho no mesmo tempo.

-   **O que você aprendeu com essa interação?**
    A colaboração com a IA foi uma experiência de aprendizado acelerado. Tecnicamente, solidifiquei meu entendimento sobre o funcionamento do CORS, a importância da gestão de dependências em Python e como diagnosticar problemas de rede no navegador. Metodologicamente, aprendi a abordar o debugging de forma mais sistemática: analisar a mensagem de erro, verificar o console do navegador, checar o log do servidor e isolar o problema com testes controlados. O mais importante foi aprender a usar a IA como uma ferramenta estratégica de "pair programming": em vez de pedir respostas prontas, passei a apresentar o problema, analisar as sugestões e pedir explicações sobre a causa raiz, transformando cada erro em uma oportunidade de aprendizado.

---

## Autor

Desenvolvido por **Thales Matos Barbosa**.