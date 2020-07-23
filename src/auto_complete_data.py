class AutoCompleteData:
    
    def __init__(self, data):
        self.completed_sentence = data["sentence"]
        self.source_text = [data["src"], data["line"]]
        self.offset = data["offset"]
        self.score = data["score"]


