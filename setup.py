from setuptools import setup

setup(
    name="study_reminders",
    version="0.1",
    description="A module for tracking a list of students, as well as managing and sending reminders for their course.",
    author="Nataniel Wlosek",
    packages=["study_reminders"],
    install_requires=["schedule", "pytz"],
    python_requires=">=3.8",
)
