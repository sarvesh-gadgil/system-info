from setuptools import setup

setup(name="Lab1",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Sarvesh Gadgil",
      author_email="sarvesh.gadgil@ucdconnect.ie",
      licence="GPL3",
      packages=['Lab1'],
      entry_points={
        'console_scripts':['comp30670_systeminfo=Lab1.main:main']
        }
      )