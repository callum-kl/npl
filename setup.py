from setuptools import setup, find_packages

_dct = {}
with open("jax/version.py") as f:
    exec(f.read(), _dct)
__version__ = _dct["__version__"]

with open("README.md") as f:
    _long_description = f.read()

setup(
    name="npl",
    version=__version__,
    description="Nonparametric Learning for Bayesian Inference",
    long_description=_long_description,
    long_description_content_type="text/markdown",
    author="Harita Dellaporta",
    packages=find_packages(exclude=["examples"]),
    python_requires=">=3.7",
    install_requires=["numpy>=1.19.5", "jax>=0.2.13" "scipy>=1.4.1" "seaborn>=0.11.2"],
    license="Apache-2.0",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
)
