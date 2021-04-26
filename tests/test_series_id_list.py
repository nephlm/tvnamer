import io

from tvnamer.main import _populate_series_id_list
from tvnamer.config import Config

from functional_runner import run_tvnamer, verify_out_data
from helpers import attr

def test_populate_series_id_list():
    Config["series_id_list"] = None
    Config["series_file"] = "something"

    content_string = "76156|Scrubs\n75397\n\n|Getting harder\n923|After the hard one\n"
    contents = io.StringIO(content_string)
    _populate_series_id_list(contents)
    assert Config['series_id_list'] == [76156, 75397, 923]


@attr("functional")
def test_series_id_list_filter():
    """Test most simple usage
    """

    conf = """
    {
        "series_id_list": [367138, 72073]
    }
    """

    out_data = run_tvnamer(
        with_files = ['star.trek.s01e01.avi'],
        with_config = conf,
        with_input = "1\ny\n")

    expected_files = ['Star Trek: Deep Space Nine - [01x01] - Emissary (1).avi']

    verify_out_data(out_data, expected_files)

@attr("functional")
def test_series_id_list_filter_select_first():
    """Test most simple usage
    """

    conf = """
    {
        "series_id_list": [367138, 72073],
        "select_first": true,
        "always_rename": true
    }
    """

    out_data = run_tvnamer(
        with_files = ['star.trek.s01e01.avi'],
        with_config = conf)

    expected_files = ['Star Trek: Deep Space Nine - [01x01] - Emissary (1).avi']

    verify_out_data(out_data, expected_files)

