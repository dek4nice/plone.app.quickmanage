from Products.Five.browser import BrowserView

class SiteStatusView(BrowserView):
    """ @@prime-app-global view for root plone instance """

    def __call__(self):
        self.update()
        return self.render()

    def update(self):
        self.site = None
        sites = [zopeobject for zopeobject in self.context.objectValues() if zopeobject.meta_type == 'Plone Site'] # objectIds()
        if len(sites) == 1:
            self.site = sites[0].id
        elif len(sites) > 1:
            self.site = str([s.id for s in sites])
        return

    def render(self):
        return self.index()
