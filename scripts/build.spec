# -*- mode: python -*-

from PyInstaller.compat import is_linux

block_cipher = None

a = Analysis(['../app/app.py'],
            pathex=['C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Enterprise\\Common7\\IDE\\Remote Debugger\\x64', 'C:\\Users\\Nokito\\Documents\\Nautiljon Notifier PythonQT'],
            binaries=[],
            datas=[('../app/assets/*', 'assets')],
            hiddenimports=[],
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher)

excludedBinaries = [
  'Qt5Network',
  'Qt5Svg'
]

def excludeBinary(binary):
  for excludedBinary in excludedBinaries:
    if excludedBinary in binary:
      return True

  return False

a.binaries = [binary for binary in a.binaries if not excludeBinary(binary[0])]

pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)

if is_linux:
  exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='nautiljon_notifier_linux',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='app/assets/nautiljon_icon.ico')
else:
  exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='nautiljon_notifier',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='app/assets/nautiljon_icon.ico')
  coll = COLLECT(exe,
                 a.binaries,
                 a.zipfiles,
                 a.datas,
                 strip=False,
                 upx=True,
                 name='app')
