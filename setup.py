from setuptools import setup, find_packages

setup(name='macCC',
      version='0.0.3',
      author="cijianzy",
      author_email="cijianzy@gmail.com",
      url="http://cijianzy.com",
      #packages=find_packages(),
      packages=['macCC'],
      #package_data={'setuptools_app': ['contents/hello']},
      # scripts=['bin/say_hello'],
      description=("A tool to capture Mac clipboard image"),
      long_description=open('README.md').read(),
      install_requires=['Pillow'],
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: MIT License",
          "Development Status :: 3 - Alpha"
          ]
      )
