from setuptools import setup

setup(name='cook4ml',
      version='0.1',
      description='Cook for Machine Learning: a helper package to easily create dataset for machine learning',
      url='http://github.com/woozzu/cook4ml',
      author='Seonghyeon Nam',
      author_email='woozzu@gmail.com',
      license='MIT',
      packages=['cook4ml'],
      install_requires=['numpy'],
      extras_require=[
          'h5py',
          'lmdb'
      ],
      zip_safe=False)
