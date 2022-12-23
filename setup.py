import setuptools

setuptools.setup(
    name="notion_ultimate_brain",
    version="0.0.1",
    url="https://github.com/Jchang4/notion_ultimate_brain.git",
    author="Justin Chang",
    author_email="",
    description="",
    python_requires=">=3.10",
    install_requires=["notion_client"],
    extras_require={"dev": ["pytest", "pytest", "pytest-cov", "pytest-mock"]},
    packages=setuptools.find_packages(),
)
