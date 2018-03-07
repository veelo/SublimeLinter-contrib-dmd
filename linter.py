#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Bastiaan N. Veelo
# Copyright (c) 2017, 218 Bastiaan N. Veelo
#
# License: MIT
#
# Functionality for reading DUB configurations was copied from
# github.com/MoritzMaxeiner/sublide, courtesy Moritz Maxeiner.

"""This module exports the Dmd plugin class."""

from SublimeLinter.lint import Linter, util
import os.path
import json
from subprocess import Popen, PIPE


class Dmd(Linter):
    """Provides an interface to dmd, the reference D compiler from dlang.org."""

    syntax = 'd'
    cmd = ('dmd', '-o-', '-w', '-wi', '-vcolumns', '*')
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 2.076.1'
    regex = (
        # Temporary source file (ignored) followed by "(row,col): "
        r'^.+tmp.+[(](?P<line>\d+)([,](?P<col>\d+))?[)]: '
        # Either "Error: ", "Warning: " or "Deprecation: "
        r'(?:(?P<error>Error)|(?P<warning>Warning|Deprecation)): '
        # Single-row message
        r'(?P<message>.+)\r?\n'
        # Ignored rows (without the path to the temp source file)
        r'((.(?!tmp))+\r?\n)*'
    )
    multiline = True
    tempfile_suffix = 'd'
    line_col_base = (1, 1)
    error_stream = util.STREAM_STDERR
    cached_include_paths = dict()
    package_filenames = ['dub.json', 'package.json', 'dub.sdl']

    def get_user_args(self, settings=None):
        """Return any args the user specifies in settings as a list, supplemented with those reported by DUB."""
        window_folders = self.view.window().folders()
        for folder in window_folders:
            if folder not in type(self).cached_include_paths.keys():
                type(self).cached_include_paths[folder] = type(self).get_include_paths(folder)
        user_args = super().get_user_args(settings)
        for paths in type(self).cached_include_paths.values():
            for path in paths:
                user_args += {'-I' + path}
        return user_args

    @classmethod
    def get_include_paths(cls, folder):
        """Return a set of include paths read from DUB configuration files."""
        include_paths = set()
        if cls.has_package_file(folder):
            description = cls.describe(folder)
            if description is not None:
                for index, package in enumerate(description['packages']):
                    base_path = os.path.abspath(package['path'])
                    for sub_path in package['importPaths']:
                        include_paths.add(os.path.join(base_path, sub_path))
        return include_paths

    @classmethod
    def has_package_file(cls, path):
        """Look for DUB configuration files in path."""
        for f in cls.package_filenames:
            p = os.path.join(path, f)
            if (os.path.exists(p)):
                return True
        return False

    @classmethod
    def describe(cls, path):
        """Let DUB describe the project."""
        description = cls.__exec(['describe', '--root=' + path, "--vquiet"])
        if len(description) == 0:
            return None
        try:
            return json.loads(description)
        except ValueError:
            return None

    @classmethod
    def __exec(cls, args):
        """Execute DUB."""
        app_path = "dub"
        # if not util.which(app_path):
        #     print(cls.name() + ': DUB functionality not available, application \"' + app_path + '\" not found.')
        #     return []
        try:
            instance = Popen([app_path] + args, stdout=PIPE)
        except FileNotFoundError:
            print(cls.name() + ': DUB functionality not available, application \"' + app_path + '\" not found.')
            return []
        else:
            return instance.communicate()[0].decode('utf-8')
