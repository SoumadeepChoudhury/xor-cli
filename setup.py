from setuptools import setup

setup(
    name="xor",
    version="1.0.0",
    description="XOR-ClI is a command line utility which provide the major task operations. Run help for more details.",
    author="Ahens | An Initiative to Initial",
    packages=['xor'],
    entry_points={
            'console_scripts':['xor=xor.xor:main',
                               ],
        },
)
