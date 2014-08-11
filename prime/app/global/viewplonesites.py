from Products.Five.browser import BrowserView

class YourSitesView(BrowserView):
    """ @@prime-app-global view for root plone instance """

    def __call__(self):
        self.update()
        return self.render()

    def update(self):
        self.sites = [zopeobject for zopeobject in self.context.objectValues() if zopeobject.meta_type == 'Plone Site'] # objectIds()
        return

    def render(self):
        return self.index()
