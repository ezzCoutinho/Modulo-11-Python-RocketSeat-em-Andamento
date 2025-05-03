import redis

r = redis.Redis(host="localhost", port=6379, db=0)

# para insert e update usamos o set
r.set("chave_1", "trocando o valor")

# para buscar usamos o get, e para tornar o valor de bytes para string usamos o decode
print(r.get("chave_1").decode("utf-8"))

# para deletar usamos o delete
r.delete("chave_1")

# para verificar se a chave existe usamos o exists
print(r.exists("chave_1"))
