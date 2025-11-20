from pages.table_page import TablePage

def test_table_structure(driver):
    table_page = TablePage(driver)
    rows = table_page.get_table_rows()
    cols = table_page.get_table_columns()
    headers = table_page.get_table_column_values()
    
    assert len(rows) == 9, f"Expected 9 rows, but got {len(rows)}"
    assert len(cols) == 6, f"Expected 6 columns, but got {len(cols)}"
    assert headers == ['ID','Course Name', 'Language', 'Level', 'Enrollments', 'Link'], f"Column Headers do not match expected values"
   
def test_language_filter(driver):
    table_page = TablePage(driver)

    for lang in ["Any", "Java", "Python"]:
        table_page.select_lang(lang)
        langs = table_page.get_language_column()

        if lang == "Any":
            # Should show ALL rows
            assert len(langs) == 9, \
                f"Any filter should show all rows, but got {len(langs)}"
        else:
            # All rows must match selected filter
            visible_langs = [l for l in langs if l]
            assert all(l == lang for l in visible_langs), \
                f"Expected only {lang}, but got {visible_langs}"

def test_level_beginner(driver):
    table_page = TablePage(driver)

    # Click Beginner checkbox
    table_page.click_beginner_level()
    rows_count = table_page.get_rows_count()
    assert rows_count == 5, f"Expected 5 rows for Beginner level, but got {rows_count}"
    
def test_level_intermediate(driver):
    table_page = TablePage(driver)

    # Click Intermediate checkbox
    table_page.click_intermediate_level()
    rows_count = table_page.get_rows_count()
    assert rows_count == 2, f"Expected 2 rows for Intermediate level, but got {rows_count}"    

def test_level_advanced(driver):
    table_page = TablePage(driver)

    # Click Advanced checkbox
    table_page.click_advanced_level()
    rows_count = table_page.get_rows_count()
    assert rows_count == 2, f"Expected 2 rows for Advanced level, but got {rows_count}" 