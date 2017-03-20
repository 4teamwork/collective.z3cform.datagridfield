# -*- coding: utf-8 -*-
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):

        import collective.z3cform.datagridfield
        self.loadZCML(
            'configure.zcml',
            collective.z3cform.datagridfield,
            context=configurationContext
        )

        import collective.z3cform.datagridfield_demo
        self.loadZCML(
            'configure.zcml',
            collective.z3cform.datagridfield_demo,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'collective.z3cform.datagridfield:default')


FIXTURE = Fixture()
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='collective.z3cform.datagridfield:Functional',
)
