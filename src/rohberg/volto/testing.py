# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import rohberg.volto


class RohbergVoltoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=rohberg.volto)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rohberg.volto:default')


ROHBERG_VOLTO_FIXTURE = RohbergVoltoLayer()


ROHBERG_VOLTO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ROHBERG_VOLTO_FIXTURE,),
    name='RohbergVoltoLayer:IntegrationTesting',
)


ROHBERG_VOLTO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ROHBERG_VOLTO_FIXTURE,),
    name='RohbergVoltoLayer:FunctionalTesting',
)


ROHBERG_VOLTO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ROHBERG_VOLTO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RohbergVoltoLayer:AcceptanceTesting',
)
