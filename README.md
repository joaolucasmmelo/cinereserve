# 🎬 CineReserve API

Uma API RESTful robusta projetada para o gerenciamento de sessões de cinema e reserva de assentos em ambientes de alta concorrência. O sistema garante a integridade das transações e evita condições de corrida (*race conditions*) durante a compra de ingressos.

## 🚀 Tecnologias e Ferramentas
* **Linguagem & Framework:** Python 3.13 | Django 6.0.3 | Django REST Framework
* **Banco de Dados Relacional:** PostgreSQL 15 (Armazenamento definitivo e integridade de dados)
* **Cache & Mensageria:** Redis (Implementação de *Distributed Locks* para reservas voláteis)
* **Autenticação:** JWT (JSON Web Tokens via `djangorestframework-simplejwt`)
* **Infraestrutura:** Docker & Docker Compose (Ambiente 100% conteinerizado)
* **Gerenciamento de Dependências:** Poetry

## ⚙️ Arquitetura e Decisões Técnicas

Para simular o desafio real de um sistema de bilheteria, a arquitetura foi dividida para tratar a concorrência de forma eficiente:
1. **Visualização em Tempo Real:** O mapa de assentos cruza os dados persistidos no PostgreSQL (compras definitivas) com as chaves em memória no Redis (reservas temporárias).
2. **Distributed Lock (Redis):** Quando um usuário tenta reservar um assento, o Redis aplica um *lock* atômico de 10 minutos vinculado ao ID do usuário. Isso impede que dois clientes reservem a mesma poltrona no mesmo milissegundo, aliviando o banco de dados relacional de *row-level locks* complexos.
3. **Paginação:** Implementada em recursos de listagem (Filmes, Sessões) para garantir performance e escalabilidade no consumo da API por clientes frontend ou mobile.

## 🗂️ Endpoints Principais

A API está estruturada seguindo boas práticas RESTful. Abaixo estão os escopos principais:

* **Autenticação:**
  * `POST /register/` - Cadastro de novos usuários.
  * `POST /login/` - Autenticação e geração do par de tokens JWT (Access/Refresh).
* **Catálogo:**
  * `GET /movies/` - Lista todos os filmes em cartaz (Paginado).
  * `GET /movies/<id>/sessions/` - Lista as sessões disponíveis para um filme específico.
* **Reserva e Compra:**
  * `GET /sessions/<id>/seats/` - Retorna o mapa completo de assentos e seus status atuais (Disponível, Reservado, Comprado).
  * `POST /sessions/<id>/seats/<seat_number>/reserve/` - Aplica a trava de 10 minutos na poltrona.
  * `POST /sessions/<id>/seats/<seat_number>/buy/` - Efetiva a compra, atualiza o banco relacional e libera a memória do Redis.

## 🛠️ Como Executar o Projeto Localmente

O projeto foi configurado para oferecer uma experiência *Plug-and-Play*. Todo o ambiente (Aplicação, Banco de Dados, Redis e PgAdmin) subirá automaticamente.

**1. Clone o repositório:**
```bash
git clone [https://github.com/seu-usuario/cinereserve.git](https://github.com/seu-usuario/cinereserve.git)
cd cinereserve