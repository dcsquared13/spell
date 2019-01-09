from LCSObject import LCSObject


class LCSMap():

    def __init__(self):
        self.lcs_objects = []
        self.line_id = 0

    # insert LCSObject into LCSMap
    def insert(self, entry):
        seq = entry.strip().split()
        obj = self.get_match(seq)
        self.line_id += 1

        if obj is None:
            self.lcs_objects.append(LCSObject(seq, self.line_id))
        else:
            obj.insert(seq, self.line_id)

    # will return a LCSObject
    def get_match(self, seq):
        best_match = None
        best_match_len = 0

        for obj in self.lcs_objects:
            if obj.length() < len(seq) / 2 or obj.length() > len(seq) * 2:
                continue

            lcs_len = obj.get_lcs(seq)
            if lcs_len >= len(seq)/2 and lcs_len > best_match_len:
                best_match_len = lcs_len
                best_match = obj

        return best_match

    # return size of LCSMap
    def size(self):
        return len(self.lcs_objects)

    # return object at index
    def object_at(self, idx):
        return self.lcs_objects[idx]

    # return the map as a string for testing
    def to_string(self):
        print "\nReturning {} objects in LCSMap:\n\n".format(self.size())
        for i in range(self.size()):
            print "Object {}: {}\n".format(i, self.object_at(i).to_string())
