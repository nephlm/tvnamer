import logging
import sys
from typing import List

from tvdb_api import BaseUI, ConsoleUI, tvdb_userabort

from .config import Config


def filter_function(show):
    return show['id'] in Config["series_id_list"]

def series_filter(allSeries:List[dict]):
    return [show for show in allSeries if filter_function(show)]

class TVNamerFilteredBaseUI(BaseUI):

    def selectSeries(self, allSeries:List[dict]):
        allSeries = series_filter(allSeries)
        return super().selectSeries(allSeries)

class TVNamerFilteredConsoleUI(ConsoleUI):

    def selectSeries(self, allSeries:List[dict]):
        allSeries = series_filter(allSeries)
        return super().selectSeries(allSeries)
