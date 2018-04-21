# Limitations

This directory contains some files displaying some known limitations of this plugin.

You can open any of the *.d files and observe errors being reported by the plugin. To compile the *.d files without errors, either use build.py, or do it manually with dmd. See the following subsections for details.

## Build (python)
You need `dmd` in your path to use the build script `build.py`. This script can be used to build all samples so you see for yourself that they're valid D programs.

* `build.py` Build all samples without running them. Default output directory is `./_build`.
* `build.py -Run` Build and run all samples in turn.
* `build.py -Clean` Remove build output instead of building.

They have been tested with dmd v2.077.1.

## Build (manually)
Each sample contains the necessary arguments to properly build them in their first line as a comment.
