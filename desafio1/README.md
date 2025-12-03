# Desafio 1: Containers em Rede

Este desafio demonstra a comunicação entre containers usando uma rede bridge personalizada `custom_bridge_v2`.

## Arquitetura
- **monitor_server**: Uma aplicação Flask expondo `/api/health` na porta 5000 (mapeada para a porta 8080 do host).
- **monitor_client**: Um script Python usando `urllib` para consultar o servidor.

## Configuração e Execução

1. **Criar a Rede:**
   ```bash
   docker network create custom_bridge_v2
   ```

2. **Construir as Imagens:**
   ```bash
   docker build -t monitor_server_img -f Dockerfile.server .
   docker build -t monitor_client_img -f Dockerfile.client .
   ```

3. **Executar o Servidor:**
   ```bash
   docker run -d --name monitor_server --network custom_bridge_v2 -p 8080:5000 monitor_server_img
   ```

4. **Executar o Cliente:**
   ```bash
   docker run -d --name monitor_client --network custom_bridge_v2 monitor_client_img
   ```

5. **Verificar:**
   Verifique os logs do cliente:
   ```bash
   docker logs -f monitor_client
   ```
   Você deve ver mensagens de sucesso "Uplink established".

   Teste a partir do host:
   ```bash
   curl http://localhost:8080/api/health
   ```