# **&lt;code_by_girls/&gt; API..**  
![GitHub top language](https://img.shields.io/github/languages/top/leandromedvedev/cap-alexandre-g05?color=yellow&style=plastic)  
![GitHub language count](https://img.shields.io/github/languages/count/leandromedvedev/cap-alexandre-g05?style=plastic)

A aplicação foi pensada para fomentar a troca de experiências, divulgação de vagas e assuntos correlatos bem como a criação e manutenção de uma rede formada por mulheres que já atuam ou almejam atuar na área de tecnologia, promovendo um espaço seguro e acolhedor para que essa troca possa acontecer.

## **Endpoints**  

Há um total de 28 endpoints.

#### **Method | Endpoint**  

1. POST     /api/login  
***  

1. POST     /api/users  
2. GET      /api/users  
3. GET      /api/users/&lt;int:id&gt;  
4. PATCH    /api/users/&lt;int:id&gt;  
5. DELETE   /api/users/&lt;int:id&gt;  
***  

1. POST     /api/users/works  
2. GET      /api/users/works  
3. PATCH    /api/users/works/&lt;int:work_id&gt;  
4. DELETE   /api/users/works/&lt;int:work_id&gt;  
***  

1. POST     /api/users/skills  
2. GET      /api/users/skills  
3. GET      /api/users/skills/&lt;int:id&gt;  
4. PATCH    /api/users/skills/&lt;int:id&gt;  
5. DELETE   /api/users/skills/&lt;int:id&gt;  
***  

1. POST     /api/groups  
2. GET      /api/groups  
3. GET      /api/groups/&lt;int:id&gt;  
4. PATCH    /api/groups/&lt;int:id&gt;  
5. DELETE   /api/groups/&lt;int:id&gt;  
***  

1. POST     /api/groups/subscribes   
2. GET      /api/groups/subscribes  
3. DELETE   /api/groups/subscribes/&lt;int:id&gt;  
***  

1. POST     /api/comments  
2. GET      /api/comments  
3. GET      /api/comments/&lt;int:id&gt;  
4. PATCH    /api/comments/&lt;int:id&gt;  
5. DELETE   /api/comments/&lt;int:id&gt;  

***  
# **Users**  

* POST     /api/users  
* GET      /api/users  
* GET      /api/users/&lt;int:id&gt;  
* PATCH    /api/users/&lt;int:id&gt;  
* DELETE   /api/users/&lt;int:id&gt; 

Rotas responsáveis pela criação, busca, atualização e deleção de usuário. 

## **Método <font color=00FF00>POST</font> - /api/users**  
Campos obrigatórios:  

* name  
* email  
* password  
  
### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=00FF00>POST</font> /api/users - Formato da Requisição**  
```py  
{  
	"name": "desmONd hUmme",  
	"email": "desmond8513@uorak.com",  
	"password": "wW*8uuuu"  
}    
```  

## **<font color=00FF00>POST</font> /api/users - Formato da Resposta - <font color=00FF00>201 CREATED</font>**  
```py  
{  
	"msg": "verify your email!"  
}  
```  

Repare que a mensagem retornada indica a necessidade de validação do e-mail passado em sua caixa de e-mail. Ao validá-lo, o acesso é liberado conforme veremos mais à frente em login.  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *um dos campos obrigatórios não é passado:*
## **<font color=00FF00>POST</font> /api/users - Formato da Requisição**  
```py  
{
	"email": "burkejuliet@lost.com",
	"password": "wW*8uuuu"
}
```  

## **<font color=00FF00>POST</font> /api/users - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**  
```py  
{  
	"error": "name, email and password are mandatory keys"  
}  
```  

2. ***Caso 2 -*** *os campos obrigatórios são passados, mas um ou mais deles contêm erro de grafia:*  

## **<font color=00FF00>POST</font> /api/users - Formato da Requisição**  
```py  
{  
	"na": "Juliet Burke",  
	"ema": "burkejuliet@lost.com",  
	"pass": "wW*8uuuu"  
}  
```  

## **<font color=00FF00>POST</font> /api/users - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**  
```py  
{  
	"invalid_keys": [  
		"na",  
		"ema",  
		"pass"  
	],  
	"valid_keys": [  
		"password",  
		"name",  
		"email"  
	]  
}  
``` 

3. ***Caso 3 -*** *o e-mail no corpo da requisição já existe:*  

## **<font color=00FF00>POST</font> /api/users - Formato da Requisição**  
```py  
{  
	"name": "Juliet Burke",  
	"email": "burkejuliet@lost.com",  
	"password": "wW*8uuuu"  
}  
```  

## **<font color=00FF00>POST</font> /api/users - Formato da Resposta - <font color='FFA500'>409 CONFLICT</font>**  
```py  
{  
	"error": "Email is already exists"  
}  
```  

***
# **Login**  

## **Método <font color=00FF00>POST</font> - /api/login**  


* POST     /api/login  

Rota responsável pelo login do usuário.  
Campos obrigatórios:  

* email  
* password  

### ***Requisição <font color='0096FF'>CORRETA</font>***  

## **<font color=00FF00>POST</font> /api/login - Formato da Requisição**  
```py  
{
	"email": "burkejuliet@lost.com",
	"password": "wW*8uuuu"
}
```  

## **<font color=00FF00>POST</font> /api/login - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
{  
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MTYwOTcxMywianRpIjoiNjUwMzE0ODgtOGViYy00OGM5LWEyMGQtOGQ1ZTczM2U0YmI3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6Ikp1bGlldCBCdXJrZSIsImVtYWlsIjoiYnVya2VqdWxpZXRAbG9zdC5jb20ifSwibmJmIjoxNjUxNjA5NzEzLCJleHAiOjE2NTE2OTYxMTN9.5MWIZBG7L9GUz6-PbLOSp8qf3BGxyP4EBmF855JTb1Q",  
	"user": {  
		"id": 1,  
		"name": "Juliet Burke",  
		"email": "burkejuliet@lost.com"  
	}  
}  
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *uma das chaves requeridas (email e password) não é passada:*  
## **<font color=00FF00>POST</font> /api/login - Formato da Requisição**
```py  
{  
	"email": "burkejuliet@lost.com"  
}  
```  

## **<font color=00FF00>POST</font> /api/login - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**  
```py  
{
	"expected": [
		"email",
		"password"
	],
	"obtained": [
		"email"
	]
}
```  

2. ***Caso 2 -*** *o email digitado é incorreto:*  

## **<font color=00FF00>POST</font> /api/login - Formato da Requisição**  
```py  
{  
	"email": "burkejuliet@lost",  
	"password": "wW*8uuuu"  
}  
```  

## **<font color=00FF00>POST</font> /api/login - Formato da Resposta - <font color='FFA500'>404 NOT FOUND</font>**  
```py  
{  
	"error": "User not found!"  
}  
```  

3. ***Caso 3 -*** *o password digitado é incorreto:*  

## **<font color=00FF00>POST</font> /api/login - Formato da Requisição**  
```py  
{  
	"email": "burkejuliet@lost.com",  
	"password": "senha_errada"  
}  
```  

## **<font color=00FF00>POST</font> /api/login - Formato da Resposta - <font color='FFA500'>401 UNAUTHORIZED</font>**
```py  
{  
	"error": "Unauthorized"  
}  
```  

4. ***Caso 4 -*** *o e-mail passado no cadastro ainda não foi confirmado em sua caixa de e-mail:*  

## **<font color=00FF00>POST</font> /api/login - Formato da Requisição**  
```py  
{  
	"email": "hummedesmond@uorak.com",  
	"password": "wW*8uuuu"  
}  
```  

## **<font color=00FF00>POST</font> /api/login - Formato da Resposta - <font color='FFA500'>401 UNAUTHORIZED</font>**
```py  
{  
	"error": "email not validate!"  
}  
```  

## **Método <font color='C710AF'>GET</font> - /api/users**  

Busca por usuários cadastrados.  

### ***Requisição <font color='0096FF'>CORRETA</font>***  
Com JWT token no cabeçalho da requisição. Sem corpo:  

## **<font color='C710AF'>GET</font> /api/users - Formato da Requisição**  
```py  
No body  
```  

## **<font color='C710AF'>GET</font> /api/users - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
[
	{
		"id": 1,
		"name": "Juliet Burke",
		"email": "burkejuliet@lost.com",
		"skills": [],
		"works": []
	},
	{
		"id": 2,
		"name": "Kate Austen",
		"email": "austenkate@lost.com",
		"skills": [],
		"works": []
	}
]
```  

### ***Requisição <font color='F70D1A'>ERRADA</font>***  

Sem token no cabeçalho da requisição:  

## **<font color='C710AF'>GET</font> /api/users - Formato da Requisição**  
```py  
No body  
```  

## **<font color='C710AF'>GET</font> /api/users - Formato da Resposta - <font color='FFA500'>422 UNPROCESSABLE ENTITY</font>**  
```py  
{  
	"msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"  
}  
```  

## **Método <font color='C710AF'>GET</font> - /api/users/&lt;int:id&gt;**  

Buscar um usuário específico por ID.  
***Nota**: O não uso de token no cabeçalho retornará o mesmo status 422 mencionado acima.  

### ***Requisição <font color='0096FF'>CORRETA</font>***  

## **<font color='C710AF'>GET</font> /api/users/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body  
```  

## **<font color='C710AF'>GET</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
{  
	"id": 3,  
	"name": "Kate Austen",  
	"email": "austenkate@lost.com",  
	"skills": [],  
	"works": []  
}  
```    

### ***Requisição <font color='F70D1A'>ERRADA</font>***  

Um ID inexistente é inserido na busca.  

## **<font color='C710AF'>GET</font> /api/users/&lt;int:id&gt; - Formato da Requisição**
```py  
No body  
```  

## **<font color='C710AF'>GET</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color='FFA500'>404 NOT FOUND</font>**  
```py  
{
	"error": "User not found"
}
```  

## **Método <font color='FFFF2E'>PATCH</font> - /api/users/&lt;int:id&gt;**  

Permite a atualização de 1 ou mais campos do usuário. Com autenticação no cabeçalho da requisição.  

### ***Requisição <font color='0096FF'>CORRETA</font>***  

## **<font color='FFFF2E'>PATCH</font> /api/users/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"name": "Sayid Jarrah",  
	"email": "jarrahsayid@lost.com"  
}  
```  

## **<font color='FFFF2E'>PATCH</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>200 OK</font>**   
```py  
{  
	"id": 1,  
	"name": "Sayid Jarrah",  
	"email": "jarrahsayid@lost.com",  
	"skills": [],  
	"works": []  
}  
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *email passado para atualização não possui formato correto contendo @ ou .com:* 

## **<font color='FFFF2E'>PATCH</font> /api/users/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"name": "Sayid Jarrah",  
	"email": "jarrahsayid@lost"  
}  
```  

## **<font color='FFFF2E'>PATCH</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**   
```py  
{  
	"invalid_email": "Past email should have a format similar to: something@something.com"  
}  
```  

2. ***Caso 2 -*** *id passado não está cadastrado:*  

## **<font color='FFFF2E'>PATCH</font> /api/users/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"name": "Sayid Jarrah",  
	"email": "jarrahsayid@lost.com"  
}  
```    

## **<font color='FFFF2E'>PATCH</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color='FFA500'>404 NOT FOUND</font>**   
```py  
{  
	"error": "id not found"  
}  
```  

3. ***Caso 3 -*** *sem token de autenticação:*  

## **<font color='FFFF2E'>PATCH</font> /api/users/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"name": "Sayid Jarrah",  
	"email": "jarrahsayid@lost.com"  
}  
```   

## **<font color='FFFF2E'>PATCH</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color='FFA500'>422 UNPROCESSABLE ENTITY</font>**   
```py  
{  
	"msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"  
}  
```  

## **Método <font color='E10600'>DELETE</font> - /api/users/&lt;int:id&gt;**  

Possibilita a exclusão de um usuário específico referenciado pelo id na URL. Exige autenticação.  

### ***Requisição <font color='0096FF'>CORRETA</font>***  

## **<font color='E10600'>DELETE</font> /api/users/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body 
```  

## **<font color='E10600'>DELETE</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>204 NO CONTENT</font>**  
```ja  
No body returned for response  
```   

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *sem token de autenticação:*  

## **<font color='E10600'>DELETE</font> /api/users/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body
```  

## **<font color='E10600'>DELETE</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color='FFA500'>422 UNPROCESSABLE ENTITY</font>**  
```py  
{  
	"msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"  
}  
```  

2. ***Caso 2 -*** *id passado não está cadastrado:*  

## **<font color='E10600'>DELETE</font> /api/users/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body
```  

## **<font color='E10600'>DELETE</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color='FFA500'>404 NOT FOUND</font>**  
```py  
{  
	"error": "id not found"  
}  
```  

***  
# **Works**  

1. POST     /api/users/works  
2. GET      /api/users/works  
3. PATCH    /api/users/works/&lt;int:work_id&gt;  
4. DELETE   /api/users/works/&lt;int:work_id&gt; 

Rotas responsáveis pela criação, busca, atualização e deleção de works. Campos na requisição:

* title  
* description  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=00FF00>POST</font> /api/users/works - Formato da Requisição**  
```py 
{  
	"title": "Code by Girls - capstone",  
	"description": "Q3 final work"  
}  
```  

## **<font color=00FF00>POST</font> /api/users/works - Formato da Resposta - <font color=00FF00>201 CREATED</font>**  
```py  
{  
	"id": 1,  
	"title": "Code By Girls - Capstone",  
	"description": "Q3 final work",  
	"user_id": 4  
}  
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *chave excedente passada ou escrita de modo errado:*  

## **<font color=00FF00>POST</font> /api/users/works - Formato da Requisição**  
```py 
{  
	"title": "Code by Girls - capstone",  
	"description": "Q3 final work",  
	"surplus_key": "surplus key"  
}  
```   

Caso o valor passado seja um número ou uma lista com ao menos um elemento, será convertida em string e criada. 

## **<font color=00FF00>POST</font> /api/users/works - Formato da Resposta - <font color=FFA500>400 BAD REQUEST</font>**  
```py  
{  
	"error": {  
		"valid_keys": [  
			"title",  
			"description"  
		],  
		"key_sended": "chave_excedente"  
	}  
}  
```  

2. ***Caso 2 -*** *valor passado é {}, []:*  

## **<font color=00FF00>POST</font> /api/users/works - Formato da Requisição**  
```py 
{  
	"title": {},  
	"description": "Q3 final work"   
}  
``` 

## **<font color=00FF00>POST</font> /api/users/works - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**  
```py  
{  
	"error": "TITLE is empty!"  
}  
```  

3. ***Caso 3 -*** *usuário não autenticado:*  

## **<font color=00FF00>POST</font> /api/users/works - Formato da Resposta - <font color='FFA500'>422 UNPROCESSABLE ENTITY</font>**  
```py  
{  
	"msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"  
}  
```  

## **Método <font color=C710AF>GET</font> - /api/users/works**  

Rota de busca de works do usuário exige autenticação, do contrário status 422.  

## **<font color=C710AF>GET</font> /api/users/works - Formato da Requisição**  
```py  
No body  
```  

## **<font color=C710AF>GET</font> /api/users/works - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
[  
	{  
		"id": 1,  
		"title": "Code By Girls - Capstone",  
		"description": "Q3 final work"  
	}  
]  
```  

## **Método <font color='FFFF2E'>PATCH</font> - /api/users/works/&lt;int:id&gt;**  

Rota de atualização do trabalho do usuário que exige autenticação, do contrário status 422.  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=FFFF2E>PATCH</font> /api/users/works/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"title": "Habit Management",  
	"description": "Q2 final work"  
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/users/works/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
{  
	"id": 1,  
	"title": "Habit Management",  
	"description": "Q2 final work",  
	"user_id": 4  
}  
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *chave errada:*  

## **<font color=FFFF2E>PATCH</font> /api/users/works/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"chave_errada": "Q2 final Work"  
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/users/works/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>400 BAD REQUEST</font>**  
```py  
{  
	"error": {  
		"valid_keys": [  
			"title",  
			"description"  
		],  
		"key_sended": "chave_errada"  
	}  
}  
```  

2. ***Caso 2 -*** *id passado na URL não existe no banco:*  

## **<font color=FFFF2E>PATCH</font> /api/users/works/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>404 NOT FOUND</font>**  
```py  
{  
	"error": "Work doesn't exists!"  
}  
```  

## **Método <font color='F70D1A'>DELETE</font> - /api/users/works/&lt;int:id&gt;**  

Rota de deleção do work do usuário que exige autenticação, do contrário status 422.  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=F70D1A>DELETE</font> /api/users/works/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body  
```  

## **<font color=F70D1A>DELETE</font> /api/users/works/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>204 NO CONTENT</font>**  
```ja  
No body returned for response 
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

Caso o usuário não esteja autenticado, status code 422 é retornado. Caso o ID passado inexista:  

## **<font color=F70D1A>DELETE</font> /api/users/works/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body   
```  

## **<font color=F70D1A>DELETE</font> /api/users/works/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>404 NOT FOUND</font>**  
```py  
{  
	"error": "Work doesn't exists!"  
}  
```  

# **Skills**  

1. POST     /api/users/skills  
2. GET      /api/users/skills  
3. GET      /api/users/skills/&lt;int:id&gt;  
4. PATCH    /api/users/skills/&lt;int:id&gt;  
5. DELETE   /api/users/skills/&lt;int:id&gt;  

Rotas responsáveis pela criação, busca, atualização e deleção de skills. Campos na requisição:

* skill  
* level    

O campo level aceita as seguintes strings: Iniciante, Intermediario (sem acento) e Avançado.  

## **Método <font color=00FF00>POST</font> - /api/users/skills**  

### ***Requisição <font color='0096FF'>CORRETA</font>***  


## **<font color=00FF00>POST</font> /api/users/skills - Formato da Requisição**  
```py 
{  
	"skill": "React",  
	"level": "Intermediario"  
}   
```  

## **<font color=00FF00>POST</font> /api/users/skills - Formato da Resposta - <font color=00FF00>201 CREATED</font>**  
```py  
{  
	"id": 5,  
	"skill": "React",  
	"level": "Intermediario"  
}    
```  

Caso o valor passado no campo skill for um número decimal, inteiro, array, será convertido para string e criado normalmente.

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *chave excedente passada ou correta, mas escrita de modo errado:*  

## **<font color=00FF00>POST</font> /api/users/skills - Formato da Requisição**  
```py 
{   
	"skill": "React",  
	"level": "Intermediario",  
	"surplus_key": "surplus_value"  
}  
```    

## **<font color=00FF00>POST</font> /api/users/skills - Formato da Resposta - <font color=FFA500>400 BAD REQUEST</font>**  
```py  
{  
	"msg": {  
		"valid_keys": {  
			"skill": "",  
			"level": ""  
		},  
		"your_keys": {  
			"skill": "React",   
			"level": "Intermediario",  
			"surplus_key": "surplus_value",  
			"user_id": 12  
		}  
	}  
}  
```  

2. ***Caso 2 -*** *usuário não autenticado:*  

## **<font color=00FF00>POST</font> /api/users/skills - Formato da Resposta - <font color='FFA500'>422 UNPROCESSABLE ENTITY</font>**  
```py  
{  
	"msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"  
}  
```  

## **Método <font color=C710AF>GET</font> - /api/users/skills**  

Rota de busca de skills do usuário exige autenticação, do contrário status 422.  

## **<font color=C710AF>GET</font> /api/users/skills - Formato da Requisição**  
```py  
No body  
```  

## **<font color=C710AF>GET</font> /api/users/skills - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
[  
	{  
		"id": 5,  
		"skill": "React",  
		"level": "Intermediario"  
	},  
	{  
		"id": 6,  
		"skill": "Django",  
		"level": "Intermediario"  
	}  
]  
```  

## **Método <font color='FFFF2E'>PATCH</font> - /api/users/skills/&lt;int:id&gt;**  

Rota de atualização da skill do usuário que exige autenticação, do contrário status 422.  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=FFFF2E>PATCH</font> /api/users/skills/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"skill": "fLASk",  
	"level": "Intermediario"  
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/users/skills/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
{  
	"id": 6,  
	"skill": "Flask",  
	"level": "Intermediario"  
}   
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *chave errada:*  

## **<font color=FFFF2E>PATCH</font> /api/users/skills/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"skil": "fLAsk",  
	"levl": "Intermediario"  
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/users/skills/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>400 BAD REQUEST</font>**  
```py  
{  
	"msg": {  
		"valid_keys": {  
			"skill": "",  
			"level": ""  
		},  
		"your_keys": {  
			"skil": "fLAsk",  
			"levl": "Intermediario"  
		}  
	}  
}   
```  

2. ***Caso 2 -*** *id passado na URL não existe no banco:*  

## **<font color=FFFF2E>PATCH</font> /api/users/skills/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>404 NOT FOUND</font>**  
```py  
{  
	"msg": "Non-existent skill"
}  
```  

## **Método <font color='F70D1A'>DELETE</font> - /api/users/skills/&lt;int:id&gt;**  

Rota de deleção da skill do usuário que exige autenticação, do contrário status 422.  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=F70D1A>DELETE</font> /api/users/skills/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body  
```  

## **<font color=F70D1A>DELETE</font> /api/users/skills/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>204 NO CONTENT</font>**  
```ja  
No body returned for response 
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

Caso o usuário não esteja autenticado, status code 422 é retornado. Caso o ID passado inexista:  

## **<font color=F70D1A>DELETE</font> /api/users/skills/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>404 NOT FOUND</font>**  
```py  
{  
	"msg": "Non-existent skill"  
}   
```  

# **Groups**  

1. POST     /api/groups  
2. GET      /api/groups  
3. GET      /api/groups/&lt;int:id&gt;  
4. PATCH    /api/groups/&lt;int:id&gt;  
5. DELETE   /api/groups/&lt;int:id&gt;  

Rotas responsáveis pela criação, busca, atualização e deleção de groups. Todas as rotas de groups exigem autenticação, do contrário status code 422 será retornado. Campos na requisição:

* title  
* description  

## **Método <font color=00FF00>POST</font> - /api/groups**  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=00FF00>POST</font> /api/groups - Formato da Requisição**  
```py 
{  
	"name": "gIRls grOUp",  
	"description": "group formed by girls"  
}  
```  

## **<font color=00FF00>POST</font> /api/groups - Formato da Resposta - <font color=00FF00>201 CREATED</font>**  
```py  
{  
	"name": "Girls Group",  
	"description": "Group formed by girls",  
	"id": 10  
}   
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *chave excedente passada ou escrita de modo errado:*  

## **<font color=00FF00>POST</font> /api/groups - Formato da Requisição**  
```py 
{  
	"nme": "gIRls group",  
	"description": "group formed by girls",  
	"surplus_key": "wrong_key"  
}   
```   

## **<font color=00FF00>POST</font> /api/groups - Formato da Resposta - <font color=FFA500>400 BAD REQUEST</font>**  
```py  
{  
	"invalid_keys": [  
		"nme",  
		"surplus_key"  
	],  
	"valid_keys": [  
		"description",  
		"name"  
	]  
}  
```  

2. ***Caso 2 -*** *valor passado não é uma string:*  

## **<font color=00FF00>POST</font> /api/groups - Formato da Requisição**  
```py 
{  
	"name": "Girls Group",  
	"description": {}  
}  
``` 

## **<font color=00FF00>POST</font> /api/groups - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**  
```py  
{   
	"error": "Invalid data type. Type must be a string"  
}  
```  

## **Método <font color=C710AF>GET</font> - /api/groups**  

### ***Requisição <font color='0096FF'>CORRETA</font>***  

## **<font color=C710AF>GET</font> /api/groups - Formato da Requisição**  
```py  
No body  
```  

## **<font color=C710AF>GET</font> /api/groups - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
[  
	{  
		"id": 2,  
		"name": "Pyladies",  
		"description": "Girls tech",  
		"group_owner": {  
			"id": 1,  
			"name": "Austen Kate"  
		},  
		"subscribes": [  
			{  
				"name": "Austen Kate",  
				"email": "austenkate@uorak.com"  
			}  
		],  
		"remarks": []  
	},  
	{  
		"id": 9,  
		"name": "Raygirls",  
		"description": "Girls tech",  
		"group_owner": {  
			"id": 2,  
			"name": "Juliet Burke"  
		},  
		"subscribes": [  
			{  
				"name": "Juliet Burke",  
				"email": "burkejuliet@uorak.com"   
			}   
		],  
		"remarks": []  
	}  
]  
```  

Busca de um grupo específico por ID:
## **<font color='C710AF'>GET</font> /api/groups/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body  
```  

## **<font color='C710AF'>GET</font> /api/groups/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
{  
	"id": 2,  
	"name": "Pyladies",  
	"description": "Girls tech",  
	"subscribes": [  
		{  
			"name": "Austen Kate",  
			"email": "austenkate@uorak.com"  
		}  
	],  
	"group_owner": {  
		"id": 1,  
		"name": "Austen Kate"  
	},  
	"remarks": []  
}  
```     

### ***Requisição <font color='F70D1A'>ERRADA</font>***  

1. ***Caso 1 -*** *id passado na URL não existe:*  

## **<font color='C710AF'>GET</font> /api/groups/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body  
```  

## **<font color='C710AF'>GET</font> /api/groups/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>404 NOT FOUND</font>**  
```py  
{  
	"error": "Group not found"  
}  
```  

## **Método <font color='FFFF2E'>PATCH</font> - /api/groups/&lt;int:id&gt;**  

Rota de atualização do grupo do usuário que exige autenticação, do contrário status 422. Só lembrando que o método PATCH, diferente do método PUT que exige a passagem de todos os campos, permite que você opte entre atualizar um ou mais campos.  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=FFFF2E>PATCH</font> /api/groups/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"name": "tEch gIRls grOUP"  
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/groups/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
{  
	"id": 10,  
	"name": "Tech Girls Group",  
	"description": "Group formed by girls",  
	"subscribes": [  
		{  
			"id": 2,  
			"name": "Juliet Burke",  
			"email": "burkejuliet@uorak.com"  
		}  
	],  
	"group_owner": {  
		"id": 2,  
		"name": "Juliet Burke",  
		"email": "burkejuliet@uorak.com"  
	},  
	"remarks": []  
}   
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *chave errada:*  

## **<font color=FFFF2E>PATCH</font> /api/groups/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"nae": "tEch gIRls grOUP 2"
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/groups/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>200 OK</font>**  
```py  
{  
	"id": 10,  
	"name": "Tech Girls Group",  
	"description": "Group formed by girls",  
	"subscribes": [  
		{  
			"id": 2,  
			"name": "Juliet Burke",  
			"email": "burkejuliet@uorak.com"  
		}  
	],  
	"group_owner": {  
		"id": 2,  
		"name": "Juliet Burke",  
		"email": "burkejuliet@uorak.com"  
	},  
	"remarks": []  
}   
```  

Conquanto o status code retornado seja 200 OK, note que o campo 'name' não foi atualizado, isso porque a chave passada contém erro de sintaxe, 'nae' ao invés de 'name'.

2. ***Caso 2 -*** *id passado na URL não existe no banco:*  

## **<font color=FFFF2E>PATCH</font> /api/groups/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>404 NOT FOUND</font>**  
```py  
{  
	"error": "Group not found"  
}  
```  

3. ***Caso 3 -*** *nome do grupo a ser atualizado já existe:*  

## **<font color=FFFF2E>PATCH</font> /api/groups/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"name": "tEch gIRls grOUP"
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/groups/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
{  
	"error": "Group already exists, choose another name."   
}   
```  

4. ***Caso 4 -*** *grupo a ser atualizado não foi criado por você:*  

## **<font color=FFFF2E>PATCH</font> /api/groups/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"name": "tEch gIRls grOUP"
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/groups/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>401 UNAUTHORIZED</font>**  
```py  
{  
	"error": "Unauthorized update. You are only allowed to update groups created by you"  
}   
```  

## **Método <font color='F70D1A'>DELETE</font> - /api/groups/&lt;int:id&gt;**  

Rota de deleção do grupo do usuário que exige autenticação, do contrário status 422.  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=F70D1A>DELETE</font> /api/groups/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body  
```  

## **<font color=F70D1A>DELETE</font> /api/groups/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>204 NO CONTENT</font>**  
```ja  
No body returned for response 
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *caso o ID passado inexista:*  

## **<font color=F70D1A>DELETE</font> /api/groups/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>404 NOT FOUND</font>**  
```py  
{  
	"error": "Group not found"  
}  
```  

2. ***Caso 2 -*** *grupo a ser excluído não foi criado por você:*  

## **<font color=F70D1A>DELETE</font> /api/groups/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>401 UNAUTHORIZED</font>**  
```py  
{  
	"error": "Unauthorized deletion. You are only allowed to delete groups created by you"  
}  
```  

# **Subscribes**  

1. POST     /api/groups/subscribes   
2. GET      /api/groups/subscribes   
3. DELETE   /api/groups/subscribes/&lt;int:id&gt;  

Rotas responsáveis pela inscrição, busca e deleção da inscrição em grupos. Todas as rotas de subscribes exigem autenticação, do contrário status code 422 será retornado. Campos na requisição:

* group_id  

## **Método <font color=00FF00>POST</font> - /api/groups/subscribes**  

### ***Requisição <font color='0096FF'>CORRETA</font>***  

## **<font color=00FF00>POST</font> /api/groups/subscribes - Formato da Requisição**  
```py  
{  
	"group_id": 2  
}  
```  

## **<font color=00FF00>POST</font> /api/groups/subscribes - Formato da Resposta - <font color=00FF00>201 CREATED</font>**  
```py  
{  
	"id": 2,  
	"name": "Pyladies",  
	"description": "Girls tech", 
	"group_owner": {  
	"id": 1,  
	"name": "Austen Kate",  
	"email": "austenkate@uorak.com"  
	}, 
	"subscribes": [  
		{  
			"id": 1,  
			"name": "Austen Kate",  
			"email": "austenkate@uorak.com"  
		},  
		{  
			"id": 2,  
			"name": "Juliet Burke",  
			"email": "burkejuliet@uorak.com"  
		}  
	],    
	"remarks": []  
}  
```    

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *chave errada passada:*  

## **<font color=00FF00>POST</font> /api/groups/subscribes - Formato da Requisição**  
```py  
{  
	"group": 2   
}   
```   

## **<font color=00FF00>POST</font> /api/groups/subscribes - Formato da Resposta - <font color=FFA500>400 BAD REQUEST</font>**  
```py  
{  
	"error": {  
		"valid_key": "group_id",  
		"key_sended": "group"  
	}  
}  
```  

2. ***Caso 2 -*** *valor passado não é um número inteiro:*  

## **<font color=00FF00>POST</font> /api/groups/subscribes - Formato da Requisição**  
```py  
{  
	"group_id": []    
}  
```  

## **<font color=00FF00>POST</font> /api/groups/subscribes - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**  
```py  
{   
	"error": "Invalid data type. The type must be an integer"  
}  
```  

3. ***Caso 3 -*** *valor passado é um número decimal ou grupo não existe:*  

## **<font color=00FF00>POST</font> /api/groups/subscribes - Formato da Requisição**  
```py  
{  
	"group_id": 7.9  
}  
```  

## **<font color=00FF00>POST</font> /api/groups/subscribes - Formato da Resposta - <font color='FFA500'>404 NOT FOUND</font>**  
```py  
{   
	"error": "Group doesn't exists"  
}  
```  

## **Método <font color=C710AF>GET</font> - /api/groups/subscribes**  

## **<font color=C710AF>GET</font> /api/groups/subscribes - Formato da Requisição**  
```py  
No body  
```  

## **<font color=C710AF>GET</font> /api/groups/subscribes - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
[  
	{  
		"id": 9,  
		"name": "Raygirls 9",  
		"description": "Girls tech",  
		"group_owner": {  
			"id": 1,  
			"name": "Austen Kate",  
			"email": "austenkate@uorak.com"  
		},  
		"subscribes": [  
			{  
				"id": 1,  
				"name": "Austen Kate",  
				"email": "austenkate@uorak.com"  
			},  
			{  
				"id": 2,  
				"name": "Juliet Burke",  
				"email": "burkejuliet@uorak.com"  
			}  
		],  
		"remarks": []  
	},  
	{  
		"id": 11,  
		"name": "Fatech Girls",  
		"description": "Group formed by girls",  
		"group_owner": {  
			"id": 2,  
			"name": "Juliet Burke",  
			"email": "burkejuliet@uorak.com"  
		},  
		"subscribes": [  
			{  
				"id": 2,  
				"name": "Juliet Burke",  
				"email": "burkejuliet@uorak.com"  
			}  
		],  
		"remarks": []  
	}   
]  
```  

## **Método <font color='F70D1A'>DELETE</font> - /api/groups/subscribes/&lt;int:id&gt;**  

Rota de deleção da inscrição do usuário que exige autenticação, do contrário status 422.  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=F70D1A>DELETE</font> /api/groups/subscribes/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body  
```  

## **<font color=F70D1A>DELETE</font> /api/groups/subscribes/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
{
	"msg": "You unsubscribed from the group 'Pyladies'"  
}
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *caso o ID passado inexista:*  

## **<font color=F70D1A>DELETE</font> /api/groups/subscribes/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>404 NOT FOUND</font>**  
```py  
{  
	"error": "Group not found"  
}  
```  

2. ***Caso 2 -*** *tentativa de desinscrição num grupo no qual você não está inscrito:*  

## **<font color=F70D1A>DELETE</font> /api/groups/subscribes/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>404 NOT FOUND</font>**  
```py  
{  
	"error": "Subscribe not found!"  
}  
```  

# **Comments**  

1. POST     /api/comments  
2. GET      /api/comments  
3. GET      /api/comments/&lt;int:id&gt;  
4. PATCH    /api/comments/&lt;int:id&gt;  
5. DELETE   /api/comments/&lt;int:id&gt;  

Rotas responsáveis pela criação, busca, atualização e exclusão de comentários.  
Todas as rotas de comentários exigem autenticação, do contrário status code 422 será retornado.  
Para comentar em um grupo, o usuário deve estar inscrito no grupo.  
Para comentar, o ID do grupo no qual o usuário quer comentar deverá ser passado na URL.  
Campos na requisição:  

* comments    

## **Método <font color=00FF00>POST</font> - /api/comments**  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=00FF00>POST</font> /api/comments/&lt;int:id&gt; - Formato da Requisição**  
```py 
{  
	"comments": "Hi, ladies"  
}  
```  

## **<font color=00FF00>POST</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>201 CREATED</font>**  
```py  
{  
	"id": 9,  
	"comment": "Hi, ladies",  
	"timestamp": "Sun, 05 May 2022 23:24:50 GMT",  
	"author": {  
		"id": 2,  
		"name": "Juliet Burke"  
	}  
}   
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *chave errada:*  

## **<font color=00FF00>POST</font> /api/comments/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"valid_key": "comments",  
	"received_keys": [  
		"coments"  
	]  
}  
```   

## **<font color=00FF00>POST</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>400 BAD REQUEST</font>**  
```py  
{  
	"invalid_keys": [  
		"nme",  
		"surplus_key"  
	],  
	"valid_keys": [  
		"description",  
		"name"  
	]  
}  
```  

2. ***Caso 2 -*** *valor passado não é uma string:*  

## **<font color=00FF00>POST</font> /api/comments/&lt;int:id&gt; - Formato da Requisição**  
```py 
{  
	"comments": []  
}  
``` 

## **<font color=00FF00>POST</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**  
```py  
{   
	"error": "Invalid data type. The comment must be of type string"  
}  
```  

3. ***Caso 3 -*** *ID passado na URL não existe ou existe, mas não corresponde ao ID dum grupo ao qual o usuário está inscrito, considerando que o comentário só pode ser postado num grupo em que o usuário já se inscreveu:*  

## **<font color=00FF00>POST</font> /api/comments/&lt;int:id&gt; - Formato da Requisição**  
```py 
{  
	"comments": "Group formed by girls"  
}  
``` 

## **<font color=00FF00>POST</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color='FFA500'>404 NOT FOUND</font>**  
```py  
{   
	"error": "Either you are not subscribed or the group does not exist"  
}  
```  

## **Método <font color=C710AF>GET</font> - /api/comments**  

## **<font color=C710AF>GET</font> /api/comments - Formato da Requisição**  
```py  
No body  
```  

## **<font color=C710AF>GET</font> /api/comments - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
[  
	{  
		"id": 1,  
		"comments": "Group formed by girls",  
		"timestamp": "Wed, 05 May 2022 03:07:49 GMT",  
		"author": {  
			"id": 2,  
			"name": "Juliet Burke",  
			"email": "burkejuliet@uorak.com"  
		}  
	},  
	{  
		"id": 2,  
		"comments": "Group formed by girls and boys",  
		"timestamp": "Wed, 05 May 2022 03:26:41 GMT",  
		"author": {  
			"id": 2,  
			"name": "Juliet Burke",  
			"email": "burkejuliet@uorak.com"  
		}  
	}  
]  
```    

