from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Sarvesh Gadgil",
      author_email="sarvesh.gadgil@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
        'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
        }
      )