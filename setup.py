import os
from setuptools_scm.version import get_local_node_and_date
from setuptools import setup, find_packages

LONG_DESC="""
This package implements a basic girder worker task plugin and is
intended as a non-trivial example.

It implements a single task that performs principal component analysis
on a CSV with two components.  The task returns a dictionary with the
explained variance of each component and a path to a figure that plots
the data.  """

def prerelease_local_scheme(version):
    if 'CIRCLE_BRANCH' in os.environ and \
       os.environ['CIRCLE_BRANCH'] == 'master':
        return ''
    else:
        return get_local_node_and_date(version)

setup(name='gwpca',
      use_scm_version={'local_scheme': prerelease_local_scheme},
      description='An example girder worker extension',
      long_description=LONG_DESC,
      author='Chris Kotfila',
      author_email='chris.kotfila@kitware.com',
      license='Apache v2',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Topic :: Scientific/Engineering',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python'
      ],

      setup_requires=[
          'setuptools_scm'
      ],
      install_requires=[
          "girder_worker",
          "girder_worker_utils"
      ],
      extras_require={
          "girder": [
              "girder"
          ],
          "worker": [
              "sklearn",
              "pandas",
              "scipy",
              "matplotlib"
          ]
      },
      include_package_data=True,
      entry_points={
          'girder_worker_plugins': [
              'gwpca = gwpca:GWPCAPlugin',
          ]
      },
      packages=find_packages(),
      zip_safe=False)
