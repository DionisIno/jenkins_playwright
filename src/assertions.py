class Assertions:

    def assert_text(self, actual_text, expected_text):
        assert actual_text == expected_text, (f"Текст не соответствует ожидаемому. "
                                              f"Ожидали {expected_text}, получили {actual_text}")
