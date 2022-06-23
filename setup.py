import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='console_interface',  
     version='0.1',
     scripts=['console_interface.py'] ,
     author="Luís Fernando Oliveira Caldeira",
     author_email="luisfcaldeira@gmail.com",
     description="A tool for interact with user in the console.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/luisfcaldeira/console_interface",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )