Criar apis com o django framerworks
# Passo 1 - Criar o modelo no arquivo models.py
# Passo 2 - registrar o modelo no admin
Serializer - Ele faz a 'conversão' do objeto python que está vindo do banco de dados para um formato json.
#Passo 3 - Criar o aquivo serializer que irá dizer pra api o que enviar para o cliente
#Passo 4 - registrar no urls.py a minha rota para ele poder 'saber' pra onde ir.

Criar autenticação - 

# Passo 1 - instalar a lib djangorestframework-simplejwt
#Passo 2 - configurar uma sessão no settings.py passando o nome do token
Passo 3 - ir no urls.py, importar as libs, declarar os paths no urls patterns
Passo 4 - ir no views.py e declarar uma variavel chamando a classe isAuthenticated