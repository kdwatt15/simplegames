import setuptools

with open("README.md", "r") as f:
	long_description = f.read()
	f.close
	
with open("requirements.txt", "r") as f:
	install_requires = f.readlines()
	f.close
	
setuptools.setup(
	name="simplegames",
	version="0.1.0",
	author="Kevin Watt",
	author_email="kdwatt15@gmail.com",
	description="Package for simple game engines and associated AIs",
	long_description=long_description,
	long_description_content_type="test/markdown",
	packages=setuptools.find_packages(include=["simplegames"]),
	package_dir={'': 'lib'},
	install_requires=install_requires,
	license="MIT",
	python_requires=">=3.5"
)
