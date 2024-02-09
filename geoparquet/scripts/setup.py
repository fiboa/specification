from setuptools import setup, find_packages

setup(
    name="fiboa_parquet",
    version="0.0.1",
    install_requires=[
        "jsonschema>=4.4",
        "pyyaml>=5.1",
        "pyarrow>=7.0",
        "fsspec>=2022.3",
        "click>=8.1",
        "geopandas>=0.14.1"
    ],
    packages=find_packages(),
    package_data={
        "fiboa_parquet": ["../core/schema/schema.yml"]
    },
    entry_points={
        "console_scripts": [
            "fiboa_parquet=fiboa_parquet:main"
        ]
    }
)