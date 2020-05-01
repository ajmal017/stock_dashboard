from setuptools import setup, find_packages

requires = [
    'TA-Lib',
    'matplotlib',
    'mplfinance',
    'pandas',
    'numpy',
    'requests',
    'requests_oauthlib',


]

setup(
    name='stock_dashboard',
    version='',
    packages=find_packages(),
    keywords='python stock candlestick matplotlib pandas Ally',
    url='',
    license='',
    author='Tom Hildebrand',
    author_email='t1manster@gmail.com',
    description='Stock Dashboard to connect to an Ally account for retrieving information about stocks.',
    install_requires=requires
)
