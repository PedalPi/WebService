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

import uuid
import unittest
import requests

from wstest.rest_facade import RestFacade

from pluginsmanager.model.bank import Bank
from pluginsmanager.model.pedalboard import Pedalboard

from pluginsmanager.model.lv2.lv2_effect_builder import Lv2EffectBuilder


class Test(unittest.TestCase):
    address = 'http://localhost:3000/v1/'

    SUCCESS = 200
    CREATED = 201
    UPDATED = 200
    DELETED = 200

    ERROR = 400
    rest = RestFacade()

    plugins_builder = Lv2EffectBuilder()

    def setUp(self):
        try:
            self.rest.get('')
        except requests.exceptions.ConnectionError:
            self.fail("Server is down")

    @property
    def default_bank_mock(self):
        bank = BankMock('REST - Default Bank' + str(uuid.uuid4()))
        pedalboard = Pedalboard('REST - Default Pedalboard')

        reverb = self.plugins_builder.build('http://calf.sourceforge.net/plugins/Reverb')
        reverb2 = self.plugins_builder.build('http://calf.sourceforge.net/plugins/Reverb')

        bank.append(pedalboard)

        pedalboard.append(reverb)
        pedalboard.append(reverb2)

        reverb.outputs[0].connect(reverb2.inputs[0])

        return bank


class BankMock(Bank):

    def __init__(self, name):
        super().__init__(name)

        self._index = -1

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
