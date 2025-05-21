import os


class LoadWords:
    def __init__(self, file_name: str):
        if not os.path.exists(file_name):
            with open(file_name, 'w', encoding='utf-8') as file:
                pass
        self._file_name = file_name

    def load_words(self, words: dict[str, str | list[str]]) -> None:
        """_summary_

        Args:
            words (dict[str, str]): dictionary. First value must be an original word.
            Second value must be a translation.
        """
        with open(self._file_name, 'r+', encoding='utf-8') as file:
            for original, translations in words.items():
                file.write(f"{original}: {translations}\n")

    def get_words(self) -> dict[str, str | list[str]]:
        with open(self._file_name, 'r+', encoding='utf-8') as file:
            words = {}
            for line in file.readlines():
                line = line.strip()
                line = line.split(": ")
                exist = words.get(line[0])
                if exist:
                    words[line[0]].add(line[1])
                else:
                    words[line[0]] = set()
                    words[line[0]].add(line[1])
            for key, value in words.items():
                words[key] = list(value)
        return words


if __name__ == '__main__':
    loading = LoadWords("words.txt")
    loading.load_words({"coffee": "кофе", "eat": "есть"})
    words_for_train = loading.get_words()
