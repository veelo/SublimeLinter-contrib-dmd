param(
  [switch]$Run,
  [switch]$Clean,

  [string]$OutDir = [System.IO.Path]::Combine($PSScriptRoot, "_build")
)

$ErrorActionPreference = "Stop"
cd $PSScriptRoot

if($Clean)
{
  $ToClean = ls -File $OutDir
  if($ToClean)
  {
    Write-Host "Removing:"
    $ToClean | % { Write-Host "  $_" }
    rm -Force $ToClean
  }
}
else
{
  foreach($SourceFile in ls $PSScriptRoot -File -Filter '*.d')
  {
    $SourceLines = Get-Content $SourceFile
    $CommandLine = $SourceLines[0].TrimStart('/').Trim()
    if($CommandLine.StartsWith("dmd"))
    {
      $OutFilePath = [System.IO.Path]::Combine($OutDir, [System.IO.Path]::ChangeExtension($SourceFile.Name, ".exe"))
      $Expression = "$CommandLine `"$SourceFile`" `"-of=$OutFilePath`""
      Write-Host "Compiling: $Expression"
      Invoke-Expression $Expression
      
      if($? -and $Run)
      {
        Write-Host "Running: $OutFilePath"
        & $OutFilePath
      }
    }
  }
}
