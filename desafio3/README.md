# Desafio 3: Orquestrando com Docker Compose

Este desafio orquestra uma arquitetura de 3 camadas usando Docker Compose.

## Arquitetura
- **portal_app**: Serviço frontend (Flask) que consome tanto cache quanto banco de dados.
- **session_store**: Redis para cache de contagem de acessos.
- **user_db**: PostgreSQL para armazenamento persistente.
- **Rede**: `backend_net` isola esses serviços.

## Configuração e Execução

1. **Iniciar Serviços:**
   ```bash
   docker-compose up --build -d
   ```

2. **Verificar:**
   Acesse a aplicação portal:
   ```bash
   curl http://localhost:5000
   ```
   Você deve ver uma resposta JSON com `total_visits` (incrementando a cada atualização) e a string de versão do PostgreSQL.

3. **Encerrar:**
   ```bash
   docker-compose down
   ```