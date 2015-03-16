from Products.Five.browser import BrowserView

class TestView(BrowserView):
    """ @@prime-app-global view for root plone instance """

    def __call__(self):
        self.update()
        return self.render()

    def update(self):
        return

    def render(self):
        return self.index()
