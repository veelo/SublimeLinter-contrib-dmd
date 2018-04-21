// dmd -version=Foo

version(Foo)
{
  import std.stdio;
}

void func1() {
  /// `writeln` is not defined, perhaps `std.stdio;` is needed?
  writeln("func1");
}

void main()
{
  func1();
}
