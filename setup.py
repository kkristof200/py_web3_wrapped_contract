import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        long_description = f.read()
else:
    long_description = 'web3_wrapped_contract'

setuptools.setup(
    name='web3_wrapped_contract',
    version='0.0.16',
    author='Kristóf-Attila Kovács',
    description='web3_wrapped_contract',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kkristof200/py_web3_wrapped_contract',
    packages=setuptools.find_packages(),
    install_requires=[
        'eth-account>=0.5.6',
        'setuptools>=59.6.0',
        'web3>=5.25.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
)