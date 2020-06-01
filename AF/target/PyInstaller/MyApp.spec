# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/magnu/Documents/QT/AF/src/main/python/main.py'],
             pathex=['/home/magnu/Documents/QT/AF/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/home/magnu/.local/lib/python3.8/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/home/magnu/Documents/QT/AF/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='MyApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='MyApp')
