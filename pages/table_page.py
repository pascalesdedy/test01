from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TablePage(BasePage):
    TABLE_ROWS = (By.CSS_SELECTOR, "table#courses_table tbody tr")
    TABLE_COLS = (By.CSS_SELECTOR, "table#courses_table thead th")

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
        match lang:
            case "Any":
                self.visit("https://practicetestautomation.com/practice-test-table/")
                lang_option = self.driver.find_element(*self.SELECT_ANY)
                lang_option.click()
            case "Java":    
                self.visit("https://practicetestautomation.com/practice-test-table/")
                lang_option = self.driver.find_element(*self.SELECT_JAVA)
                lang_option.click()
            case "Python":    
                self.visit("https://practicetestautomation.com/practice-test-table/")
                lang_option = self.driver.find_element(*self.SELECT_PYTHON)
                lang_option.click()
            
        
    