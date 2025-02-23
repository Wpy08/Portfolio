# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['9X9_main_Windows_FL.py'],
    pathex=[],
    binaries=[],
    datas=[('images/*', 'images')],
    hiddenimports=['mm_9X9_third_CH_FL', 'mm_9X9_third_zy_FL', 'mm_random_shuffle_CH_second_FL', 'mm_random_shuffle_zy_FL', 'mm_saying_random_CH_FL'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='9X9_main_Windows_FL',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['image.ico'],
)
