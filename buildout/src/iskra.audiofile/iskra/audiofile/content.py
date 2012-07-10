from plone.directives import form
from five import grok
from plone.multilingualbehavior import directives
from zope import schema
from Acquisition import aq_inner
from plone.namedfile.field import NamedImage, NamedFile
from iskra.audiofile import _
import os

from iskra.audiofile.interfaces import IMediaInfo


class IAudioFile(form.Schema):
    audiofile = NamedFile(title=_(u"File MP3"),)

    audiofileogg = NamedFile(title=_(u"File Ogg"), required=False,)

    directives.languageindependent('image')
    image = NamedImage(title=_(u"Image"),)



class View(grok.View):
    grok.context(IAudioFile)
    grok.require('zope2.View')

    def video(self):
        info = IMediaInfo(self.context)
        return dict(title=self.context.Title(),
            description=self.context.Description(),
            height=info.height,
            width=info.width,
            duration=info.duration)

    def getFilename(self):
        context = aq_inner(self.context)
        return context.audiofile.filename


