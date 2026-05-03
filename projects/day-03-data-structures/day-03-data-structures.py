def reverse_list(lst):
    ''' Here i can also use lst[::-1] but it requires O(n) for both time  and space complexity
    So instead we can use lst.reverse() which need O(n) time complexity but O(1) for space so thats better
    But lets just not use inbuilt functions for now and try to focus on logic more - two pointer approach here
    Two pointer require same complexities O(n) and O(1)
    '''
    if not lst:
        return lst
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left+=1
        right-=1

    return lst

def find_max_min(lst):

    #Here also we can directly use max(lst) and min(lst) but lets try to avoid it for now
    #First lets consider an edge case where the list is passed empty
    if not lst:
        return None, None
    # Manual approach
    max_val = lst[0]
    min_val = lst[0]
    
    for num in lst[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val

def remove_duplicates(lst):
    '''For this we can use list(set(lst)) but
    There are tradeoff that order will be lost
    So lets try to preserve the original order
    and use a better and manual approach
    '''
    seen = set() #This is very important pattern and will be later on used in many cases

    result = []
    
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

def squares(lst):
    '''This is a simple but important function
    We can use a simple loop over the list here
    But then it would be too easy and not optimal 
    Lets try to learn more about List comprehension
    and try to implement it here
    '''
    return [num * num for num in lst]
def frequency_count(lst):
    '''For count we have an inbuilt function in
    python that we can use lst.count(x) like this
    But that needs to be checked for all the elements
    means O(n) and for each element whole list would be
    traversed means O(n) again so this makes the whole 
    complexity O(n^2) so instead lets simply make a new dictionary
    for storing the numbers with their respective frequencies and 
    add if the number appears while we traverse the list'''
    freq = {}
    
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    return freq


def most_frequent(lst):
    '''For checking frequency lets use above function
    and then we can implement the most frequency by
    just comparing the frequencies this still maintains
    the time complexity of O(n)'''

    #First lets check if lst is empty
    if not lst:
        return None
    freq = frequency_count(lst)
    
    max_count = 0
    max_elem = None
    
    for key, value in freq.items():
        if value > max_count:
            max_count = value
            max_elem = key
    
    return max_elem

def common_elements(lst1, lst2):
    '''I thought about this one for a while and felt a
    bit challenging to implement using some specific logic
    Thought about implementing a simple loop and if lst1 
    have same element as lst2 then append in result but this
    has to check the whole lst2 for each element in lst1 so O(n^2)
    time complexity.. 
    Then i thought about using the more concise and very simple approach
    which can be used in python list(set(lst1) & set(lst2)) but order would
    be lost here..
    So after trying this set approach i realised one thing that why cant i 
    just convert one of the list into set and in single loop compare with it
    or even better to use a list comprehension
    This will get O(n) and also preserve order of one list'''
    
    set2 = set(lst2) # Very important pattern for filtering 
    return [x for x in lst1 if x in set2]


def analyze_list(lst):
    '''In this block lets try to reuse our functions
    and demonstrate the modular approach'''
    return {
        "unique": remove_duplicates(lst),
        "frequency": frequency_count(lst),
        "sorted": sorted(lst),
        "most_frequent": most_frequent(lst)
    }

def sort_by_frequency(freq_dict):
    items = list(freq_dict.items())
    '''In items each entry has (number, frequency) so
    x[1] means frequency here and basically we are asking
    it to sort it according to frequency and reverse so we 
    get maximum frequency first
    ''' 
    items.sort(key=lambda x: x[1], reverse=True)
    
    return dict(items)


if __name__ == "__main__":
    data = [10, 20, 20, 30, 40, 40, 40]
    empty = []
    single = [5]

    print("---- Reverse ----")
    print(reverse_list(data.copy()))
    print(reverse_list(empty))
    print(reverse_list(single))

    print("\n---- Max Min ----")
    print(find_max_min(data))
    print(find_max_min(empty))
    print(find_max_min(single))

    print("\n---- Remove Duplicates ----")
    print(remove_duplicates(data))

    print("\n---- Squares ----")
    print(squares(data))

    print("\n---- Frequency ----")
    freq = frequency_count(data)
    print(freq)

    print("\n---- Most Frequent ----")
    print(most_frequent(data))
    print(most_frequent(empty))

    print("\n---- Common Elements ----")
    print(common_elements(data, [20, 40, 50]))
    print(common_elements([1,2,2,3], [2,2,4]))

    print("\n---- Analyze List ----")
    print(analyze_list(data))

    print("\n---- Sort by Frequency ----")
    print(sort_by_frequency(freq))