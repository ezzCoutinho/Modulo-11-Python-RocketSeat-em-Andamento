import redis

r = redis.Redis(host="localhost", port=6379, db=0)

# para insert e update usamos o set
r.set("chave_1", "trocando o valor")

# para buscar usamos o get, e para tornar o valor de bytes para string usamos o decode
print(r.get("chave_1").decode("utf-8"))

# para deletar usamos o delete
r.delete("chave_1")

# para verificar se a chave existe usamos o exists, se retornar 1 a chave existe, se retornar 0 a chave não existe
print(r.exists("chave_1"))

### comandos para hash
meu_hash = {"nome": "joao", "idade": 30, "cidade": "sao paulo"}
r.hset("meu_hash", "nome", "joao")
r.hset("meu_hash", "idade", "30")
r.hset("meu_hash", "cidade", "curitiba")

# para buscar um valor específico usamos o hget
print(r.hget("meu_hash", "nome").decode("utf-8"))

# para buscar todos os valores usamos o hgetall
print(r.hgetall("meu_hash"))

# para deletar um valor específico usamos o hdel
r.hdel("meu_hash", "cidade")

## buscas por existencia

# para verificar se a chave existe usamos o hexists
print(r.hexists("meu_hash", "cidade"))

# para buscar o número de chaves usamos o hlen
print(r.hlen("meu_hash"))

# para buscar as chaves usamos o hkeys
print(r.hkeys("meu_hash"))
