#!/usr/bin/env python

"""Functional tests for tvnamer tests
"""

import os
from functional_runner import run_tvnamer, verify_out_data
from helpers import attr
import pytest


@attr("functional")
def test_simple_single_file():
    """Test most simple usage
    """

    conf = """
    {
    "filename_with_episode":
        "%(seriesname)s - [%(seasonnumber)02dx%(episode)s] - %(first_aired)s - %(episodename)s%(ext)s"
    }
    """

    out_data = run_tvnamer(
        with_files = ['scrubs.s01e01.avi'],
        with_config = conf,
        with_input = "1\ny\n")

    expected_files = ['Scrubs - [01x01] - 2001-10-02 - My First Day.avi']

    verify_out_data(out_data, expected_files)

