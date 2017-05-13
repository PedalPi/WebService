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

class integer(object):
    """
    Convert the informed args to integer
    """
    def __init__(self, *args):
        self.args = args

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            for arg in self.args:
                kwargs[arg] = int(kwargs[arg])
            f(*args, **kwargs)

        return wrapped