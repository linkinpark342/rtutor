try:
    from distribute_setup import use_setuptools
except ImportError:
    pass
else:
    use_setuptools()

from setuptools import setup, find_packages

setup(name="rtutor",
        packages=find_packages(),
        install_requires=[
            'django',
            'django_cas',
        ],
        extras_require={
            'FastCGI': ['flup'],
        },
        test_suite='rtutor.runtests.runtests',
)

