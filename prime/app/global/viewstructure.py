from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from Products.CMFCore.interfaces import ISiteRoot
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.interfaces import ITypesTool

class SiteStructureView(BrowserView):
    """ @@sitestructure view for root plone instance """

    __name__ = 'sitestructure'
    level = 0
    is_full = False

    def __call__(self,all=False):
        if all:
            self.is_full = True

        self.update()
        return self.render()

    def update(self):
        self.site = None
        # self.portal = getUtility(ISiteRoot)
        self.portal = self.context.portal_url.getPortalObject()
        portal_url = self.portal.absolute_url()
        # portal_url = self.portal.portal_url()
        # self.types = getUtility(ITypesTool)
        self.view_url = '{0}/@@{1}'.format(portal_url , self.__name__)
        self.types = getToolByName(self.context, 'portal_types')
        self.catalog = getToolByName(self.context, 'portal_catalog')
        self.filter_provides = 'Products.CMFCore.interfaces._content.IContentish'
        return
        contentFilter = {
            'meta_type' : 'Cart Item' ,
            'review_state' : ['published','visible'] ,
            'path' : self.filter_path,
            'sort_on':'getObjPositionInParent'
        }
        # self.objects = catalog.queryCatalog(contentFilter, show_all=1, show_inactive=1)
        # self.objects = catalog(object_provides='Products.CMFCore.interfaces._content.IContentish' , sort_on='getObjPositionInParent')
        # self.objects = [o.getObject() for o in self.objects[1:10]]

    def get_filter_path(self , contentish):
        filter_query = '/'.join(contentish.getPhysicalPath())
        filter_depth = 1
        return {'query':filter_query, 'depth':filter_depth,}

    def walker_next(self , contentish_current , level):
        level += 1
        # zcatalogbrain_current
        # zcatalogbrain_next
        current_path = self.get_filter_path(contentish_current)
        out = list()
        for zcatalogbrain_next in self.getZCatalogBrainObjects(current_path):
            contentish_next = zcatalogbrain_next.getObject()
            # out.append(str(contentish_next))
            out.append(self.render_item(zcatalogbrain_next , level))
            if self.is_full:
                out.append(self.walker_next(contentish_next , level))
        return "\n".join(out)

    def getZCatalogBrainObjects(self , path):
        self.objects = self.catalog(object_provides=self.filter_provides , path=path , sort_on='getObjPositionInParent')
        return self.objects
        self.objects = objects
        # self.objects = [o.getObject() for o in objects]
        self.length = 'portal_catalog: %d' % len(self.objects)
        # "%s/%s [%s] (%s)" % (portal_type, meta_type, review_state, getId)

    mybrainsitem_template = ViewPageTemplateFile('templates/sitestructure-mybrainsitem-view.pt')
    def render_item(self,item , level=0):
        # "%s/%s [%s] (%s)" % (portal_type, meta_type, review_state, getId)
        level = '|---' * level
        type = "%s / %s" % (item.portal_type, item.meta_type)
        state = "[%s]" % item.review_state
        id = "(%s)" % item.getId
        url = item.getURL()
        title = item.Title
        return self.mybrainsitem_template(type=type , state=state , id=id , level=level , url=url , title=title)

    def render(self):
        # return self.walker_next(self.portal , -1)
        return self.index()
