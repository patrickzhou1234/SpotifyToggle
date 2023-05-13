; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

global i:=true

F6::
if (i) {
    Run, %localappdata%\Programs\Python\Python39\pythonw.exe pause.py
    i:=false
} else {
    Run, %localappdata%\Programs\Python\Python39\pythonw.exe resume.py
    i:=true
}
return