#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Created on Sat Oct 14 13:31:08 2023
For Simulation Biology EN.605.755.81.FA23
Discovery Project

@author: Shelby Golden and Mukul Sherekar

Python version: 3.7

NOTE: a different enviroment was setup to include seaborn using conda (miniconda3)
check out how to do this/change enciroments:
https://docs.spyder-ide.org/5/faq.html#using-packages-installer

Restarting the kernel sometimes isn't enough. Closing and re-opening Spyder does
"""

Created on Oct 14
For the Simulation Biology EN.605.755.81.FA23 Discovery Projec

@author: Shelby Golden and Mukul Sherekar
@version: Python 3.7

NOTE: a different enviroment was setup to include seaborn using conda (miniconda3)
check out how to do this/change enciroments:
https://docs.spyder-ide.org/5/faq.html#using-packages-installer

Restarting the kernel sometimes isn't enough. Closing and re-opening Spyder does

Code source: https://github.com/tlubitz/SBtab/blob/master/python/README.md'
"""





The following section was intended to convert sbtab TSV files to SBML for modification.
This was a necessary workaround since modified TSV files were not able to be uploaded
    to the Paramater Balancing tool.
"""


import libsbml
    '''source: https://synonym.caltech.edu/software/libsbml/5.18.0/docs/formatted/python-api/'''

'''SBtab classes source code'''
import SBtab # <- conda install failed
    
'''Converter SBML -> SBtab'''
import sbml2sbtab


    
'''Open a file and read it'''
file_name = 'your_file.tsv'
sbtab_file = open(file_name, 'r')
file_content = sbtab_file.read()
sbtab_file.close()

  
'''Convert sbtab to sbml'''
Cd = sbtab2sbml.SBtabDocument(file_name)
(sbml, warnings) = Cd.convert_to_sbml('31')
  '''...where '31' is the SBML Level/Version 3.1'''