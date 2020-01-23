import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfToImg",  # Replace with your own username
    version="0.0.1",
    author="starkblaze01",
    author_email="mp.pathela@gmail.com",
    description="Easily convert PDF to Image from command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/starkblaze01/Pdf-To-Image",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.6',
)
