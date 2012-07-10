# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner
from zope.publisher.browser import BrowserView

from iskra.audiofile.content import IAudioFile
from Products.ATContentTypes.interfaces.news import IATNewsItem


class AudioList(BrowserView):
    __call__ = ViewPageTemplateFile('listing.pt')

    def getAudioFiles(self):
        context = aq_inner(self.context)
        pc = getToolByName(context, "portal_catalog")
        folder_path = '/'.join(context.getPhysicalPath())
        return pc(object_provides=IAudioFile.__identifier__,
            path={'query': folder_path, 'depth': 1})

