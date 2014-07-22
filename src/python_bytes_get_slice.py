#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2014

@author: anroco

How to get a slice of a bytes object in Python?

¿Cómo obtener una sección de un objeto bytes en Python?
'''

#create a bytes object
b = b'bytes data in Python'
print(b)

#b[start:stop] the start index is inclusive and the end index is exclusive.
b_new = b[6:10]
print(b_new)

#if the start index isn't defined, is taken from the beginning.
b_new = b[-6:]
print(b_new)

#if the end index isn't defined, is taken until the end
b_new = b[:5]
print(b_new)

#if neither is defined, returns the full bytes object
b_new = b[:]
print(b_new)
