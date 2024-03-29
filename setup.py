from distutils.core import setup
setup(
  name = 'gs_utility',         # How you named your package folder (MyLib)
  packages = ['gs_utility'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Useful for manipulating data on google spreadsheet',   # Give a short description about your library
  author = 'Bihari Lal Pandey',                   # Type in your name
  author_email = 'biharilalpandey1@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/codebat/gs_utility',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/codebat/gs_utility/archive/0.5.tar.gz',    # I explain this later on
  keywords = ['google', 'spreadsheet'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'apiclient',
	  'oauth2client',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
  ],
)
