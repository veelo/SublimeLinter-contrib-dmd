"""
Builds and optionally runs all limitation samples.
"""

import sys, os, glob, subprocess, shutil, argparse
from glob import glob

IS_WINDOWS = os.name == 'nt'

def main(run, clean, code_dir, build_dir):
    """Main entry point to build and optionally run all samples."""
    os.chdir(code_dir)
    if clean:
        if os.path.exists(build_dir):
            print("Removing directory:", build_dir)
            shutil.rmtree(build_dir)
        else:
            print("Nothing to clean")
    else:
        sources = glob('{}/*.d'.format(code_dir))
        for source_path in sources:
            with open(source_path) as source_file:
                first_line = source_file.readline()

            command = first_line.lstrip('/').strip()

            if not command.startswith("dmd"):
                print("Skipping:", source_path)
                continue

            # Add the path to the source file.
            command += ' "' + source_path + '"'

            # Determine the output file name so we can invoke it later.
            source_name = os.path.basename(os.path.splitext(source_path)[0])
            executable_path = os.path.join(build_dir, source_name)
            if IS_WINDOWS:
                executable_path += '.exe'

            command += ' "-of={}"'.format(executable_path)

            print("Compiling:", command)
            subprocess.call(command, shell=True)

            if run:
                print("Running:", os.path.basename(source_path))
                subprocess.call(executable_path)
                print()

if __name__ == '__main__':
    file_dir = os.path.dirname(__file__) #os.path.dirname()
    code_dir = file_dir
    default_build_dir = os.path.join(file_dir, '_build')

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--run',   action='store_true', default=True,
                        help='run all built examples.')
    parser.add_argument('--clean', action='store_true', default=False,
                        help='instead of building/running, remove the build dir')
    parser.add_argument('--build-dir', default=default_build_dir,
                        help='output directory for build results. ' + \
                        'Note: working directory during build is: ' + os.path.abspath(code_dir))
    args = parser.parse_args()

    main(args.run, args.clean, code_dir, args.build_dir)
