class Sol:
    def to_goat_latin(self,sentence):
        s=sentence.split()
        vowels=['a','e','i','o','u']
        for i, word in enumerate(s):
            if word[0].lower() not in vowels:
                s[i]=word[1:]+word[0]
            s[i]+='m'+(i+2)*'a'
        return s

if __name__ == '__main__':
    p = Sol()
    print(p.to_goat_latin(sentence = "I speak Goat Latin"))
