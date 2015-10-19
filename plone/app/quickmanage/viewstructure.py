from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from Products.CMFCore.interfaces import ISiteRoot
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.interfaces import ITypesTool
# from plone.folder.interfaces import IOrderableFolder
from Products.CMFCore.interfaces._content import IFolderish

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
        # self.types = getUtility(ITypesTool)
        self.view_url = '{0}/@@{1}'.format(self.context.absolute_url() , self.__name__)
        self.types = getToolByName(self.context, 'portal_types')
        self.catalog = getToolByName(self.context, 'portal_catalog')
        self.filter_provides = 'Products.CMFCore.interfaces._content.IContentish'
        self.isFolder = IFolderish.providedBy(self.context)
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
            # out.append(str(contentish_next))
            contentish_next = zcatalogbrain_next.getObject()
            isFolder = IFolderish.providedBy(contentish_next)
            out.append(self.render_item(zcatalogbrain_next , isFolder , level))
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
    def render_item(self , item , isFolder , level=0):
        # "%s/%s [%s] (%s)" % (portal_type, meta_type, review_state, getId)
        level_string = '|---' * level
        type = "%s / %s" % (item.portal_type, item.meta_type)
        state = item.review_state
        id = item.getId
        url = item.getURL()
        title = item.Title.decode('utf-8')
        return self.mybrainsitem_template(type=type , state=state , id=id , level=level , level_string=level_string , url=url , title=title , isfolder=isFolder)

    context_buttons_template = ViewPageTemplateFile('templates/sitestructure-context-view.pt')
    def render_context(self):
        id = self.context.id
        url = self.context.absolute_url()
        title = self.context.Title().decode('utf-8')
        type = "%s / %s" % (self.context.portal_type, self.context.meta_type)
        return self.context_buttons_template(type=type , id=id , url=url , title=title)

    def render(self):
        # return self.walker_next(self.context , -1)
        return self.index()
