from wordfinder import WordFinder

class RandomWordFinder(WordFinder):
    """
    Get random word form a file that contains lines that are comments 
    and lines that have blank lines
    >>> random_word = RandomWordFinder('randomWords.txt')
    >>> random_word.random()
        'apple'
    >>> random_word.random()
        'kale'
    >>> random_word.random()
        'mango'
    >>> random_word.random()
        'parsnips'
    """
    def __init__(self, file):
        super().__init__(file)
        self.words = self.get_list()
        self.num_of_words = len(self.words)
   
    def get_list(self):
        """remove blank lines and lines that are comment"""
        list = [line.strip() for line in self.words]
        list_to_remove = [
            item for item in list 
            if item == '' or item.startswith('#')
            ]
        food_list = [
            item for item in list 
            if item not in list_to_remove
            ]
        return food_list
    