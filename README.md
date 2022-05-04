# **&lt;code_by_girls/&gt; API..**  
![GitHub top language](https://img.shields.io/github/languages/top/leandromedvedev/cap-alexandre-g05?color=yellow&style=plastic)  
![GitHub language count](https://img.shields.io/github/languages/count/leandromedvedev/cap-alexandre-g05?style=plastic)

A aplicação foi pensada para fomentar a troca de experiências, divulgação de vagas e assuntos correlatos bem como a criação e manutenção de uma rede formada por mulheres que já atuam ou almejam atuar na área de tecnologia, promovendo um espaço seguro e acolhedor para que essa troca possa acontecer.

## **Endpoints**  

Há um total de 28 endpoints.

#### **Method                  |               Endpoint**

* POST     /api/users  
* GET      /api/users  
* GET      /api/users/&lt;int:id&gt;  
* PATCH    /api/users/&lt;int:id&gt;  
* DELETE   /api/users/&lt;int:id&gt; 
* POST     /api/comments  
* DELETE   /api/comments/&lt;int:id&gt;  
* GET      /api/comments  
* GET      /api/comments/&lt;int:id&gt;  
* PATCH    /api/comments/&lt;int:id&gt;  
* POST     /api/groups  
* DELETE   /api/groups/&lt;int:id&gt;  
* GET      /api/groups/&lt;int:id&gt;  
* GET      /api/groups  
* PATCH    /api/groups/&lt;int:id&gt;  
* POST     /api/login  
* PATCH    /api/users/skills/&lt;int:id&gt;  
* POST     /api/users/skills  
* DELETE   /api/users/skills/&lt;int:id&gt;  
* GET      /api/users/skills  
* GET      /api/users/skills/&lt;int:id&gt;  
* DELETE   /api/groups/subscribes/&lt;int:id&gt;  
* GET      /api/groups/subscribes  
* POST     /api/groups/subscribes   
* POST     /api/users/works  
* DELETE   /api/users/works/&lt;int:work_id&gt;  
* GET      /api/users/works  
* PATCH    /api/users/works/&lt;int:work_id&gt;  

***  
## **Users**  

* POST     /api/users  
* GET      /api/users  
* GET      /api/users/&lt;int:id&gt;  
* PATCH    /api/users/&lt;int:id&gt;  
* DELETE   /api/users/&lt;int:id&gt; 

Rotas responsáveis pela criação, busca, atualização e deleção de usuário. 

## **Método <font color=lime>POST</font> - /api/users**  
Campos obrigatórios:  

* name  
* email  
* password  
  
### ***Requisição <font color='0096FF'>CORRETA</font>***

## **<font color=lime>POST</font> /api/users - Formato da Requisição**  
```py  
{  
	"name": "Juliet Burke",  
	"email": "burkejuliet@lost.com",  
	"password": "wW*8uuuu"  
}  
```  

## **<font color=lime>POST</font> /api/users - Formato da Resposta - <font color=lime>201 CREATED</font>**  
```py  
{  
	"id": 1,  
	"name": "Juliet Burke",  
	"email": "burkejuliet@lost.com",  
	"skills": [],  
	"works": []  
}  
```  

### ***Requisições <font color='F70D1A'>ERRADAS</font>***  

1. ***Caso 1 -*** *um dos campos obrigatórios não é passado:*
## **<font color=lime>POST</font> /api/users - Formato da Requisição**  
```py  
{
	"email": "burkejuliet@lost.com",
	"password": "wW*8uuuu"
}
```  

## **<font color=lime>POST</font> /api/users - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**  
```py  
{  
	"error": "name, email and password are mandatory keys"  
}  
```  

2. ***Caso 2 -*** *os campos obrigatórios são passados, mas um ou mais deles contêm erro de grafia:*  

## **<font color=lime>POST</font> /api/users - Formato da Requisição**  
```py  
{  
	"na": "Juliet Burke",  
	"ema": "burkejuliet@lost.com",  
	"pass": "wW*8uuuu"  
}  
```  

## **<font color=lime>POST</font> /api/users - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**  
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

## **<font color=lime>POST</font> /api/users - Formato da Requisição**  
```py  
{  
	"name": "Juliet Burke",  
	"email": "burkejuliet@lost.com",  
	"password": "wW*8uuuu"  
}  
```  

## **<font color=lime>POST</font> /api/users - Formato da Resposta - <font color='FFA500'>409 CONFLICT</font>**  
```py  
{  
	"error": "Email is already exists"  
}  
```  

***
## **Login**  

## **Método <font color=lime>POST</font> - /api/login**  


* POST     /api/login  

Rota responsável pelo login do usuário.  
Campos obrigatórios:  

* email  
* password  

### ***Requisição <font color='0096FF'>CORRETA</font>***  

## **<font color=lime>POST</font> /api/login - Formato da Requisição**  
```py  
{
	"email": "burkejuliet@lost.com",
	"password": "wW*8uuuu"
}
```  

## **<font color=lime>POST</font> /api/login - Formato da Resposta - <font color=lime>200 OK</font>**  
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
## **<font color=lime>POST</font> /api/login - Formato da Requisição**
```py  
{  
	"email": "burkejuliet@lost.com"  
}  
```  

## **<font color=lime>POST</font> /api/login - Formato da Resposta - <font color='FFA500'>400 BAD REQUEST</font>**  
FALTANDO  (Matheus fará este tratamento)

2. ***Caso 2 -*** *o email digitado é incorreto:*  

## **<font color=lime>POST</font> /api/login - Formato da Requisição**  
```py  
{  
	"email": "burkejuliet@lost",  
	"password": "wW*8uuuu"  
}  
```  

## **<font color=lime>POST</font> /api/login - Formato da Resposta - <font color='FFA500'>404 NOT FOUND</font>**  
```py  
{  
	"error": "User not found!"  
}  
```  

3. ***Caso 3 -*** *o password digitado é incorreto:*  

## **<font color=lime>POST</font> /api/login - Formato da Requisição**  
```py  
{  
	"email": "burkejuliet@lost.com",  
	"password": "senha_errada"  
}  
```  

## **<font color=lime>POST</font> /api/login - Formato da Resposta - <font color='FFA500'>401 UNAUTHORIZED</font>**
```py  
{  
	"error": "Unauthorized"  
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

## **<font color='C710AF'>GET</font> /api/users - Formato da Resposta - <font color=lime>200 OK</font>**  
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

## **<font color='C710AF'>GET</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color=lime>200 OK</font>**  
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

## **<font color='FFFF2E'>PATCH</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color=lime>200 OK</font>**   
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

## **<font color='E10600'>DELETE</font> /api/users/&lt;int:id&gt; - Formato da Resposta - <font color=lime>204 NO CONTENT</font>**  
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

1. ***Caso 2 -*** *id passado não está cadastrado:*  

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
## **Groups**  


***  
## **Comments**  


***  
## **Users Skills**  


***  
## **Works**  


***  
## **Groups Subscribes**   










![GitHub followers](https://img.shields.io/github/followers/leandromedvedev?style=social)