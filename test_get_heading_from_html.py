from crawl import get_heading_from_html

def test_get_heading_from_html_basic(self):
    input_body = "<html><body><h1>Test Title</h1></body></html>"
    actual = get_heading_from_html(input_body)
    expected = "Test Title"
    self.assertEqual(actual, expected)


