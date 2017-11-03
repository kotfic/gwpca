from setuptools import setup, find_packages

setup(name='gwpca',
      version='0.1.0',
      description='An example girder worker extension',
      author='Chris Kotfila',
      author_email='chris.kotfila@kitware.com',
      license='Apache v2',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: Apache Software License'
          'Topic :: Scientific/Engineering :: GIS',
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
