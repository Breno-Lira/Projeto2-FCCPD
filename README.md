# Projeto2-FCCPD

Projeto para a diciplina e Fundamentos de Computação Concorrente e Paralela - FCCPD implementando os desafios apresentados
Abaixo vai a explicação do que está sendo feito em cada desafio e como roda-los usando o docker:

<details>
  <summary><h3>Desafio 1 — Containers em Rede</h3></summary>

  <h2>Objetivo</h2>
  Criar dois containers que se comunicam por uma rede Docker customizada.

  <br>
  <ul>
    <li><strong>Network:</strong> rede-desafio1</li>
    <li><strong>Primeiro container:</strong> cliente-desafio1</li>
    <li><strong>Segundo container:</strong> servidor-desafio1</li>
  </ul>

  A network é criada para concetar os conteiners, o server abre a porta 8080 e o cliente se conecta a ela para estabelecer a conexão. Cada diretiorio possui um Dockerfile de configuração para buildar os containers
 
  1. Para rodar basta, entrar na pasta :
  ```bash
  cd desafio1
  ```
  2. Criando uma rede customizada:
   ```bash
  docker network create rede-desafio1
  ```
  4. Fazer build das imagens:
  ```bash
  docker build -t servidor-flask1 ./app
  docker build -t cliente1 ./cliente
  ```
  4. Rodar os conteiners:
  ```bash
    docker run -d --name servidor-desafio1 --network rede-desafio1 -p 8080:8080 servidor-flask1
    docker run -d --name cliente-desafio1 --network rede-desafio1 cliente1
  ```
  5. E agora será possivel vivusalizar os logs gerados
  ```bash
    -Ver as requisições do cliente:
      docker logs -f cliente-desafio1
    -Ver as requisições chegando ao servidor Flask:
    docker logs -f servidor-desafio1
  ```
  6. Para outra forma de vizualização (Recarregue a pagina Para ver a atualização do tempo):
    "http://localhost:8080/" 
  
</details>

<details>
  <summary><h3>Desafio 2 — Volumes e Persistência de Dados</h3></summary>

  <h2>Objetivo</h2>
  Criar um container que utiliza um volume Docker para persistir dados, demonstrando que os dados permanecem mesmo após a remoção do container.

  <br>
  <ul>
    <li><strong>Volume:</strong> desafio2-volume</li>
    <li><strong>Container:</strong> desafio2-container</li>
  </ul>

  O volume é criado para armazenar dados persistentes. O container escreve dados no volume montado, e mesmo após remover o container, os dados permanecem no volume.
 
  1. Para rodar, entre na pasta:
  ```bash
  cd desafio2
  ```
  2. Criar o volume Docker:
  ```bash
  docker volume create desafio2-volume
  ```
  3. Fazer build da imagem:
  ```bash
  docker build -t desafio2-app .
  ```
  4. Rodar o container com o volume:
  ```bash
  docker run --name desafio2-container -v desafio2-volume:/data desafio2-app
  ```
  5. Testar a persistência removendo o container:
  ```bash
  docker rm desafio2-container
  ```
  6. Rodar novamente com o mesmo volume:
  ```bash
  docker run --name desafio2-container -v desafio2-volume:/data desafio2-app
  ```
  OBS: Assim deve aparecer a antiga inserção feita e uma nova com os mesmos nomes
  
  7. Opcional - Container para ler o banco (ele se auto apaga após a realização):
  ```bash
  docker run --rm -v desafio2-volume:/data desafio2-app python reader.py
  ```
  
</details>

<details>
  <summary><h3>Desafio 3 — Docker Compose com Múltiplos Serviços</h3></summary>

  <h2>Objetivo</h2>
  Criar uma aplicação multi-container usando Docker Compose, integrando uma aplicação web com banco de dados PostgreSQL e cache Redis.

  <br>
  <br>
  <ul>
    <li><strong>Serviço Web:</strong> Flask na porta 8080</li>
    <li><strong>Banco de Dados:</strong> PostgreSQL</li>
    <li><strong>Cache:</strong> Redis</li>
  </ul>

  O Docker Compose orquestra os três serviços, permitindo que a aplicação web se comunique com o banco de dados PostgreSQL e o Redis para cache.
 
  1. Para rodar, entre na pasta:
  ```bash
  cd desafio3
  ```
  2. Subir todos os serviços com Docker Compose:
  ```bash
  docker compose up -d
  ```
  3. Testar a comunicação:
  ```bash
  - Testar serviço web:
  http://localhost:8080
  
  - Testar PostgreSQL:
  http://localhost:8080/db
  Deve retornar a data/hora do servidor PostgreSQL.
  
  - Testar Redis:
  http://localhost:8080/cache
  Cada refresh incrementa o contador.
  ```
  
</details>

<details>
  <summary><h3>Desafio 4 — Comunicação entre Serviços</h3></summary>

  <h2>Objetivo</h2>
  Criar dois serviços que se comunicam entre si usando Docker Compose, onde um serviço consome dados de outro serviço.

  <br>
  <br>
  <ul>
    <li><strong>Service A:</strong> Fornece dados de usuários na porta 5000</li>
    <li><strong>Service B:</strong> Consome dados do Service A na porta 5001</li>
  </ul>

  O Service B faz requisições HTTP para o Service A para obter dados de usuários e disponibiliza um endpoint combinado com informações completas.
 
  1. Para rodar, entre na pasta:
  ```bash
  cd desafio4
  ```
  2. Subir os serviços com build:
  ```bash
  docker compose up --build
  ```
  3. Testar os serviços:
  ```bash
  - Service A (listar usuários):
  curl http://localhost:5000/users
  
  - Service B (dados completos consumindo A):
  curl http://localhost:5001/completo
  ```
  
</details>

<details>
  <summary><h3>Desafio 5 — API Gateway com Microserviços</h3></summary>

  <h2>Objetivo</h2>
  Implementar um API Gateway que roteia requisições para diferentes microserviços (usuários e pedidos) usando Docker Compose.

  <br>
  <br>
  <ul>
    <li><strong>Gateway:</strong> API Gateway na porta 8080</li>
    <li><strong>Service Users:</strong> Microserviço de usuários</li>
    <li><strong>Service Orders:</strong> Microserviço de pedidos</li>
  </ul>

  O Gateway recebe as requisições e as encaminha para os microserviços apropriados, implementando o padrão de API Gateway para centralizar o acesso aos serviços.
 
  1. Para rodar, entre na pasta:
  ```bash
  cd desafio5
  ```
  2. Subir todos os serviços:
  ```bash
  docker compose up -d
  ```
  3. Testar o Gateway:
  ```bash
  - Gateway listar usuários:
  http://localhost:8080/users
  
  - Gateway listar pedidos:
  http://localhost:8080/orders
  ```
  
</details>
