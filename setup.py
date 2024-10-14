from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

setup(
    name="truck_agent",
    version="1.0.0",
    author="WALTER GROUP",
    author_email="",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url="https://www.waltergroup.com",
    license="LICENSE",
    description="Python truck agent for WALTER GROUP Hackathon: Sustainable Logistics",
    long_description=(this_directory / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    python_requires=">=3.10, <4",
    install_requires=["fastapi", "uvicorn", "request", "httpx", "pytest-runner", "pytest"],
    entry_points={
        "console_scripts": ["run=truck_agent.main:main"],
    },
    zip_safe=False,
    include_package_data=True,
)
