# bryde.utils
# Utilities for the NLTK Tutorial/Bryde module.
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Sat May 28 21:43:21 2016 -0700
#
# Copyright (C) 2016 District Data Labs
# For license information, see LICENSE.txt
#
# ID: utils.py [] benjamin@bengfort.com $

"""
Utilities for the NLTK/Bryde module.
"""

##########################################################################
## Imports
##########################################################################

import time

from functools import wraps


def timeit(func):
    """
    Returns the number of seconds that a function took along with the result
    """

    @wraps(func)
    def timer_wrapper(*args, **kwargs):
        """
        Inner function that uses the Timer context object
        """
        start  = time.time()
        result = func(*args, **kwargs)

        return result, time.time() - start

    return timer_wrapper
