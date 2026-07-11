class TRFAManager:
    def __init__(self):
        self.true_keywords = set()
        self.false_keywords = set()
        self.current_mode = "True"

    def set(self, mode: str):
        if mode in ["True", "False"]:
            self.current_mode = mode
        else:
            raise ValueError("mode Error")

    def main(self, keyword: str):
        if self.current_mode == "True":
            self.true_keywords.add(keyword)
        else:
            self.false_keywords.add(keyword)

    def qnatr(self, keyword: str) -> bool:
        return keyword in self.true_keywords

    def have(self, text: str) -> bool:
        for kw in self.true_keywords:
            if kw in text:
                return True
        return False

    def haver(self, char: str) -> bool:
        target_set = self.true_keywords if self.current_mode == "True" else self.false_keywords
        for kw in target_set:
            if char in kw:
                return True
        return False

    def reset(self):
        self.true_keywords.clear()
        self.false_keywords.clear()
        self.current_mode = "True"