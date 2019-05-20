#!/usr/bin/env python

from mp import version
from distutils.core import setup

setup(name='mpfshell-lite',
      version=version.FULL,
      description='The lightweight version of the mpfshell is for pure CUI drivers.',
      author='Stefan Wendler & Juwan',
      author_email='junhuanchen@qq.com',
      url='https://github.com/junhuanchen/mpfshell-lite',
      download_url='https://codeload.github.com/junhuanchen/mpfshell-lite/zip/master',
      install_requires=['pyserial', 'websocket_client'],
      packages=['mp'],
      scripts=['mpfs'],
      keywords=['micropython', 'shell', 'file transfer', 'development'],
      classifiers=[],
      entry_points={"console_scripts": ["mpfs=mp.mpfshell:main"]},
)
