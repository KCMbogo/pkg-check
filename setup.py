from setuptools import setup

setup(
    name="pkg-check",
    version="0.1",
    py_modules=["pkg_check"],
    author="Kadilana Mbogo",
    author_email="kadilanambogo@gmail.com",
    entry_points={
        "console_scripts": [
            "pkg-check = pkg_check:main",
        ]
    }
)