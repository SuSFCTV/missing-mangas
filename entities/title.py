class Title:
    def __init__(self, names: list, meta=None):
        self.names = list(set(names))
        self.meta = meta
    
    def _clear(self, s):
        s = ''.join(list(filter(lambda c: c.isalpha() or c.isdigit() or c == ' ', s)))
        s = s.lower()
        return s
        
    def _fuzzy_equal(self, s1, s2):
        return self._clear(str(s1)) == self._clear(str(s2))
        
    def __eq__(self, other):
        for name1 in self.names:
            for name2 in other.names:
                if self._fuzzy_equal(name1, name2):
                    return True
        return False
    
    def strong_equal_names_n(self, other):
        eqs = 0
        for name1 in self.names:
            for name2 in other.names:
                if self._fuzzy_equal(name1, name2):
                    eqs += 1
        return eqs
    
    def get_index(self):
        try:
            return self.meta['index']
        except:
            return None
    
    def __repr__(self):
        return "<Title> with names " + ', '.join(list(map(str, self.names)))