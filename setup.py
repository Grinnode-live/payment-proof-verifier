import setuptools

setuptools.setup(
    name='python-grin-verifier',
    version='0.0.2',
    packages=['verifier',],
    license='MIT',
    description = 'An API wrapper for grinnode.live Grin payment proof verification service.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Marek Narozniak',
    author_email = '',
    install_requires=['bip_utils', 'pynacl', 'requests', 'furl'],
    url = 'https://github.com/marekyggdrasil/poketext',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
