from tvdb_api import BaseUI, tvdb_userabort

SERIES_DATA_PATH = "/series_list.txt"


class AutoUI(BaseUI):
    def __init__(self, config, log=None):
        super().__init__(config, log)
        self.series_dict = {}
        self._populate_series_dict()

    def _populate_series_dict(self):
        with open(SERIES_DATA_PATH, "r") as fp:
            for line in fp:
                (sid, title) = line.split("|", 1)
                self.series_dict[int(sid)] = title

    def selectSeries(self, allSeries):
        for series_dict in allSeries:
            print(
                f'Series selected: {series_dict["seriesName"]}  ({series_dict["id"]})'
            )
            if series_dict["id"] in self.series_dict:
                return series_dict
        raise tvdb_userabort
