from distutils.core import setup

setup (
    name = "autoscaling",
    version = "0.0.10",
    description = "Cog commands for AWS autoscaling",
    author = "Charles Martinot",
    author_email = "charles.martinot@honestbee.com",
    url = "https://github.com/honestbee/cog-autoscaling",
    packages = ["autoscaling", "autoscaling.commands"],
    requires = ["pycog3 (>=0.1.25)", "boto3 (==1.4.0)"],
    keywords = ["cog", "aws", "autoscaling", "bot", "devops", "chatops", "automation"],
    classifiers = [
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