Busca de um grupo específico por ID:
## **<font color='C710AF'>GET</font> /api/comments/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body  
```  

## **<font color='C710AF'>GET</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
{  
	"id": 20,  
	"comments": "Hi, ladies",  
	"timestamp": "Wed, 05 May 2022 03:26:41 GMT",  
	"author": {  
		"id": 2,  
		"name": "Juliet Burke",  
		"email": "burkejuliet@uorak.com"  
	}  
}  
```       

### ***Requisição <font color='F70D1A'>ERRADA</font>***  

1. ***Caso 1 -*** *id passado na URL não existe:*  

## **<font color='C710AF'>GET</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>404 NOT FOUND</font>**  
```py  
{  
	"msg": "Non-existent comment"  
}  
```  

## **Método <font color='FFFF2E'>PATCH</font> - /api/comments/&lt;int:id&gt;**  

Rota de atualização do comentário do usuário que exige autenticação, do contrário status 422.  
### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=FFFF2E>PATCH</font> /api/comments/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"comments": "Hi, girls"  
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>200 OK</font>**  
```py  
{  
	"id": 19,  
	"comments": "Hi, girls",  
	"timestamp": "Wed, 05 May 2022 03:36:41 GMT",  
	"user": {  
		"id": 2,  
		"name": "Juliet Burke"  
	}  
}   
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *chave errada:*  

## **<font color=FFFF2E>PATCH</font> /api/comments/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"commets": "Hi, girls"  
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>400 BAD REQUEST</font>**  
```py  
{   
	"valid_key": "comment",  
	"invalid_keys": [  
		"commets"  
	]  
}   
```  

2. ***Caso 2 -*** *id passado na URL não existe no banco:*  

## **<font color=FFFF2E>PATCH</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>404 NOT FOUND</font>**  
```py  
{  
	"msg": "Non-existent comment"  
}  
```  

3. ***Caso 3 -*** *id passado na URL referencia um comentário não criado pelo usuário:*  

## **<font color=FFFF2E>PATCH</font> /api/comments/&lt;int:id&gt; - Formato da Requisição**  
```py  
{  
	"commets": "Hi, girls"  
}  
```  

## **<font color=FFFF2E>PATCH</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>200 OK</font>**  
```py  
{  
	"msg": "It is possible to update only your comments"  
}   
```  

## **Método <font color='F70D1A'>DELETE</font> - /api/comments/&lt;int:id&gt;**  

Rota de deleção do comentário do usuário que exige autenticação, do contrário status 422.  

### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=F70D1A>DELETE</font> /api/comments/&lt;int:id&gt; - Formato da Requisição**  
```py  
No body  
```  

## **<font color=F70D1A>DELETE</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=00FF00>204 NO CONTENT</font>**  
```ja  
No body returned for response 
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *caso o ID passado inexista:*  

