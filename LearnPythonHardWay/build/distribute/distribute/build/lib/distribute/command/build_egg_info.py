# -*- coding: utf8 -*-
""" build_egg_info command.
"""
import os
from distutils.core import Command
from distutils import log

from distribute.resources.version import parse_version
from distribute.resources.requirement import parse_requirements
from distribute.resources.util import safe_name, safe_version, to_filename
from distribute.resources.entrypoint import EntryPoint
from distribute.resources.workingset import iter_entry_points

#
# maybe we could rename it to build_metadata
#
class build_egg_info(Command):
    """Builds the distribution's .egg-info metadata directory."""

    description = "create a distribution's .egg-info directory"

    user_options = [
        ('egg-base=', 'e', "directory containing .egg-info directories"
         " (default: top of the source tree)")]

    def initialize_options(self):
        self.egg_name = None
        self.egg_version = None
        self.egg_base = None
        self.egg_info_path = None
        self.broken_egg_info = False

    def finalize_options(self):
        self.egg_name = safe_name(self.distribution.get_name())
        self.egg_version = safe_version(self.distribution.get_version())

        # Check the requirements against syntax errors
        try:
            list(parse_requirements('%s==%s' % (self.egg_name,
                                                self.egg_version)))
        except ValueError:
            raise DistutilsOptionError(
                "Invalid distribution name or version syntax: %s-%s" %
                (self.egg_name, self.egg_version))

        # Determine the base directory (under which the packages can be found)
        if self.egg_base is None:
            dirs = self.distribution.package_dir
            self.egg_base = (dirs or {}).get('', os.getcwd())

        # Make sure the given base directory exists and is really a directory
        self.ensure_dirname('egg_base')

        # Determine the path of the egg-info directory
        self.egg_info_path = os.path.join(self.egg_base,
                                     to_filename(self.egg_name) + '.egg-info')

        # Warn the user if there is a problem with the egg name
        if '-' in self.egg_name:
            self._check_broken_egg_info()

    def _check_broken_egg_info(self):
        bei = self.egg_name + '.egg-info'
        if self.egg_base != os.curdir:
            bei = os.path.join(self.egg_base, bei)
        if os.path.exists(bei):
            log.warn(
                "-"*78+'\n'
                "Note: Your current .egg-info directory has a '-' in its name;"
                '\nthis will not work correctly with "setup.py develop".\n\n'
                'Please rename %s to %s to correct this problem.\n'+'-'*78,
                bei, self.egg_info_path
            )
            self.broken_egg_info = self.egg_info_path
            self.egg_info_path = bei     # make it work for now

    def run(self):
        # create the egg-info folder
        self.mkpath(self.egg_info_path)

        # now fills the egg-info folder
        self._write_pkg_info()   # adds PKG-INFO

        # now iterates over all plugins that may add files in egg-info
        # XXX need to copy to prevent the plugin to change the metadata
        #metadata = self.distribution.metadata
        #for entry_point in iter_entry_points('distribute.egg_info_writers'):
        #    entry_point = entry_point.load()
        #    entry_point(metadata, self.egg_info_path)

    def _write_pkg_info(self):
        filename = os.path.join(self.egg_info_path, 'PKG-INFO')
        log.info("writing %s", filename)
        if not self.dry_run:
            metadata = self.distribution.metadata
            metadata.write_pkg_info(self.egg_info_path)

