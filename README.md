# Projeto 2 - Docker e Microsserviços (Variante B)

Este repositório implementa os desafios da "Variante B" para o projeto de Docker e Microsserviços.

## Detalhes da Implementação da Variante B

1.  **Gateway em Nível de Aplicação (Desafio 5):**
    -   Em vez de usar Nginx, o API Gateway é implementado como uma **Aplicação Python Flask**. Isso fornece flexibilidade para lógica personalizada, autenticação ou transformação no nível do gateway usando código Python padrão.

2.  **Persistência Baseada em Arquivo (Desafio 2):**
    -   Para demonstrar a mecânica de volumes sem a complexidade de sistemas de gerenciamento de banco de dados, utilizamos um **Armazenamento Baseado em Arquivo**. A aplicação grava logs em um arquivo de texto em um volume montado, provando que arquivos em disco sobrevivem aos ciclos de vida dos containers.

3.  **Redes:**
    -   Redes bridge personalizadas (`custom_bridge_v2`, `backend_net`, `microservices_net`, `gateway_net`) são usadas em todo o projeto para isolar ambientes.

## Estrutura

-   **desafio1/**: Comunicação de Containers (Servidor/Cliente).
-   **desafio2/**: Persistência de Volume (Logger de Arquivo).
-   **desafio3/**: Orquestração (App + Redis + Postgres).
-   **desafio4/**: Microsserviços (Provedor/Consumidor).
-   **desafio5/**: Padrão API Gateway (Gateway + Usuários + Pedidos).

## Início Rápido

Navegue até qualquer pasta de desafio e siga o `README.md` local.

**Exemplo (Desafio 5):**
```bash
cd desafio5
docker-compose up --build
```

**Exemplo (Desafio 3):**
```bash
cd desafio3
docker-compose up --build
```