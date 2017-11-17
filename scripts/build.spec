# -*- mode: python -*-

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
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)
exe = EXE(pyz,
        a.scripts,
        exclude_binaries=True,
        name='Nautiljon Notifier',
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
