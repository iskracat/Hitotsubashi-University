from zope.interface import Interface, Attribute
from zope import schema

from iskra.audiofile import _


class IMediaElementJSPlayable(Interface):
    """A file playable with mediaelementjs
    """
    audiofile = Attribute("Audio file")

    image = Attribute("Image file")

class IVideo(IMediaElementJSPlayable):
    """Marker interface for files that contain mp4 content
    """



class IMediaInfo(Interface):
    """Information about a video object
    """
    width = schema.Int(title=_(u"Width"), required=False)
    height = schema.Int(title=_(u"Height"), required=False)
    duration = schema.Timedelta(title=_(u"Duration"), required=False)
