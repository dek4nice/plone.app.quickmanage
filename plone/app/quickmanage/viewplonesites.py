from Products.Five.browser import BrowserView

class YourSitesView(BrowserView):
    """ @@prime-app-global view for root plone instance """

    actions = [
        # ('dev' , '@@quickdev'), #moved to link-href attribute
        ('MNG' , 'manage'),
        ('QI' , 'portal_quickinstaller/manage_workspace'),
        ('FC' , '@@folder_contents'),
    ]

    def __call__(self):
        self.update()
        self.checkout_mail_hosts()
        return self.render()

    def update(self):
        self.sites = [zopeobject for zopeobject in self.context.objectValues() if zopeobject.meta_type == 'Plone Site'] # objectIds()
        self.siteactions = [{'title':action[0] , 'url':action[1]} for action in self.actions]

    def checkout_mail_hosts(self):
        self.mail_hosts_detected = list()
        for site in self.sites:
            if 'MailHost' in site.objectIds():
                self.mail_hosts_detected.append(site.id)

    def render(self):
        return self.index()
