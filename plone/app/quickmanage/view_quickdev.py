from Products.Five.browser import BrowserView
from zope.component import getUtility
from Products.CMFCore.interfaces import ISiteRoot
from zope.component import getMultiAdapter
import urllib

class DevelopSiteManageLinks(BrowserView):

    """ @@quickdev """

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
        self.links1.append(('manage_UndoForm' , 'undo'))
        self.links1.append((self.get_search_old_types_url() , 'oldsearch'))

        self.links1.append(('portal_actions/manage_workspace' , 'actions'))
        self.links1.append(('portal_types/manage_main' , 'types'))
        self.links1.append(('portal_css/manage_cssComposition' , 'stylesheets'))
        self.links1.append(('portal_javascripts/manage_jsComposition' , 'javascripts'))

        self.links1.append(('portal_catalog/manage_catalogView' , 'catalog'))
        self.links1.append(('portal_setup/manage_importSteps' , 'setup'))
        self.links1.append(('portal_quickinstaller/manage_workspace' , 'quickinstaller'))

        self.links1.append(('portal_skins/manage_propertiesForm' , 'skins'))

        self.links2.append(('@@folder_contents?show_all=true' , 'contents'))
        self.links2.append(('@@manage-portlets' , 'portlets'))
        self.links2.append(('@@manage-viewlets' , 'viewlets'))
        self.links2.append(('portal_registry?q=prime' , 'registryprime'))
        self.links2.append(('@@dexterity-types' , 'dexterity'))

        # plone/app/controlpanel/overview.py
        overview_state = getMultiAdapter((self.context, self.request), name=u'overview-controlpanel')
        self.plone_sublist = overview_state.sublists('Plone')
        # self.resp =  self.context.REQUEST.RESPONSE

    def get_search_old_types_url(self):
        obj_metatypes = ['Controller Page Template', 'Folder', 'Controller Python Script', 'Controller Validator', 'Page Template', 'Script (Python)']
        # [o.replace(' ','+') for o in obj_metatypes]
        metatypes_args = ['obj_metatypes:list=' + urllib.quote(o) for o in obj_metatypes]
        vars = {
            'obj_ids:tokens' : '',
            'obj_searchterm' : '',
            'obj_mspec' : '<',
            'obj_mtime' : '',
            'search_sub:int' : '1',
            'btn_submit' : 'Find'
        }
        other_args = [name + '=' + urllib.quote(value) for name , value in vars.items()]
        return 'manage_findResult?' + '&'.join(metatypes_args + other_args)

    def render(self):
        return self.index()
