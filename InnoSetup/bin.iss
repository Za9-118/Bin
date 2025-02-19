; -- PROGRESSBAR BIN --
; Demonstrates copying 3 files and creating an icon.

[Setup]
AppName=Bin
AppVersion=1.1.0
WizardStyle=classic
DefaultDirName={autopf}\Progressbar Corp\Bin
DefaultGroupName=Progressbar Corp
UninstallDisplayIcon={app}\Bin.exe
VersionInfoCompany=Progressbar Corporation
VersionInfoCopyright=Copyright (c) 2001 Progressbar Corporation. All wrongs reserved.
VersionInfoDescription=Progressbar Recycle Bin
VersionInfoVersion=1.1.0
VersionInfoOriginalFileName=Bin.exe
VersionInfoProductName=Bin
VersionInfoProductTextVersion=Hotfix 1
VersionInfoProductVersion=1.1.0
VersionInfoTextVersion=1.1.0
PrivilegesRequired=admin
Compression=lzma2
InfoBeforeFile=data/readme.txt
SolidCompression=yes
WizardImageFile=media/Header.bmp
WizardSmallImageFile=media/Icon.bmp
AllowCancelDuringInstall=yes
AppVerName=Bin v1.1
AppId=Progressbar.RecyclePet
AppComments=Progressbar Bin
OutputDir=dist
OutputBaseFilename=Bin Setup v1.1

[Files]
Source: "data/Executable/Bin.exe"; DestDir: "{app}"
Source: "data/Executable/bindialog.py"; DestDir: "{app}"
Source: "data/Readme.txt"; DestDir: "{app}"; Flags: isreadme
Source: "data/data.json"; DestDir: "{app}"
Source: "data/Executable/utilities/*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs
Source: "data/Executable/media/*"; DestDir: "{app}\png"; Flags: recursesubdirs createallsubdirs
Source: "data/Executable/_internal/*"; DestDir: "{app}\_internal"; Flags: recursesubdirs createallsubdirs

[Dirs]
Name: "{app}\png"
Name: "{app}\utilities"
Name: "{app}"; Permissions: everyone-modify

[Icons]
Name: "{group}\Bin"; Filename: "{app}\Bin.exe"
Name: "{userdesktop}\Bin"; Filename: "{app}\Bin.exe"
Name: "{userstartup}\BinServiceIcon"; Filename: "{app}\BinServiceIcon.exe"; Tasks: installServiceIcon

[Tasks]
Name: "installServiceIcon"; Description: "Enable background utility to update desktop icon"; GroupDescription: "Additional Options"; Flags: unchecked
Name: "runBin"; Description: "Run Bin after installation"; GroupDescription: "Post-install Options"; Flags: unchecked

[Run]
Filename: "{app}\Bin.exe"; Parameters: ""; StatusMsg: "Launching Bin..."; Flags: nowait postinstall; Tasks: runBin

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
Type: files; Name: "{userstartup}\BinServiceIcon.lnk"
