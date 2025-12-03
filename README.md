# Projeto 2 - Docker e Microsserviços

Este repositório contém a implementação prática de 5 desafios focados em Docker, Orquestração e Microsserviços.

## Estrutura do Projeto

O projeto está dividido em pastas independentes para cada desafio, contendo seus próprios arquivos de configuração (`Dockerfile`, `docker-compose.yml`) e documentação específica.

### [Desafio 1: Containers em Rede](./desafio1)
- Comunicação entre dois contêineres (Cliente/Servidor) via rede bridge customizada.
- **Tecnologias:** Python, Docker Network.

### [Desafio 2: Volumes e Persistência](./desafio2)
- Demonstração de persistência de dados usando Docker Volumes.
- **Tecnologias:** Python, Bind Mounts.

### [Desafio 3: Orquestração com Docker Compose](./desafio3)
- Orquestração de uma aplicação Web com Cache (Redis) e Banco de Dados (Postgres).
- **Tecnologias:** Flask, Redis, Postgres, Docker Compose.

### [Desafio 4: Microsserviços Independentes](./desafio4)
- Comunicação direta HTTP entre dois microsserviços (Provedor e Consumidor).
- **Tecnologias:** Flask, Requests.

### [Desafio 5: Microsserviços com API Gateway](./desafio5)
- Implementação de um API Gateway (Nginx) para centralizar acesso a serviços de back-end.
- **Tecnologias:** Nginx, Flask, Docker Compose.

## Pré-requisitos Gerais

Para executar os desafios, você precisará ter instalado:
- **Docker Engine**
- **Docker Compose** (Geralmente incluído no Docker Desktop ou via plugin `docker compose`).

## Como Navegar

Entre na pasta de cada desafio e leia o arquivo `README.md` local para instruções detalhadas de execução.

Exemplo:
```bash
cd desafio1
cat README.md
```
