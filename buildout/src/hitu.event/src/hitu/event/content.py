from plone.directives import form
from five import grok
from zope import schema
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

from Products.CMFPlone.i18nl10n import ulocalized_time
from plone.event.utils import is_same_day, is_same_time
from plone.app.event.base import DT
from plone.app.event.interfaces import IEventAccessor


def prepare_for_display(context, start, end, whole_day):
    """ Return a dictionary containing pre-calculated information for building
    <start>-<end> date strings.

    Keys are:
        'start_date' - date string of the start date
        'start_time' - time string of the start date
        'end_date'   - date string of the end date
        'end_time'   - time string of the end date
        'start_iso'  - start date in iso format
        'end_iso'    - end date in iso format
        'same_day'   - event ends on the same day
        'same_time'  - event ends at same time
    """

    # The behavior os ulocalized_time() with time_only is odd.
    # Setting time_only=False should return the date part only and *not*
    # the time
    #
    # ulocalized_time(event.start(), False,  time_only=True, context=event)
    # u'14:40'
    # ulocalized_time(event.start(), False,  time_only=False, context=event)
    # u'14:40'
    # ulocalized_time(event.start(), False,  time_only=None, context=event)
    # u'16.03.2010'

    # this needs to separate date and time as ulocalized_time does
    DT_start = DT(start)
    DT_end = DT(end)
    start_date = ulocalized_time(DT_start, long_format=False, time_only=None,
                                 context=context)
    start_time = ulocalized_time(DT_start, long_format=False, time_only=True,
                                 context=context)
    end_date = ulocalized_time(DT_end, long_format=False, time_only=None,
                               context=context)
    end_time = ulocalized_time(DT_end, long_format=False, time_only=True,
                               context=context)
    same_day = is_same_day(start, end)
    same_time = is_same_time(start, end)

    # set time fields to None for whole day events
    if whole_day:
        start_time = end_time = None

    return  dict(start_date=start_date,
                 start_time=start_time,
                 start_iso=start.isoformat(),
      
           end_date=end_date,
                 end_time=end_time,
                 end_iso=end.isoformat(),
                 same_day=same_day,
                 same_time=same_time)


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

    form.widget(event_location=AutocompleteFieldWidget)
    event_location = RelationChoice(title=u"Location",
                       description=_(u"The place where the event will take place"),
                       required=True,
                       source=ObjPathSourceBinder(object_provides=IVocaLocationList.__identifier__))

    audio_recording = NamedFile(title=_(u"Audio Recording"), required=False,)


class View(grok.View):
    grok.context(IHitUEvent)
    grok.require('zope2.View')

    static = ""

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.data = IEventAccessor(self.context)

    def date_for_display(self):
        return prepare_for_display(
                self.context,
                self.data['start'],
                self.data['end'],
                self.data['whole_day'])

