from Products.Five.browser import BrowserView

class YourSitesView(BrowserView):
    """ @@prime-app-global view for root plone instance """

    actions = [
        ('dev' , '@@dev-links'),
        ('manage' , 'manage'),
        ('QI' , 'portal_quickinstaller/manage_workspace'),
        ('FC' , '@@folder_contents'),
    ]

    def __call__(self):
        self.update()
        return self.render()

    def update(self):
        self.sites = [zopeobject for zopeobject in self.context.objectValues() if zopeobject.meta_type == 'Plone Site'] # objectIds()
        self.siteactions = [{'title':action[0] , 'url':action[1]} for action in self.actions]

    def render(self):
        return self.index()
