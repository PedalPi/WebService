# -*- coding: utf-8 -*-


class WebSocketConnections(object):
    connections = dict()

    @staticmethod
    def register(token, connection):
        WebSocketConnections.connections[connection] = token

    @staticmethod
    def unregister(connection):
        del WebSocketConnections.connections[connection]

    @staticmethod
    def sendBroadcast(data, token=''):
        for connection in WebSocketConnections.connections:
            connection_token = WebSocketConnections.connections[connection]

            if token == '' or token != connection_token:
                connection.write_message(data)
