# Desafio 2: Volumes e Persistência

Este desafio demonstra a persistência de dados usando Volumes do Docker. A aplicação grava logs em um arquivo dentro de um volume montado, garantindo que os dados sobrevivam a reinicializações do container.

## Arquitetura
- **logger_app**: Um script Python que adiciona carimbos de data/hora em `/app/data/history.log`.
- **Armazenamento**: Um arquivo de texto (`history.log`) em vez de um banco de dados (SQLite evitado conforme requisitos).

## Configuração e Execução

1. **Construir a Imagem:**
   ```bash
   docker build -t logger_app_img .
   ```

2. **Executar com Volume:**
   Montamos um diretório local `$(pwd)/data` para o `/app/data` do container.
   ```bash
   mkdir -p data
   docker run -d --name logger_container -v $(pwd)/data:/app/data logger_app_img
   ```

3. **Verificar Persistência:**
   
   Aguarde alguns segundos, depois pare e remova o container:
   ```bash
   docker stop logger_container
   docker rm logger_container
   ```
   
   Inicie uma NOVA instância de container com o MESMO volume:
   ```bash
   docker run -d --name logger_container_2 -v $(pwd)/data:/app/data logger_app_img
   ```
   
   Verifique os logs do novo container. Ele deve imprimir os "DADOS RECUPERADOS" ("RECOVERED DATA") da execução anterior:
   ```bash
   docker logs logger_container_2
   ```

   Você também pode inspecionar o arquivo localmente:
   ```bash
   cat data/history.log
   ```