from setuptools import setup
setup(
    name = 'blackjack',
    version = '0.1.0',
    packages = ['blackjack'],
    entry_points = {
        'console_scripts': [
            'blackjack = blackjack.__main__:main'
        ]
    })
