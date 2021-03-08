import unittest
import crawler as cr
class TestCrawlerMethods(unittest.TestCase):

    def test_get_links_from_current_page(self):
        self.assertEqual(list,type(cr.get_first("https://www.boisestate.edu/coen-cs/")))

    def test_get_links_from_pages(self):
        self.assertEqual(list, type(cr.get_all_urls(cr.get_first("https://www.boisestate.edu/coen-cs/"))))


if __name__ == '__main__': 
    unittest.main() 