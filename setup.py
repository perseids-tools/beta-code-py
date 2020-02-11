import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="beta_code",
  version="0.0.5",
  author="perseids",
  author_email="perseids@tufts.edu",
  description="Converts Greek beta code to Greek characters and vice versa",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/perseids-tools/beta-code-py",
  packages=setuptools.find_packages(),
  include_package_data=True,
  classifiers=(
    "Programming Language :: Python",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ),
)
