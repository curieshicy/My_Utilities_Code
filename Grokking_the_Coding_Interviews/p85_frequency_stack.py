from collections import defaultdict
class FrequencyStack:
    def __init__(self):
        self.num_dict = defaultdict(int)
        self.freq_count = defaultdict(list)
        self.max_freq = 0
        
    def push(self, num):
        self.num_dict[num] += 1
        self.freq_count[self.num_dict[num]].append(num)
        self.max_freq = max(self.max_freq, self.num_dict[num])

    def pop(self):
        popped_val = self.freq_count[self.max_freq].pop()
        self.num_dict[popped_val] -= 1
        if not self.freq_count[self.max_freq]:
            del self.freq_count[self.max_freq]
            self.max_freq -= 1
        return popped_val
        
        
def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


main()
