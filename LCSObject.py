

class LCSObject:

    line_ids = []
    lcs_seq = []

    def __init__(self, seq, line_id):
        self.lcs_seq = seq
        self.line_ids.append(line_id)

    def __call__(self, seq, line_id):
        self.lcs_seq = seq
        self.line_ids.append(line_id)

    def get_lcs(self, seq):
        count = 0
        last_match = -1
        for i in range(len(self.lcs_seq)):
            if self.lcs_seq[i] == "*":
                continue
            for j in range(last_match + 1, len(seq)):
                if self.lcs_seq[i] == seq[j]:
                    last_match = j
                    count += 1
                    break

        return count

    def insert(self, seq, line_id):
        self.line_ids.append(line_id)
        temp = ""
        last_match = -1
        placeholder = False
        for i in range(len(self.lcs_seq)):
            if self.lcs_seq[i] == "*":
                if not placeholder:
                    temp = temp + "* "
                placeholder = True
                continue

            for j in range(last_match + 1, len(seq)):
                if self.lcs_seq[i] == seq[j]:
                    placeholder = False
                    temp = temp + self.lcs_seq[i] + " "
                    last_match = j
                    break
                elif not placeholder:
                    temp = temp + "* "
                    placeholder = True

        self.lcs_seq = temp.split()



    def length(self):
        return len(self.lcs_seq)

    def count(self):
        return len(self.line_ids)

    def to_string(self):
        return ' '.join(self.lcs_seq) + "{ " + ', '.join(self.line_ids) + " }"

        