## **<font color=F70D1A>DELETE</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>404 NOT FOUND</font>**  
```py  
{  
	"msg": "Non-existent comment"  
}  
```  

2. ***Caso 2 -*** *comentário a ser excluído não foi feito pelo usuário:*  

## **<font color=F70D1A>DELETE</font> /api/comments/&lt;int:id&gt; - Formato da Resposta - <font color=FFA500>401 UNAUTHORIZED</font>**  
```py  
{  
	"msg": "It is possible to delete only your comments"   
}  
```  

# **Readme Colors**

**GREEN** 	  -		00FF00  
**ORANGE** 	  -		FFA500  
**PURPLE**	  -		C710AF  
**YELLOW**	  -		FFFF2E  
**RED** 	  -		F70D1A  
**BLUE**	  - 	0096FF  

***  
## **Team**   

![Matheus Serafim](https://avatars.githubusercontent.com/u/77494384?s=32&v=4)  
Matheus Serafim - Scrum Master    

![Leandro Medvedev](https://avatars.githubusercontent.com/u/88355581?s=32&v=4)  
Leandro Medvedev - Tech Lead   

![Marta Lima](https://avatars.githubusercontent.com/u/88337182?s=32&v=4)  
Marta Lima - Product Owner  

![Jonatas Heiderich](https://avatars.githubusercontent.com/u/91901328?s=32&v=4)  
Jonatas Heiderich - Quality Assurance  

![Miguel Leite](https://avatars.githubusercontent.com/u/88355609?s=32&v=4)  
Miguel Leite - Quality Assurance  

![Samuel Manga](https://avatars.githubusercontent.com/u/86072678?s=32&v=4)  
Samuel Manga - Quality Assurance  

##### **Made with python_passion. We hope you like it.**  🙋🏽
##### **3rd May 2022, Brazil**  

![GitHub followers](https://img.shields.io/github/followers/leandromedvedev?style=social)  
