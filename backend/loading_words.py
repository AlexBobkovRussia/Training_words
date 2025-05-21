import psycopg2


class LoadWords:
    def __init__(self):
        self.__conn = psycopg2.connect(dbname="Words",
                                       user="postgres",
                                       password="asdfvcxz16022011",
                                       host="95.79.11.225",
                                       port=5433)
        self._cursor = self.__connection.cursor()

    def load_words(self, words: dict[str, str]) -> None:
        """_summary_

        Args:
            words (dict[str, str]): dictionary. First value must be an original word.
            Second value must be a translation.
        """
        for original, translation in words.items():
            pass


if __name__ == '__main__':
    loading = LoadWords()
