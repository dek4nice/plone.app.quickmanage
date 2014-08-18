from Products.Five.browser import BrowserView
from zope.component import getUtility
from Products.CMFCore.interfaces import ISiteRoot

class DevelopSiteManageLinks(BrowserView):


    def __call__(self):
        self.update()
        return self.render()

    def update(self):
        portal = getUtility(ISiteRoot)
        self.portal_url = self.context.portal_url()
        # self.links1 = ['CSS Management','CSS Management','CSS Management',]
        self.links1 = list()
        self.links2 = list()

        self.links1.append(('manage_propertiesForm' , 'property'))
        self.links1.append(('portal_properties/manage_main' , 'properties'))
        self.links1.append(('portal_catalog/manage_catalogView' , 'catalog'))
        self.links1.append(('portal_types/manage_main' , 'types'))
        self.links1.append(('portal_setup/manage_importSteps' , 'setup'))
        self.links1.append(('portal_skins/manage_propertiesForm' , 'skins'))
        self.links1.append(('portal_css/manage_cssComposition' , 'stylesheets'))
        self.links1.append(('portal_javascripts/manage_jsComposition' , 'javascripts'))
        self.links1.append(('portal_quickinstaller/manage_workspace' , 'quickinstaller'))

        self.links2.append(('@@folder_contents' , 'contents'))
        self.links2.append(('@@manage-portlets' , 'portlets'))
        self.links2.append(('@@manage-viewlets' , 'viewlets'))
        self.links2.append(('plone_control_panel' , 'control'))
        self.links2.append(('portal_registry?q=prime' , 'registryprime'))
        # self.resp =  self.context.REQUEST.RESPONSE

    def render(self):
        return self.index()
