import time
import ConnectionProvider


def callback(ch, method, properties, body):
    process_result = False
    print " [x] Received %r" % (body,)
    process_result = True
    time.sleep(body.count('.'))
    #Do process here than change process_result
    print " [x] Done"
    if process_result:
        login_success()
    else:
        login_failed()
    ch.basic_ack(delivery_tag=method.delivery_tag)


def login_success():
    ConnectionProvider.channel.basic_publish(exchange='', routing_key='loginResult', body='ok')


def login_failed():
    ConnectionProvider.channel.basic_publish(exchange='', routing_key='loginResult', body='failed')


ConnectionProvider.channel.basic_qos(prefetch_count=1)
ConnectionProvider.channel.basic_consume(callback, queue='loginCheck')
ConnectionProvider.channel.start_consuming()
