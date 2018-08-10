# -*- mode: python -*-

block_cipher = None


a = Analysis(['Pyinstaller_learn.py'],
             pathex=['/Users/kuyou1/Documents/mine/demo/Python/py3/pyinstaller'],
             binaries=[],
             datas=[('/Users/kuyou1/Documents/mine/demo/Python/py3/pyinstaller/res','')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Pyinstaller_learn',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
