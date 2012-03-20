# -*- coding: utf8 -*-
""" develop command tests.
"""
import os

from distutils import log
from distutils.command.install import install
from distribute.command.build_egg_info import build_egg_info

class develop(install):
    """Installs the package in development mode by linking the source
    to site-packages."""

    description = "install package in 'development mode'"

    user_options = install.user_options + \
            [("uninstall", "u", "Uninstall this source package")]

    def initialize_options(self):
        install.initialize_options(self)
        self.uninstall = None

    def finalize_options(self):
        install.finalize_options(self)
        if self.uninstall is None:
            self.uninstall = False
        # Ensure metadata is up-to-date
        build_egg_info = self.get_finalized_command('build_egg_info')
        build_egg_info.run()
        egg_base, egg_info = os.path.split(build_egg_info.egg_info_path)
        egg_pth = os.path.splitext(egg_info)[0] + '.pth'

        # create an .pth in the installation dir, pointing to our egg
        self.egg_base = os.path.abspath(egg_base)
        self.egg_pth = os.path.join(egg_base, egg_pth)

    def run(self):
        # Build extensions in-place
        build_ext = self.get_finalized_command('build_ext')
        build_ext.inplace = 1
        build_ext.run()
        if self.uninstall:
            self._uninstall_link()
        else:
            self._install_for_development()

    def _install_for_development(self):
        # XXX need to add in .pth all parent folder
        # of all packages and modules defined in the install options
        log.info("Creating %s (link to %s)", self.egg_pth, self.egg_base)
        if not self.dry_run:
            f = open(self.egg_pth, "w")
            f.write(self.egg_base)
            f.close()

    def _uninstall_link(self):
        if os.path.exists(self.egg_pth):
            log.info("Removing %s (link to %s)", self.egg_pth, self.egg_base)
            if not self.dry_run:
                os.unlink(self.egg_pth)
        if self.distribution.scripts:
            # XXX should also check for entry point scripts!
            log.warn("Note: you must uninstall or replace scripts manually!")

