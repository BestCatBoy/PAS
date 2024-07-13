; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{BD12A097-41FC-40FB-A43A-13F6FA25E0FD}
AppName=PAS
AppVersion=1.0
;AppVerName=PAS 1.0
AppPublisher=����������� ��������������� ������� ��. �.�. ��������
AppPublisherURL=https://arz.unn.ru/spo
AppSupportURL=https://arz.unn.ru/spo
AppUpdatesURL=https://arz.unn.ru/spo
DefaultDirName={pf}\PAS
DefaultGroupName=PAS
OutputDir=D:\PAS\app\setup
OutputBaseFilename=PAS.setup
SetupIconFile=D:\PAS\app\executable\img\logo.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\PAS\app\executable\run.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PAS\app\executable\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\PAS"; Filename: "{app}\run.exe"
Name: "{commondesktop}\PAS"; Filename: "{app}\run.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\run.exe"; Description: "{cm:LaunchProgram,PAS}"; Flags: nowait postinstall skipifsilent

