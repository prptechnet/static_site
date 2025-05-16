import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD, url=None)
        self.assertEqual(node, node2)


    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC, url= "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_empty_url_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC, url=None)
        node2 = TextNode("This is a text node", TextType.ITALIC, url="")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()