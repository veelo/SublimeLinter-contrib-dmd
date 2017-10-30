SublimeLinter-contrib-dmd
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-dmd.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-dmd)

This linter plugin for [SublimeLinter][docs] provides an interface to [dmd](https://dlang.org), the reference compiler for the D programming language. It will be used with files that have the “D” syntax. These will be parsed by `dmd` and any errors and warnings will be shown inline and optionally as [tooltips][user-settings]. The advantages to pure syntax linters are:

1. The parser is always up-to-date.
1. Does full symbol resolution, including imports.
1. Mixins are expanded.
1. Templates are validated.
1. Deprecation warnings are included.
1. The "did you mean &hellip;" assistance appears right where it is most helpful.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `dmd` is installed on your system. To install `dmd`, go to https://dlang.org/download.html.

**Note:** This plugin was developed using `dmd` 2.076.1.

### Linter configuration
In order for `dmd` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `dmd`, you can proceed to install the SublimeLinter-contrib-dmd plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `dmd`. Among the entries you should see `SublimeLinter-contrib-dmd`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

You may pass any [arguments and switches][compile-flags] to `dmd` by configuring the `args` linter setting, like so:
```
            "dmd": {
                "@disable": false,
                "args": ["-I/my/include/dir", "-dip25"],
                "excludes": []
            }
```

<!---
In addition to the standard SublimeLinter settings, SublimeLinter-contrib-dmd provides its own settings. Those marked as “Inline Setting” or “Inline Override” may also be [used inline][inline-settings].

|Setting|Description|Inline Setting|Inline Override|
|:------|:----------|:------------:|:-------------:|
|foo|Something.|&#10003;| |
|bar|Something else.| |&#10003;|
-->

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pydocstyle linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
[user-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#user-settings
[compile-flags]: https://dlang.org/dmd-windows.html#switches
