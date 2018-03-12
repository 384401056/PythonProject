# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.pets import Pets
from .api.pets_petId import PetsPetid


routes = [
    dict(resource=Pets, urls=['/pets'], endpoint='pets'),
    dict(resource=PetsPetid, urls=['/pets/<petId>'], endpoint='pets_petId'),
]