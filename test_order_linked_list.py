import unittest
from order_linked_list import Order, OrderLinkedList

class TestOrderLinkedList(unittest.TestCase):
    def test_append_and_display(self):
        ll = OrderLinkedList()
        order1 = Order(1, "Alice", "2 items")
        order2 = Order(2, "Bob", "1 item")
        ll.append(order1)
        ll.append(order2)
        self.assertEqual(ll.head.order.customer_name, "Alice")
        self.assertEqual(ll.head.next.order.customer_name, "Bob")

    def test_reverse_normal(self):
        ll = OrderLinkedList()
        for i in range(1, 4):
            ll.append(Order(i, f"Customer{i}", f"{i} item(s)"))
        ll.reverse()
        self.assertEqual(ll.head.order.order_id, 3)

    def test_reverse_empty(self):
        ll = OrderLinkedList()
        ll.reverse()
        self.assertIsNone(ll.head)

    def test_reverse_single_element(self):
        ll = OrderLinkedList()
        ll.append(Order(1, "Solo", "One item"))
        ll.reverse()
        self.assertEqual(ll.head.order.customer_name, "Solo")

    def test_display_empty(self):
        ll = OrderLinkedList()
        try:
            ll.display()
        except Exception:
            self.fail("display() raised Exception unexpectedly!")

if __name__ == '__main__':
    unittest.main()
