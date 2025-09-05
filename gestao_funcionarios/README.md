# Sistema de Gestão de Funcionários

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-2C5E7E?style=for-the-badge&logo=tkinter&logoColor=white)

Este é um projeto de software desktop desenvolvido como um exercício prático para aplicar conceitos fundamentais de Programação Orientada a Objetos (POO) com Python. A aplicação permite o cadastro de diferentes tipos de funcionários e calcula seus salários com base em regras de negócio específicas para cada cargo.

## ✨ Principais Funcionalidades

* **Cadastro de Funcionários:** Interface gráfica para registrar novos funcionários.
* **Diferentes Tipos de Cargos:** O sistema distingue entre funcionários **Administrativos**, **Professores** e **Técnicos**.
* **Cálculo de Salário Polimórfico:** Cada classe de funcionário possui seu próprio método para calcular o salário final, adicionando bônus específicos:
    * **Administrativo:** Salário base + Bônus fixo.
    * **Professor:** Salário base + Bônus percentual.
    * **Técnico:** Salário base + Bônus fixo por periculosidade.
* **Interface Gráfica Moderna:** Desenvolvida com `tkinter` e estilizada com a biblioteca `ttkbootstrap` para uma aparência amigável.
*  **Atualização - 04/09 :** - Adição de Menu dinâmico à lacuna de "cargos" com acionamento de campos específicos de cada classe de funcionário
                             - Inserção de campos para melhor diferenciação de funcionários (CPF) e

## 🚀 Tecnologias Utilizadas

* **Python 3:** Linguagem principal do projeto.
* **Tkinter:** Biblioteca padrão do Python para a criação da interface gráfica (GUI).
* **ttkbootstrap:** Biblioteca para aplicação de temas modernos e widgets estilizados sobre o Tkinter.

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação em seu ambiente local.

### Pré-requisitos

* Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado em seu sistema.
* É necessário ter o [Git](https://git-scm.com/downloads) instalado para clonar o repositório.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/](https://github.com/)[SEU_USUARIO]/[SEU_REPOSITORIO].git
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd desenv_software
    ```

3.  **Instale as dependências necessárias:**
    A única dependência externa é o `ttkbootstrap`. Instale-a usando o pip:
    ```bash
    pip install ttkbootstrap
    ```

4.  **Execute a Aplicação:**
    O arquivo principal que inicia a interface gráfica é o `Main.py` dentro do pacote `gestao_funcionarios`. Execute-o com o seguinte comando a partir da pasta `desenv_software`:
    ```bash
    python gestao_funcionarios/Main.py
    ```
    *(Dependendo do seu sistema, você pode precisar usar `python3` em vez de `python`)*

## 🎓 Objetivos de Aprendizado do Projeto

Este projeto serviu como uma ferramenta prática para estudar e aplicar os seguintes conceitos:

* **Programação Orientada a Objetos (POO):**
    * **Herança:** Criação de uma classe base `Funcionario` e classes filhas especializadas.
    * **Polimorfismo:** Implementação de um mesmo método (`calcular_salario`) com comportamentos diferentes em cada classe filha.
    * **Encapsulamento:** Organização da lógica de negócios dentro das classes apropriadas.
* **Desenvolvimento de Interface Gráfica (GUI):** Uso do Tkinter para criar janelas, labels, campos de entrada, botões e menus.
* **Estruturação de Projetos em Python:** Separação do código em diferentes módulos e criação de um pacote para a lógica de negócio.
* **Versionamento de Código:** Utilização de Git e GitHub para controle de versão e armazenamento do projeto, seguindo o fluxo de commit e push.

---

Desenvolvido como parte de um estudo prático em desenvolvimento de software.
