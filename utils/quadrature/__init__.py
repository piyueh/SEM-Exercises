#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Pi-Yueh Chuang <pychuang@gwu.edu>
#
# Distributed under terms of the MIT license.

"""__init__.py for quadrature subpackage"""

from utils.quadrature.GaussJacobi import GaussJacobi
from utils.quadrature.GaussRadauJacobi import GaussRadauJacobi
from utils.quadrature.GaussLobattoJacobi import GaussLobattoJacobi

__version__ = "alpha"
__author__ = "Pi-Yueh Chuang"
