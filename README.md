# microservice
Teste de comunicação entre serviços usando RabbitMQ

Aplicação que simula um sensor enviado dados para o servidor. São três serviços que se comunicam entre si, o producer(main.py) envia os dados para o RabbitMQ e o consumer(receive) consome e armazena no banco de dados PostgreSQL. Por último o serviço app.py(Flask) é responsável por mostrar os dados em uma lista.

Utilizar docer-compose para testar a aplicação.

http://0.0.0.0:5001/sensors?sensor=S01&temperature=40&huminity=25 - Envio dos dados para o RabbitMQ.

http://0.0.0.0:5000/ - Serviço em Flask para consulta dos dados.
