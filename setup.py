from setuptools import setup, find_packages

__name__ = "rabbit-shell"
__version__ = "2.0"
__author__ = "greed albadi"
__author_email__ = "greedalbadi@gmail.com"


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
f.close()
print(find_packages())
setup(
    name=__name__,
    version=__version__,
    description='Rabbit shell reverse shell tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/greedalbadi/rabbit-shell',
    author=__author__,
    author_email=__author_email__,

    project_urls={
      'Source': 'https://github.com/greedalbadi/rabbit-shell',
    },
    include_package_data=True,
    license='MIT',

    keywords=[
        "python",
        "shell",
        "networking",
        "server", "reverse-shell", "tool", "hacking",
        "cyber"
       ],
    packages=find_packages(),
    entry_points={
                        'console_scripts': [
                                'rsb=rabbit_shell.__main__:main',
                        ]
                }
)