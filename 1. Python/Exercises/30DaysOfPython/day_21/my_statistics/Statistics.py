class Statistics:
    def __init__(self, data: list):
        self.data = list(data);
    def get_counts(self):
        counts = {}
        unique = set(self.data)
        for i in unique:
            counts[str(i)] = self.data.count(i);
        counts = sorted(counts.items(), key=lambda x:x[1], reverse=True);
        return counts;
    def count(self):
        return len(self.data);
    def sum(self):
        return sum(self.data);
    def min(self):
        return min(self.data)
    def max(self):
        return max(self.data)
    def range(self):
        return self.max() - self.min()
    def mean(self):
        n = self.count()
        total = self.sum()
        return total/n;
    def median(self):
        self.data.sort()
        median = self.data[len(self.data)//2]
        return median
    def mode(self):
        counts = self.get_counts();
        mode = counts[0]
        mode = {'mode' : int(mode[0]), 'count': mode[1]}
        return mode;
    def std(self):
        import math as m;
        a = self.data[1]
        n = self.count();
        d_values = [x-a for x in self.data]
        summation_d = sum(d_values);
        d_sq_values = [x**2 for x in d_values];
        summation_d_sq = sum(d_sq_values);
        std = m.sqrt((summation_d_sq/n) - ((summation_d/n)**2));
        return float(format(std, '.1f'))
    def var(self):
        return float(format(float(self.std())**2, '.1f'))
    def freq_dist(self):
        counts = self.get_counts()
        counts = [(float(count*4), int(val)) for (val, count) in counts];
        values = [count for (count, x) in counts];
        sorting = {}
        for i in values:
            temp = []
            for (count, val) in counts:
                if count == i:
                    temp.append(val);
            sorting[i] = sorted(temp, reverse=True);
        output = []
        for key, values in sorting.items():
            for value in values:
                output.append((key, value));
        return output;
    def describe(self):
        string = f'Count: {self.count()}\nSum: {self.sum()}\nMin: {self.min()}\nMax: {self.max()}\nRange: {self.range()}\nMean: {self.mean()}\nMedian: {self.median()}\nMode: {self.mode()}\nStandard Deviation: {self.std()}\nVariance: {self.var()}\nFrequency Distribution: {self.freq_dist()}'
        return string;