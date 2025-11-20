from time import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TablePage(BasePage):
    TABLE_ROWS = (By.CSS_SELECTOR, "table#courses_table tbody tr")
    TABLE_COLS = (By.CSS_SELECTOR, "table#courses_table thead th")
    LANG_RADIOS = (By.NAME, "lang")
    LANG_COL = (By.CSS_SELECTOR, "table#courses_table tbody tr td:nth-child(3)")

    SELECT_ANY = (By.XPATH, "//*[@id='xpath-table']/div[2]/fieldset[1]/label[1]")
    SELECT_JAVA = (By.XPATH, "//*[@id='xpath-table']/div[2]/fieldset[1]/label[2]")
    SELECT_PYTHON = (By.XPATH, "//*[@id='xpath-table']/div[2]/fieldset[1]/label[3]")

    def get_table_rows(self):
        self.visit("https://practicetestautomation.com/practice-test-table/")
        return self.driver.find_elements(*self.TABLE_ROWS)

    def get_table_columns(self):
        self.visit("https://practicetestautomation.com/practice-test-table/")
        return self.driver.find_elements(*self.TABLE_COLS)

    def get_table_column_values(self):
        cols = self.get_table_columns()
        return [col.text for col in cols]
    
    def get_column_values(self, col_index):
        rows = self.get_table_rows()
        column_values = []
        for row in rows:    
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > col_index:
                column_values.append(cells[col_index].text)
            return column_values
        
    def select_lang(self, lang):
        self.visit("https://practicetestautomation.com/practice-test-table/")
        radios = self.driver.find_elements(*self.LANG_RADIOS)
        for r in radios:
            if r.get_attribute("value") == lang:
                r.click()
                return
    
    def get_language_column(self):
        cols = self.driver.find_elements(*self.LANG_COL)
        return [c.text.strip() for c in cols]
    
    def get_table_languages(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        langs = []
        for r in rows:
            cells = r.find_elements(By.TAG_NAME, "td")
            langs.append(cells[2].text.strip())   # kolom Language
        return langs