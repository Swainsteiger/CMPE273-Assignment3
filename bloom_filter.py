from random import shuffle
from bitarray import bitarray
import mmh3
import math


class BloomFilter():
    def __init__(self, num_keys, fp_prob):
        self.num_keys = num_keys
        self.fp_prob = fp_prob
        self.size = self.get_size(num_keys, fp_prob)
        self.count_hash = self.get_count_hash(self.size, num_keys)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def get_size(self, num_keys, fp_prob):
        size = -(num_keys * math.log(fp_prob)) / (math.log(2) ** 2)
        return int(size)

    def get_count_hash(self, size, num_keys):
        count = (size / num_keys) * math.log(2)
        return int(count)

    def add(self, key):
        res = []
        i = 0
        while i < self.count_hash:
            temp = mmh3.hash(key, i) % self.size
            res.append(temp)
            self.bit_array[temp] = True
            i = i + 1

    def is_member(self, key):
        i = 0
        while i < self.count_hash:
            index = mmh3.hash(key, i) % self.size
            if not self.bit_array[index]:
                return False
            i = i + 1
        return True


