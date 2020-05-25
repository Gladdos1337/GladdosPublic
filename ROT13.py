class ROT13():
    def __init__(self, text):
        self.text = text

    def __len__(self):
        return len(self.text)
        
    def solver(self,text):
        i = 0
        text = list
        while i < len(text):
            if text[i] == "a" or "A":
                text[i] = "Z"
            i+=1
        text = "".join(text)

        return text
    
text = "This ain't nothing to relate to."
solver = ROT13(text)
print(solver.solver(text))
