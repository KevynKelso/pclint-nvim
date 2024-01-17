from static_analysis import parse_csv

def test_parse_csv_00():
    results = parse_csv('./test.csv')
    assert len(results) > 0
    assert 'file' in results[0].keys()
    assert 'line' in results[0].keys()
    assert 'message' in results[0].keys()

