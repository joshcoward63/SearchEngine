import unittest
import crawler as cr
class TestCrawlerMethods(unittest.TestCase):

    def test_get_links_from_current_page1(self):
        self.assertEqual(list,type(cr.get_first("https://www.boisestate.edu/coen-cs/")))
    
    def test_get_links_from_current_page2(self):
        self.assertEqual(list,type(cr.get_first("https://www.geeksforgeeks.org/unit-testing-python-unittest/")))        

    def test_get_links_from_current_page3(self):
        self.assertEqual(list,type(cr.get_first("https://www.allrecipes.com/recipe/214931/oven-roasted-asparagus/")))

    def test_get_links_from_current_page4(self):
        self.assertEqual(list,type(cr.get_first("https://www.boisestate.edu/index/")))

    def test_get_links_from_current_page5(self):
        self.assertEqual(list,type(cr.get_first("https://www.naturalreaders.com/online/")))

    def test_get_links_from_current_page6(self):
        self.assertEqual(list,type(cr.get_first("https://www.boisestate.edu/accessibility/")))

    def test_get_links_from_current_page7(self):
        self.assertEqual(list,type(cr.get_first("https://www.yahoo.com/")))

    def test_get_links_from_current_page8(self):
        self.assertEqual(list,type(cr.get_first("https://en.wikipedia.org/wiki/Main_Page")))

    def test_get_links_from_current_page9(self):
        self.assertEqual(list,type(cr.get_first("https://www.boisestate.edu/accessibility/faculty/")))

    def test_get_links_from_current_page10(self):
        self.assertEqual(list,type(cr.get_first("https://www.boisestate.edu/accessibility/students/")))
    
    def test_get_links_from_pages(self):
        self.assertEqual(list, type(cr.get_all_urls(cr.get_first("https://www.boisestate.edu/coen-cs/"))))


if __name__ == '__main__': 
    unittest.main() 