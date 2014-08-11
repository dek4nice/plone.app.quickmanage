from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='prime.app.global',
      version=version,
      description="Global Prime Views",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='zope view',
      author='Dek4nice',
      author_email='admin911@list.ru',
      url='https://bitbucket.org/studio-web/prime.app.global',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['prime', 'prime.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
