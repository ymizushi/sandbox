# -*- coding: utf-8 -*-

from enum import Enum


class Role(Enum):
    admin = 0
    staff = 1
    user = 2


class UserStatus(Enum):
    inactive = 0
    new = 1
    active = 2