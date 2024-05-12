def get_counts(items: list):
    unique_items = list(set(items));
    unique_items.sort()
    counts_along_item = {}
    for item in unique_items:
        counts_along_item[items.count(item)] = [int(i) for i in item.split('-')];
    return counts_along_item;

def get_ci_freqs(values: list):
    values = [[CI, fi] for (fi, CI) in values];
    class_intervals = [CI for [CI, x] in values];
    frequencies = [fi for [x, fi] in values];
    return [class_intervals, frequencies];

def eval_mean(values: list):
    class_intervals, frequencies = get_ci_freqs(values);
    xi_values = [sum(CI)/2 for CI in class_intervals]
    fi_xi = [(fi * xi) for fi, xi in zip(frequencies, xi_values)]
    mean = sum(fi_xi) / sum(frequencies);
    return float(format(mean, '.2f'));

def  eval_median(values: list):
    class_intervals, frequencies = get_ci_freqs(values);
    index = 1
    f = frequencies[index]
    h = abs(class_intervals[index][0] - class_intervals[index][1])
    cumulative_frequency = []
    cumulative_frequency.append(frequencies[0])
    i = 0;
    go = True
    while go:
        try:
            cumulative_frequency.append(cumulative_frequency[i] + frequencies[i+1])
        except:
            go = False;
            pass;
        i += 1
    m = cumulative_frequency[index-1]
    l = class_intervals[index][0]
    # ∑n/2
    val = sum(frequencies)/2;
    median = l + ((val-m)/f) * h
    return float(format(median, '.2f'))

def eval_standard_deviation(values: list):
    import math as m
    class_intervals, frequencies = get_ci_freqs(values);
    xi_values = [sum(CI)/2 for CI in class_intervals]
    mean = eval_mean(values);
    sum_of_fi_xi_square = sum([(fi*(xi**2)) for fi, xi in zip(frequencies, xi_values)]);
    standard_deviation = m.sqrt((sum_of_fi_xi_square/sum(frequencies))-(mean**2))    
    return float(format(standard_deviation, '.2f'))

