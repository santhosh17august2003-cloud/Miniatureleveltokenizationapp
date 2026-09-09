# PowerShell script to create Desktop Shortcut with custom icon
$WScriptShell = New-Object -ComObject WScript.Shell
$DesktopPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Desktop)
$ProjectDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$MainPy = Join-Path $ProjectDir "main.py"
$IconPath = Join-Path $ProjectDir "assets\app_icon.ico"

# Locate pythonw.exe or python.exe
$PythonW = (Get-Command pythonw.exe -ErrorAction SilentlyContinue).Source
if (-not $PythonW) {
    $PythonW = (Get-Command python.exe -ErrorAction SilentlyContinue).Source
}

Write-Host "Project Directory: $ProjectDir"
Write-Host "Python Executable: $PythonW"
Write-Host "Icon Path: $IconPath"
Write-Host "Desktop Path: $DesktopPath"

# 1. Create shortcut on Desktop
$DesktopShortcutPath = Join-Path $DesktopPath "Miniature Tokenization App.lnk"
$Shortcut = $WScriptShell.CreateShortcut($DesktopShortcutPath)
$Shortcut.TargetPath = $PythonW
$Shortcut.Arguments = "`"$MainPy`""
$Shortcut.WorkingDirectory = $ProjectDir
$Shortcut.IconLocation = "$IconPath,0"
$Shortcut.Description = "Miniature NLP Tokenization Desktop App"
$Shortcut.Save()
Write-Host "Created Desktop shortcut at: $DesktopShortcutPath"

# 2. Create shortcut in project folder as well
$LocalShortcutPath = Join-Path $ProjectDir "Miniature Tokenization App.lnk"
$LocalShortcut = $WScriptShell.CreateShortcut($LocalShortcutPath)
$LocalShortcut.TargetPath = $PythonW
$LocalShortcut.Arguments = "`"$MainPy`""
$LocalShortcut.WorkingDirectory = $ProjectDir
$LocalShortcut.IconLocation = "$IconPath,0"
$LocalShortcut.Description = "Miniature NLP Tokenization Desktop App"
$LocalShortcut.Save()
Write-Host "Created Local shortcut at: $LocalShortcutPath"
