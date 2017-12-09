# Limitations

This directory contains some files displaying some known limitations of this plugin.

Each sample contains in its first line the `dmd` commandline used to build the sample.

## Build
You can use `build.ps` to build all samples and see for yourself that they're valid D programs.

* `build.ps1` Build all samples without running them. Output directory is `./_build`.
* `build.ps1 -Run` Build and run all samples in turn.
* `build.ps1 -Clean` Remove build output instead of building.

They have been tested with dmd v2.077.1.
