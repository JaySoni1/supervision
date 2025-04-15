from setuptools import setup, find_packages

setup(
    name="your_project_name",  # Replace with your actual project name
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "requests",
        "opencv-python",
        "torch",
        "seaborn",
        "pandas",
        "python-dotenv"  # For environment variable support if needed
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change license if different
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)