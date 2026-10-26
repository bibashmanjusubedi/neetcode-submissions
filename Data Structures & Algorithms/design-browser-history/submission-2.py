class BrowserHistory:

    def __init__(self, homepage: str):
        self.backHistory = [homepage]
        self.frontHistory = []
        

    def visit(self, url: str) -> None:
        self.backHistory.append(url)
        self.frontHistory = []
        
    def back(self, steps: int) -> str:
        while steps and len(self.backHistory) > 1:
            self.frontHistory.append(self.backHistory.pop())
            steps -=1
        return self.backHistory[-1]

    def forward(self, steps: int) -> str:
        while steps and self.frontHistory:
            self.backHistory.append(self.frontHistory.pop())
            steps -=1
        return self.backHistory[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)