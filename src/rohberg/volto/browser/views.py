from Products.Five import BrowserView
import logging

logger = logging.getLogger("views of rohberg.igib")


class PDBView(BrowserView):
    def __call__(self):
        context = self.context
        ctx = context.aq_base

        import pdb; pdb.set_trace()

        return 'pdb view done.'
