from time import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TablePage(BasePage):
    TABLE_ROWS = (By.CSS_SELECTOR, "table#courses_table tbody tr:not([style*='display:none']):not([style*='display: none']):not(.hidden)")
    TABLE_COLS = (By.CSS_SELECTOR, "table#courses_table thead th")
    LANG_RADIOS = (By.NAME, "lang")
    LANG_COL = (By.CSS_SELECTOR, "table#courses_table tbody tr td:nth-child(3)")
    BEGINNER_CHECKBOX = (By.XPATH, "//*[@id='xpath-table']/div[2]/fieldset[2]/label[1]/input")
    INTERMEDIATE_CHECKBOX = (By.XPATH, "//*[@id='xpath-table']/div[2]/fieldset[2]/label[2]/input")
    ADVANCED_CHECKBOX = (By.XPATH, "//*[@id='xpath-table']/div[2]/fieldset[2]/label[3]/input")

    def get_table_rows(self):
        self.visit("https://practicetestautomation.com/practice-test-table/")
        return self.driver.find_elements(*self.TABLE_ROWS)
    
    def get_rows_count(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows)

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
    
    def click_beginner_level(self):
        self.visit("https://practicetestautomation.com/practice-test-table/")
        if self.driver.find_element(*self.BEGINNER_CHECKBOX).is_selected():
            self.driver.find_element(*self.INTERMEDIATE_CHECKBOX).click()
            self.driver.find_element(*self.ADVANCED_CHECKBOX).click()
    
    def click_intermediate_level(self):
        self.visit("https://practicetestautomation.com/practice-test-table/")
        if self.driver.find_element(*self.INTERMEDIATE_CHECKBOX).is_selected():
            self.driver.find_element(*self.BEGINNER_CHECKBOX).click()
            self.driver.find_element(*self.ADVANCED_CHECKBOX).click()
    
    def click_advanced_level(self):
        self.visit("https://practicetestautomation.com/practice-test-table/")
        if self.driver.find_element(*self.ADVANCED_CHECKBOX).is_selected():
            self.driver.find_element(*self.BEGINNER_CHECKBOX).click()
            self.driver.find_element(*self.INTERMEDIATE_CHECKBOX).click()