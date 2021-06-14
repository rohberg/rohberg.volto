# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from rohberg.volto.testing import ROHBERG_VOLTO_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that rohberg.volto is properly installed."""

    layer = ROHBERG_VOLTO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rohberg.volto is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'rohberg.volto'))

    def test_browserlayer(self):
        """Test that IRohbergVoltoLayer is registered."""
        from rohberg.volto.interfaces import (
            IRohbergVoltoLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IRohbergVoltoLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ROHBERG_VOLTO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['rohberg.volto'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if rohberg.volto is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'rohberg.volto'))

    def test_browserlayer_removed(self):
        """Test that IRohbergVoltoLayer is removed."""
        from rohberg.volto.interfaces import \
            IRohbergVoltoLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IRohbergVoltoLayer,
            utils.registered_layers())
