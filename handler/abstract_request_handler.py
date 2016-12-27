import tornado.web
import json
from tornado_cors import CorsMixin


class AbstractRequestHandler(CorsMixin, tornado.web.RequestHandler):
    CORS_ORIGIN = '*'
    CORS_CREDENTIALS = True
    CORS_MAX_AGE = 21600
    CORS_HEADERS = 'Content-Type, x-xsrf-token'

    @property
    def request_data(self):
        return json.loads(self.request.body.decode('utf-8'))

    def success(self):
        self.send(200)

    def created(self, message):
        self.send(201, message)

    def error(self, message):
        self.send(400, {"error": message})

    def print_error(self):
        import traceback
        import sys
        print(traceback.format_exc(), file=sys.stderr, flush=True)

    def send(self, status, message=None):
        self.clear()
        self.set_status(status)
        self.finish(message)

    @property
    def token(self):
        token = self.request.headers.get('x-xsrf-token')

        return '' if token is None else token

    def get(self, method, args):
        try:
            bank = self.banks.banks[bank_index]
            pedalboard = bank.pedalboards[pedalboard_index]

            return self.write(pedalboard.json)

        except IndexError as error:
            return self.error(str(error))

        except Exception:
            self.print_error()
            return self.send(500)