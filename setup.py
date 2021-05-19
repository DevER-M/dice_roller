from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='random_dice_roller',
  version='0.0.2',
  description="A very 'easy to use' random dice roller" ,
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/DevER-M/dice_roller',  
  author='Dever',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='Random dice roller', 
  packages=find_packages(),
  install_requires=['']
) 