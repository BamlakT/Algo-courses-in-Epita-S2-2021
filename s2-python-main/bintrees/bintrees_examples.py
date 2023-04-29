# -*- coding: utf-8 -*-
"""
BinTree: examples
"""

from algopy import bintree
from algopy.bintree import BinTree


B_tuto = BinTree(5, 
              BinTree(2, 
                    BinTree(-1, BinTree(4, None, None), None), 
                    BinTree(0, None, BinTree(11, None, None))),
              BinTree(12, 
                    BinTree(4, None, None), 
                    BinTree(1, BinTree(-2, None, BinTree(15, None, None)), None)))
                
B_quid = BinTree('V', 
                BinTree('D', 
                   BinTree('I', 
                      BinTree('Q', None, BinTree('U', None, None)),
                      None),
                   BinTree('S', 
                      BinTree('E', None, None),
                      BinTree('T', None, None))),
                BinTree('I', 
                   BinTree('E', 
                      None,
                      BinTree('R', None, None)),
                  BinTree('A', 
                      BinTree('T', None, None),
                      BinTree('S', None, None))))    
