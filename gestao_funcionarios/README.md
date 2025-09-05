# Sistema de Gestão de Funcionários

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-2C5E7E?style=for-the-badge&logo=tkinter&logoColor=white)

Exercício prático para aplicar conceitos fundamentais de Programação Orientada a Objetos (POO) com Python. A aplicação permite o cadastro de diferentes tipos de funcionários, calcula seus salários com base em regras específicas e exibe os cadastros em tempo real.

## ✨ Principais Funcionalidades

* **Cadastro de Funcionários:** Interface gráfica para registrar novos funcionários.
* **Diferentes Tipos de Cargos:** O sistema distingue entre funcionários **Administrativos**, **Professores** e **Técnicos**.
* **Cálculo de Salário Polimórfico:** Cada classe de funcionário possui seu próprio método para calcular o salário final, adicionando bônus específicos.
* **Interface Gráfica Dinâmica:** O formulário de entrada se adapta em tempo real ao cargo selecionado, mostrando apenas os campos necessários.
* **Visualização de Dados:** Os funcionários cadastrados são exibidos em uma tabela na tela principal.
* **Validação de Dados:** O sistema impede o cadastro de funcionários com o mesmo CPF.
* **Interface Moderna:** Desenvolvida com `tkinter` e estilizada com a biblioteca `ttkbootstrap` para uma aparência amigável.

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

## Atualizações

* **04/09/2025:**
    * Implementada a funcionalidade de **interface dinâmica**, onde o formulário se adapta ao cargo selecionado.
    * Adicionada a **validação para impedir o cadastro de CPFs duplicados**.
    * Criada uma **tabela de visualização** para exibir os funcionários cadastrados em tempo real.
    * Organização da estrutura do código no `Main.py` para melhor organização e legibilidade.

## 🎓 Objetivos de Aprendizado da Tarefa

* **Programação Orientada a Objetos (POO):**
    * **Herança:** Criação de uma classe base `Funcionario` e classes filhas especializadas.
    * **Polimorfismo:** Implementação de um mesmo método (`calcular_salario`) com comportamentos diferentes em cada classe filha.
    * **Encapsulamento:** Separação da lógica de gerenciamento de dados (`GerenciadorFuncionarios`) da camada de apresentação (GUI).
* **Desenvolvimento de Interface Gráfica (GUI):** Uso do Tkinter para criar janelas, widgets dinâmicos e visualização de dados em tabelas (`Treeview`).
* **Estruturação de Projetos em Python:** Separação do código em diferentes módulos e criação de um pacote para a lógica de negócio.
* **Versionamento de Código:** Utilização de Git e GitHub para controle de versão e armazenamento do projeto.

---

Desenvolvido como parte de um estudo prático em desenvolvimento de software.
