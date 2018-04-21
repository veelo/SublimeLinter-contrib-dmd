// dmd "-J=."

mixin(import("mixin_import.txt"));

void main()
{
  mixin_import_func();
}
