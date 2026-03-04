from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ghostbyte",
    version="1.0.0",
    author="frankSx",
    author_email="fixes.it.frank@googlesmail.com",
    description="Unicode Exploit & ASCII Obfuscation Toolkit for Adversarial ML Testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frankSx/ghostbyte",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'ghostbyte=src.__init__:main',
        ],
    },
    keywords="unicode security adversarial-ml homoglyph obfuscation ghostbyte",
    project_urls={
        "Bug Reports": "https://github.com/frankSx/ghostbyte/issues",
        "Source": "https://github.com/frankSx/ghostbyte",
        "Blog": "https://frankhacks.blogspot.com",
    },
)
