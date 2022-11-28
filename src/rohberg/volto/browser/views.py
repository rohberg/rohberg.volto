from importlib import import_module

from Products.Five import BrowserView
import logging

logger = logging.getLogger("views of rohberg.igib")


class PDBView(BrowserView):
    def __call__(self):
        context = self.context
        ctx = context.aq_base

        PLONE_6 = getattr(
            import_module("Products.CMFPlone.factory"), "PLONE60MARKER", False
        )
        print("PLONE_6", PLONE_6)

        import pdb

        pdb.set_trace()

        return "pdb view done."
