class LCSObject:

    def __init__(self, seq, line_id):
        self.lcs_seq = seq
        self.line_ids = [line_id]

    """DP based LCS count between a sequence and this object"""
    def get_lcs(self, seq):
        # find the length of the sequences
        this_seq = len(self.lcs_seq)
        new_seq = len(seq)

        # declaring the array for storing the dp values
        L = [[0] * (new_seq + 1) for i in xrange(this_seq + 1)]

        # Build L table in standard dynamic programming approach
        for i in range(this_seq + 1):
            for j in range(new_seq + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif self.lcs_seq[i - 1] == seq[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        return L[this_seq][new_seq]

    """Insert a new line item into this object"""
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

    """Length of the sequence"""
    def length(self):
        return len(self.lcs_seq)

    """Number of line ids assigned to this object"""
    def count(self):
        return len(self.line_ids)

    """Return object as a string for testing"""
    def to_string(self):
        return ' '.join(self.lcs_seq) + " : { " + ', '.join(str(x) for x in self.line_ids) + " }"
