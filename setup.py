#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decimer",
    version="2.0.1",
    author="Kohulan Rajan",
    author_email="kohulan.rajan@uni-jena.de",
    maintainer="Kohulan Rajan",
    maintainer_email="kohulan.rajan@uni-jena.de",
    description="DECIMER 2.0: Deep Learning for Chemical Image Recognition using Efficient-Net V2 + Transformer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kohulan/DECIMER-Image_Transformer",
    packages=setuptools.find_packages(),
    license="MIT",
    install_requires=[
        "tensorflow>=2.6.3",
        "opencv-python",
        "pystow",
        "efficientnet",
    ],
    package_data={"DECIMER": ["repack/*.*","automl/*.*", "automl/efficientnetv2/*.*", "Utils/*.*"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
