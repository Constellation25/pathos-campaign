from setuptools import setup, find_packages
setup(
    name="pathos-ai",
    version="1.0.0",
    author="CyGeL Co - DBA KRE8TIVE KONCEPTZ",
    description="PaTHos: The AI Pathway. Cygnus: Us. Geek the Greek.",
    packages=find_packages(),
    install_requires=["click", "rich", "questionary"],
    entry_points={
        "console_scripts": [
            "pathos=pathos_ai.cli:pathos"
        ]
    },
)
