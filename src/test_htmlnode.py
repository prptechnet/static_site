import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_not_eq(self):
        test_props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(value="This is a text node", props=test_props)
        node2 = HTMLNode(value="This is a text node")
        self.assertNotEqual(node, node2)

    def test_props_to_html_eq(self):
        test_props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(value="This is a text node", props=test_props)
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_props_to_html_not_eq(self):
        test_props = {"href": "https://www.bing.com", "target": "_blank"}
        node = HTMLNode(value="This is a text node", props=test_props)
        self.assertNotEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

#class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_not_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertNotEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_title(self):
        node = LeafNode("title", "Hello, world!")
        self.assertEqual(node.to_html(), "<title>Hello, world!</title>")

    def test_leaf_to_html_not_title(self):
        node = LeafNode("title", "Hello, world!")
        self.assertNotEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_not_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertNotEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_not_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(node.to_html(), "<a>Click me!</a>")

#class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()