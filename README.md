## 02/05

Esse módulo nos iremos trabalhar com um banco de dados NOSQL, que será o REDIS.
O Redis é um banco de dados NoSQL amplamente reconhecido por sua alta performance, sendo considerado um dos mais rápidos do mundo. Ele utiliza memória volátil como armazenamento, o que permite operações extremamente rápidas. O funcionamento do Redis é baseado em cache: quando um produto é buscado pela primeira vez, o sistema consulta o Redis para verificar se o produto já está armazenado em cache. Se não estiver, a busca é realizada no banco de dados principal, e o resultado é armazenado no Redis para que futuras consultas sobre o mesmo produto sejam atendidas de forma muito mais rápida. Além disso, o Redis suporta estruturas de dados avançadas, como listas, conjuntos e hashes, o que o torna versátil para diversas aplicações, como gerenciamento de sessões, filas de mensagens e contadores em tempo real.


## 03/05

Hoje, adicionamos a biblioteca redis ao projeto, onde aprendemos a fazer a conexão com o banco de dados e a executar comandos básicos do Redis.


## 05/05

Hoje, configuramos a inicialização da nossa tabela de banco de dados, que servirá como modelo para a estrutura da tabela. Também estabelecemos a conexão com o Redis, incluindo métodos para conectar e acessar essa conexão.


## 06/05

Hoje, configuramos nossos repositórios com métodos do Redis, que incluem: insert, get_key, insert_hash, get_hash, insert_hash_expire e insert_expire. Todos esses métodos foram testados no arquivo redis_raw.py. Além disso, finalizamos a conexão com o banco de dados SQLite3.


## 07/05

Hoje, desenvolvemos a classe `ProductsRepository`, responsável por gerenciar operações de inserção e consulta de produtos no banco de dados através do nome do produto. Implementamos testes de integração utilizando o framework `pytest` para validar o funcionamento desta classe. Além disso, criamos interfaces para padronizar as conexões tanto com o SQLite quanto com o Redis, estabelecendo contratos claros para os repositórios e conexões em ambos os bancos de dados. Futuramente, iremos complementar com testes unitários para garantir ainda mais a qualidade do código. 