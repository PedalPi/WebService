# Copyright 2017 SrMouraSilva
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from application.controller.current_controller import CurrentController
from webservice.handler.abstract_request_handler import AbstractRequestHandler
from webservice.util.auth import RequiresAuthMixing


class CurrentHandler(RequiresAuthMixing, AbstractRequestHandler):
    controller = None

    def initialize(self, app, webservice):
        super(CurrentHandler, self).initialize(app, webservice)
        self.controller = app.controller(CurrentController)

    def prepare(self):
        self.auth()

    def get(self):
        json = {
            'bank': self.controller.bank.index,
            'pedalboard': self.controller.pedalboard.index
        }

        self.send(200, json)
