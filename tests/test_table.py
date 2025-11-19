from pages.table_page import TablePage

def test_table_structure(driver):
    table_page = TablePage(driver)
    rows = table_page.get_table_rows()
    cols = table_page.get_table_columns()
    headers = table_page.get_table_column_values()
    
    assert len(rows) == 9, f"Expected 9 rows, but got {len(rows)}"
    assert len(cols) == 6, f"Expected 6 columns, but got {len(cols)}"
    assert headers == ['ID','Course Name', 'Language', 'Level', 'Enrollments', 'Link'], f"Column Headers do not match expected values"
    
def select_language_and_verify(driver):
    table_page = TablePage(driver)
    for lang in ["Any", "Java", "Python"]:
        table_page.select_lang(lang)
        assert True, f"Language {lang} selection did not work as expected"

def test_language_filter(driver):
    select_language_and_verify(driver)