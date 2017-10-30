"""Test Mailroom app functionality."""


sample_list = [('Jenny Smith', [10000, 8000, 900])]


def test_create_report_function_runs():
    """Test that create_report() function runs by running True ."""
    from mailroom import create_report
    assert create_report()


def test_print_donor_list_function_runs():
    """Test that print_donor_list() function runs by running True ."""
    from mailroom import print_donor_list
    assert print_donor_list()


def test_print_report_function_runs():
    """Test that print_report() function runs by running True ."""
    from mailroom import print_report
    assert print_report(sample_list)


def test_update_donor_info_function_runs():
    """Test that update_donor_info() function runs by running True ."""
    from mailroom import update_donor_info
    assert update_donor_info("John Doe", '10000')
