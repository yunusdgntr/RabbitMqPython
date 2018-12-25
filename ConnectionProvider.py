import pika

HOST_NAME = "127.0.0.1"
USERNAME = "test"
PASSWORD = "test"
credentials = pika.PlainCredentials(USERNAME, PASSWORD)
parameters = pika.ConnectionParameters(HOST_NAME, 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
