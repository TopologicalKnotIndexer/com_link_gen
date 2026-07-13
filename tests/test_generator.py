import unittest

import com_link_gen_10
from link_rep import LinkRep


class GeneratorTests(unittest.TestCase):
    def test_document_count_and_output_are_deterministic(self):
        first = com_link_gen_10.com_link_gen(5, 2)
        second = com_link_gen_10.com_link_gen(5, 2)
        self.assertEqual(len(first), 33)
        self.assertEqual(first, second)

    def test_every_small_document_parses_and_respects_factor_bound(self):
        for document in com_link_gen_10.com_link_gen(5, 2):
            parsed = LinkRep()
            parsed.deserialize(document)
            self.assertGreaterEqual(len(parsed.link_set.var_list), 1)
            self.assertLessEqual(len(parsed.link_set.var_list), 2)
            self.assertEqual(
                len(parsed.link_method.component_list),
                len(parsed.link_set.var_list) - 1,
            )

    def test_rejects_invalid_bounds(self):
        for value in (True, 2.5):
            with self.assertRaises(TypeError):
                com_link_gen_10.com_link_gen(value, 2)
        with self.assertRaises(ValueError):
            com_link_gen_10.com_link_gen(11, 2)
        with self.assertRaises(ValueError):
            com_link_gen_10.com_link_gen(5, 0)


if __name__ == "__main__":
    unittest.main()
