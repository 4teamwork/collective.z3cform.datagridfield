# -*- coding: utf-8 -*-
from collective.z3cform.datagridfield import row
from plone.registry.field import PersistentField


class DictRow(PersistentField, row.DictRow):
    pass
