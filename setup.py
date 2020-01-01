from setuptools import setup

setup(
    name='roblox.py',
    author='Accutrix',
    url='https://github.com/accutrix/roblox.py',
    project_urls={
        "Documentation": "https://discordpy.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/Rapptz/discord.py/issues",
    },
    version=version,
    packages=[],
    license='MIT',
    description='A python wrapper for the ROBLOX API',
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3.5.3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
