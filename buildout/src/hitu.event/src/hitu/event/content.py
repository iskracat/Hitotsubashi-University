from plone.directives import form
from five import grok
from zope import schema
from Acquisition import aq_inner
from plone.namedfile.field import NamedImage, NamedFile
from hitu.event import _

from z3c.relationfield.schema import RelationChoice, RelationList

from plone.formwidget.autocomplete.widget import (
    AutocompleteMultiFieldWidget, AutocompleteFieldWidget,
    )
from plone.formwidget.contenttree import (
    ContentTreeFieldWidget,
    ObjPathSourceBinder,
    )

class IVocaLanguageList(form.Schema):
    """ Marker Vocabulary
    """


class IVocaEventTypeList(form.Schema):
    """ Marker Vocabulary
    """


class IVocaOrganitzingBodyList(form.Schema):
    """ Marker Vocabulary
    """


class IVocaLocationList(form.Schema):
    """ Marker Vocabulary
    """


class IHitUEvent(form.Schema):

    form.widget(event_language=AutocompleteFieldWidget)
    event_language = RelationChoice(title=_(u"Event Language"),
                       description=_(u"The language the event is being held in"),
                       required=True,
                       source=ObjPathSourceBinder(portal_type='hitu.event.language'))

    form.widget(event_type=AutocompleteFieldWidget)
    event_type = RelationChoice(title=u"Event Type",
                       description=_(u"Symposium, workshop, lecture, etc."),
                       required=True,
                       source=ObjPathSourceBinder(object_provides=IVocaEventTypeList.__identifier__))

    subtitle = schema.TextLine(title=_(u"Subtitle"),
                       description=_(u"Enter the subtitle, if there is one."))

    speaker = schema.TextLine(title=_(u"Speaker"),
                       description=_(u"Name(s) of person(s) speaking"))

    form.widget(organized_by=AutocompleteMultiFieldWidget)
    organized_by = RelationList(title=_(u"Organized by"),
                           description=_(u"The body or bodies organizing the event."),
                           required=False,
                           value_type=RelationChoice(title=u"Multiple",
                             source=ObjPathSourceBinder(object_provides=IVocaOrganitzingBodyList.__identifier__)))

    form.widget(location=AutocompleteFieldWidget)
    location = RelationChoice(title=u"Location",
                       description=_(u"The place where the event will take place"),
                       required=True,
                       source=ObjPathSourceBinder(object_provides=IVocaLocationList.__identifier__))

    audio_recording = NamedFile(title=_(u"Audio Recording"), required=False,)
