from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='iskra.audiofile',
      version=version,
      description="Audio Dexterity mediaelementjs player",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='audio dexterity plone mediaelementjs',
      author='Iskra Desenvolupament SCCL',
      author_email='info@iskra.cat',
      url='https://github.com/iskracat/Hitotsubashi-University/tree/master/buildout/src/iskra.audiofile',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['iskra'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.app.dexterity',
          'plone.namedfile',
          'plone.app.multilingual',
          'plone.multilingualbehavior',
          'hachoir_parser',
          'hachoir_metadata'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
