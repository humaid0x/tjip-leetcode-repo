'''
TC: O(1)
MC: O(n) 
	n is the total size of messages
'''
class Logger:
    def __init__(self):
        self._logs = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self._logs and self._logs[message] + 10 > timestamp:
            return False

        self._logs[message] = timestamp
        return True
		