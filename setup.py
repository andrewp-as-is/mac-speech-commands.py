import setuptools

setuptools.setup(
    name='mac-speech-commands',
    version='2020.12.3',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
