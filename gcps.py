class GCPs:
    def __init__(self, gcps=[]):
        self.gcps = gcps

    def __len__(self):
        return len(self.gcps)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.gcps):
            i = self.i
            self.i += 1
            return self.gcps[i]

        raise StopIteration

    def __getitem__(self, item):
        return self.gcps[item]

    def __delitem__(self, key):
        del self.gcps[key]

    def append(self, item):
        self.gcps.append(item)
