# Desafio 5: Microsserviços com API Gateway

Este desafio implementa um padrão de API Gateway usando uma aplicação Python Flask em vez de Nginx.

## Arquitetura
- **api_gateway**: Aplicação Flask expondo `/api/users` e `/api/orders` na porta 8000. Encaminha requisições para serviços internos.
- **user_service**: Serviço interno retornando dados de usuários.
- **order_service**: Serviço interno retornando dados de pedidos.
- **Rede**: `gateway_net` (Serviços internos NÃO são expostos ao host, apenas o Gateway é).

## Configuração e Execução

1. **Iniciar Serviços:**
   ```bash
   docker-compose up --build -d
   ```

2. **Verificar:**
   Acesse Usuários via Gateway:
   ```bash
   curl http://localhost:8000/api/users
   ```
   
   Acesse Pedidos via Gateway:
   ```bash
   curl http://localhost:8000/api/orders
   ```

3. **Encerrar:**
   ```bash
   docker-compose down
   ```