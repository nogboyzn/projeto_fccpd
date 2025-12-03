# Desafio 4: Microsserviços Independentes

Este desafio implementa um padrão de microsserviço Provedor-Consumidor.

## Serviços
- **inventory_service** (Provedor): Expõe uma lista de produtos na porta 5001.
- **summary_service** (Consumidor): Consome o serviço de inventário, agrega dados e expõe um resumo na porta 5002.

## Configuração e Execução

1. **Iniciar Serviços:**
   ```bash
   docker-compose up --build -d
   ```

2. **Verificar:**
   Verifique o Inventário (Provedor):
   ```bash
   curl http://localhost:5001/products
   ```
   
   Verifique o Resumo (Consumidor):
   ```bash
   curl http://localhost:5002/summary
   ```
   O serviço de resumo chamará internamente o serviço de inventário e retornará os totais calculados.

3. **Encerrar:**
   ```bash
   docker-compose down
   ```