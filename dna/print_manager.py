from collections import deque


class PrintManager:
    def __init__(self):
        self.queue = deque()
    
    def put(self, document):
        self.queue.append(document)
    
    def run(self):
        while self.queue:
            print(self.queue.popleft())
        
    def check(self, document):
        print(document)


if __name__ == "__main__":
    print_manager = PrintManager()
    print_manager.put('First Document')
    print_manager.put('Second Document')
    print_manager.run()
    print('-'*20)
    print_manager.put('Third Document')
    print_manager.run()