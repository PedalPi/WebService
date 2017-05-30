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

from webservice.handler.abstract_request_handler import AbstractRequestHandler
from webservice.util.handler_utils import integer

from application.controller.current_controller import CurrentController
from application.controller.banks_controller import BanksController


class CurrentPedalboardHandler(AbstractRequestHandler):
    controller = None
    banks = None

    def initialize(self, app, webservice):
        super(CurrentPedalboardHandler, self).initialize(app, webservice)
        self.controller = app.controller(CurrentController)
        self.banks = app.controller(BanksController)

    @integer('bank_index', 'pedalboard_index')
    def put(self, bank_index, pedalboard_index):
        bank_changed_and_pedalboard_not_changed = self.controller.bank_number != bank_index \
                                              and self.controller.pedalboard_number == pedalboard_index

        bank = self.banks.banks[bank_index]
        pedalboard = bank.pedalboards[pedalboard_index]

        self.controller.set_bank(bank, notify=bank_changed_and_pedalboard_not_changed, token=self.token)
        self.controller.set_pedalboard(pedalboard, token=self.token)
