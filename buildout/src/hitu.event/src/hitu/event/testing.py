from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class HituEvent(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import hitu.event
        xmlconfig.file('configure.zcml',
                       hitu.event,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'hitu.event:default')

HITU_EVENT_FIXTURE = HituEvent()
HITU_EVENT_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(HITU_EVENT_FIXTURE, ),
                       name="HituEvent:Integration")