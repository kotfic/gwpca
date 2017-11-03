from setuptools import setup, find_packages

LONG_DESC="""
This package implements a basic girder worker task plugin and is
intended as a non-trivial example.

It implements a single task that performs principal component analysis
on a CSV with two components.  The task returns a dictionary with the
explained variance of each component and a path to a figure that plots
the data.  """

setup(name='gwpca',
      version='0.1.1',
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
      install_requires = [
          "girder_worker",
          "girder_worker_utils"
      ],
      dependency_links=[
          "git+https://github.com/girder/girder_worker_utils/tarball/master#egg=girder_worker_utils-0.6.0"
      ],
      extras_require={
          "worker": [
              "sklearn",
              "pandas",
              "scipy",
              "matplotlib"
          ]
      },
      entry_points={
          'girder_worker_plugins': [
              'gwpca = gwpca:GWPCAPlugin',
          ]
      },
      packages=find_packages(),
      zip_safe=False)
