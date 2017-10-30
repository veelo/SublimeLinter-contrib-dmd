#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Bastiaan N. Veelo
# Copyright (c) 2017 Bastiaan N. Veelo
#
# License: MIT
#

"""This module exports the Dmd plugin class."""

from SublimeLinter.lint import Linter, util


class Dmd(Linter):
    """Provides an interface to dmd, the reference D compiler from dlang.org."""

    syntax = 'd'
    cmd = ('dmd', '-o-', '-w', '-wi', '-vcolumns', '*')
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 2.076.1'
    regex = (
        # Temporary source file (ignored) followed by "(row,col): "
        r'^.+SublimeLinter3.+[(](?P<line>\d+)([,](?P<col>\d+))?[)]: '
        # Either "Error: ", "Warning: " or "Deprecation: "
        r'(?:(?P<error>Error)|(?P<warning>Warning|Deprecation)): '
        # Single-row message
        r'(?P<message>.+)\r?\n'
        # Ignored rows (without the path to the temp source file)
        r'((.(?!SublimeLinter3))+\r?\n)*'
    )
    multiline = True
    tempfile_suffix = 'd'
    line_col_base = (1, 1)
    error_stream = util.STREAM_STDERR
