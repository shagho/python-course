class Note:
    def __init__(self, memo):
        self.message=memo

    def getMessage(self):
        return self.message

    def setMessage(self, new_memo):
        self.message = new_memo

    def __str__(self):
        #return "{}".format(self.message)
        return f'{self.message}'