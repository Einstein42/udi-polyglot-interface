from distutils.core import setup
#from setuptools import setup

setup(name='lifxlan',
      version='1.0.0',
      description='UDI Polyglot v2 Interface',
      url='http://github.com/mclarkk/lifxlan',
      author='James Milne',
      author_email='milne.james@gmail.com',
      license='MIT',
      packages=['polyinterface'],
      install_requires=[
        "bitstring",
	"paho-mqtt",
	"python-dotenv",
        ],
      zip_safe=False,
          # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ])
