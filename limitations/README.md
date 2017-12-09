# Limitations

This directory contains some files displaying some known limitations of this plugin.

Each sample contains in its first line the `dmd` commandline used to build the sample.

## Build (Powershell)
You can use `build.ps` to build all samples and see for yourself that they're valid D programs.

* `build.ps1` Build all samples without running them. Output directory is `./_build`.
* `build.ps1 -Run` Build and run all samples in turn.
* `build.ps1 -Clean` Remove build output instead of building.

They have been tested with dmd v2.077.1.

## Build (manually)
As mentioned earlier, each sample contains the necessary arguments to build them in their first line. Just make sure to `cd` into this directory and to also pass the name of the file you wish to compile.
