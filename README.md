# 🃏 Truco em Python

Projeto de desenvolvimento de uma plataforma de **Truco** utilizando Python, inicialmente executada pelo terminal e planejada para futuramente receber uma **interface gráfica e versão para dispositivos móveis**.

O objetivo do projeto é, além de construir um jogo funcional, praticar conceitos de **Programação Orientada a Objetos (POO)**, organização de projetos, lógica de programação, Git e arquitetura de software.

---

## 🎯 Objetivos

* Desenvolver um jogo de Truco funcional em Python.
* Praticar Programação Orientada a Objetos.
* Trabalhar com classes, objetos, atributos e métodos.
* Desenvolver uma arquitetura organizada e de fácil manutenção.
* Utilizar Git e GitHub para versionamento.
* Implementar progressivamente as regras do Truco.
* Criar inicialmente uma interface via terminal.
* Futuramente desenvolver uma interface gráfica.
* Preparar a estrutura para uma possível versão mobile.

---

## 🏗️ Estrutura do projeto

```text
truco-python/
│
├── main.py
│
├── truco/
│   ├── __init__.py
│   ├── carta.py
│   ├── baralho.py
│   ├── jogador.py
│   ├── rodada.py
│   └── jogo.py
│
├── .gitignore
│
└── README.md
```

### Principais classes

#### 🃏 `Carta`

Representa uma carta do baralho.

Responsável por armazenar informações como:

* valor;
* naipe.

---

#### 🎴 `Baralho`

Representa o baralho utilizado durante o jogo.

Responsável por operações como:

* criação das cartas;
* embaralhamento;
* retirada de cartas.

---

#### 👤 `Jogador`

Representa um jogador da partida.

Responsável por:

* armazenar suas cartas;
* receber cartas;
* jogar cartas;
* futuramente armazenar informações relacionadas à pontuação.

---

#### 🔄 `Rodada`

Representa uma mão de Truco.

Responsável por coordenar elementos como:

* baralho da rodada;
* distribuição das cartas;
* vira;
* cartas jogadas;
* jogador atual;
* futuramente, determinação do vencedor de cada rodada.

A **manilha é determinada a partir da vira**, não sendo necessário armazená-la como um atributo independente.

---

#### 🎮 `Jogo`

Responsável por coordenar a partida.

Entre suas responsabilidades estão:

* criar os jogadores;
* iniciar uma rodada;
* controlar o fluxo geral da partida;
* futuramente controlar a pontuação e o sistema de Truco.

---

## 🧠 Arquitetura

O projeto está sendo desenvolvido separando a **lógica do jogo** da **interface**.

Inicialmente, o terminal será utilizado para interação com o jogador.

```text
              ┌──────────────────┐
              │    Interface     │
              │     Terminal     │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │      Jogo        │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │     Rodada       │
              └────────┬─────────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
        ┌───────────┐      ┌───────────┐
        │  Baralho  │      │ Jogadores │
        └─────┬─────┘      └───────────┘
              │
              ▼
        ┌───────────┐
        │   Carta   │
        └───────────┘
```

A intenção é que a lógica do jogo não dependa diretamente da interface.

Dessa forma, futuramente será possível substituir o terminal por uma interface gráfica sem precisar reconstruir completamente o funcionamento interno do jogo.

---

## 🎮 Funcionamento planejado

O fluxo básico de uma mão será:

```text
Iniciar jogo
     ↓
Criar baralho
     ↓
Embaralhar
     ↓
Distribuir cartas
     ↓
Definir a vira
     ↓
Determinar a manilha
     ↓
Jogador escolhe uma carta
     ↓
Computador joga
     ↓
Comparar cartas
     ↓
Determinar vencedor
     ↓
Repetir até definir a mão
```

Posteriormente será implementado o sistema de aumento de pontos:

```text
1 → 3 → 6 → 9 → 12
```

incluindo as decisões relacionadas ao **Truco**.

---

## 🚧 Status do projeto

### Em desenvolvimento

* [x] Estrutura inicial do projeto
* [x] Classe `Carta`
* [x] Classe `Baralho`
* [x] Classe `Jogador`
* [x] Classe `Jogo`
* [x] Classe `Rodada`
* [x] Distribuição de cartas
* [x] Definição da vira
* [ ] Interface funcional no terminal
* [ ] Escolha de cartas pelo jogador
* [ ] Jogada do computador
* [ ] Comparação entre cartas
* [ ] Sistema de manilhas
* [ ] Determinação do vencedor da rodada
* [ ] Sistema de pontuação
* [ ] Sistema de Truco
* [ ] Inteligência do computador
* [ ] Testes automatizados
* [ ] Interface gráfica
* [ ] Versão para dispositivos móveis

---

## 🛠️ Tecnologias

* **Python**
* **Git**
* **GitHub**
* **PyCharm**

Tecnologias para interface gráfica/mobile serão definidas posteriormente.

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta:

```bash
cd truco-python
```

Crie ou utilize o ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual no Linux:

```bash
source .venv/bin/activate
```

Execute o projeto:

```bash
python main.py
```

---

## 📌 Versionamento

O projeto utiliza Git para acompanhar a evolução do desenvolvimento.

Os commits são organizados por funcionalidades, por exemplo:

```text
feat: cria classe Carta
feat: cria classe Baralho
feat: adiciona distribuição de cartas
feat: cria classe Jogador
feat: cria classe Rodada
feat: adiciona definição da vira
feat: implementa comparação de cartas
feat: implementa sistema de truco
```

A ideia é manter cada etapa do desenvolvimento registrada, permitindo acompanhar a evolução do projeto e retornar facilmente para versões anteriores.

---

## 🚀 Futuro do projeto

O objetivo final é transformar o projeto em uma **plataforma de Truco**, indo além da implementação inicial no terminal.

Possíveis evoluções:

```text
Terminal
   ↓
Interface gráfica
   ↓
Aplicativo
   ↓
Multiplayer
   ↓
Sistema de partidas online
```

A arquitetura será desenvolvida desde o início buscando manter a lógica do jogo independente da interface, facilitando essas futuras expansões.

---

## 📚 Propósito

Este projeto possui também um propósito educacional.

Através dele serão praticados conceitos como:

* Programação Orientada a Objetos;
* encapsulamento;
* composição entre classes;
* estruturas de dados;
* algoritmos;
* lógica de jogos;
* arquitetura de software;
* tratamento de erros;
* testes;
* Git e GitHub;
* desenvolvimento de interfaces;
* posteriormente, desenvolvimento mobile.

> **Construir algo pequeno, funcional e evoluir progressivamente.**

---
