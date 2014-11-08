def assign_drug(filename):
    """
    Takes a filename and returns the string "tylenol" if odd-numbered file
    and string "placebo" if it is an even-numbered file.
    """
    
    base_name = filename.split('.')[0]
    #file_number = int(base_name.split('_')[1])
    file_number = int(base_name[-1])
    if file_number % 2 == 0:
        return "placebo"
    else:
        return "tylenol"

assert assign_drug('inflammation_1.dat') == 'tylenol'
assert assign_drug('inflammtion_4.dat') == 'placebo'
assert assign_drug('inflammtion_3.dat') == 'tylenol'
