# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2021 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

from userge import userge
from flask import Flask, request
from flask_restful import Resource, Api

main()
app = Flask(_name_)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return 'Hello World!'
api.add_resource(Greeting, '/')

if __name__ == "__main__":
    app.run('0.0.0.0','8080')
    userge.begin()
