#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from packaging.version import Version

x1 = "1.2.3-pre"
x2 = "1.2.4"

v1 = Version(x1)
parsed1 = v1.release
if v1.pre:				### this is important too
	parsed1 += v1.pre

v2 = Version(x2)
parsed2 = v2.release
if v2.pre:				### this is important too
	parsed2 += v2.pre

# this returns correct results
print(f"x1='{x1}' x2='{x2}' v1='{v1}' v2='{v2}'\n")
print(f"Version: {v1} == {v2} = '{v1 == v2}'")
print(f"Version: {v1} <= {v2} = '{v1 <= v2}'")
print(f"Version: {v1} <  {v2} = '{v1 < v2}'")
print(f"Version: {v1} >= {v2} = '{v1 >= v2}'")
print(f"Version: {v1} >  {v2} = '{v1 > v2}'")

# this returns INCORRECT results
print(f"\n")
print(f"parsed1='{parsed1}' parsed2='{parsed2}'\n")
print(f"parsed: {parsed1} == {parsed2} = '{parsed1 == parsed2}'")
print(f"parsed: {parsed1} <  {parsed2} = '{parsed1 < parsed2}'")
print(f"parsed: {parsed1} <= {parsed2} = '{parsed1 <= parsed2}'")
print(f"parsed: {parsed1} >  {parsed2} = '{parsed1 > parsed2}'")
print(f"parsed: {parsed1} >= {parsed2} = '{parsed1 >= parsed2}'")
