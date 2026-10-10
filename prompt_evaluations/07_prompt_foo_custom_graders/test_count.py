import unittest

from count import get_assert


class CountGraderTests(unittest.TestCase):
    def test_topic_matching_is_case_insensitive(self):
        for topic in ("sheep", "Sheep", "SHEEP"):
            with self.subTest(topic=topic):
                result = get_assert(
                    "sheep Sheep SHEEP", {"vars": {"topic": topic, "count": 3}}
                )
                self.assertEqual(
                    result,
                    {
                        "pass": True,
                        "score": 1,
                        "reason": f"Expected {topic} to appear 3 times. Actual: 3",
                    },
                )

    def test_wrong_counts_fail(self):
        for count in (2, 4):
            with self.subTest(count=count):
                result = get_assert(
                    "sheep sheep sheep", {"vars": {"topic": "Sheep", "count": count}}
                )
                self.assertFalse(result["pass"])
                self.assertEqual(result["score"], 0)
                self.assertTrue(result["reason"].endswith("Actual: 3"))

    def test_zero_matches(self):
        result = get_assert("no animals here", {"vars": {"topic": "Sheep", "count": 0}})
        self.assertTrue(result["pass"])

    def test_topic_is_escaped(self):
        result = get_assert("a.b axb A.B", {"vars": {"topic": "A.B", "count": 2}})
        self.assertTrue(result["pass"])


if __name__ == "__main__":
    unittest.main()
