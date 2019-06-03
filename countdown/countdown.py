import operator
import itertools
import time
from collections import defaultdict


def good_order(input_list):
    """This function determines if all 2s and 3s come before all 0s and 1s in a list"""
    hit23=False
    for i in input_list:
        if i > 1:
            hit23 = True
        if hit23 and i<2:
            return False
    return True


# Global Constants, op and operator_list
op = (operator.mul, operator.div, operator.add, operator.sub)

operator_list = [] # Indices for operators, 0,1,2,3 is *,/,+,-
for i4 in xrange(4 ** 5):
    cl = [i4 // 256 % 4, i4 // 64 % 4, i4 // 16 % 4, i4 // 4 % 4, i4 % 4]
    if good_order(cl):
        operator_list.append(cl)
print len(operator_list)

def gen_nums(loop_array):
    """Generate all possible numbers created from operations/rearrangements of a tuple"""
    nums = defaultdict(set)

    for line2 in loop_array:
        nums_index = sorted(line2)
        nums_index = tuple([int(i) for i in nums_index]) #change to lambda

        for ops in operator_list:
            num = line2[0]
            for i in range(1, 6):
                num = op[ops[i - 1]](num, line2[i])
                if 100 <= num < 1000 and num.is_integer():
                    nums[nums_index].add(int(num))
    return nums


def write_file(nums, option_type):
    with open('results/'+option_type+'.txt','w') as f:
        for num in nums:
            f.write(str(num)+';')
            for i in sorted(nums[num]):
                f.write(str(i)+';')
            f.write("\n")
        print len(nums)


def main():
    L_array = [25., 50., 75., 100.]
    s_array = [float(i) for i in range(1, 11)]
    start = time.time()
    option = 9
    all_options = False

    # Labcde
    if option == 0 or all_options:
        option_type = "Labcde"
        print option_type, option
        nums = {}
        for L in L_array:
            for s in itertools.combinations(s_array, 5):
                loop_array = itertools.permutations([L] + list(s))
                nums.update(gen_nums(loop_array))
        write_file(nums, option_type)
        print time.time() - start, " time elapsed\n"

    #Laabcd
    if option == 1 or all_options:
        option_type = "Laabcd"
        print option_type, option
        nums = {}
        for s in itertools.combinations(s_array, 4): #does this need to be permutations?
            for L in L_array:
                for s0 in s:
                    loop_array = itertools.permutations([L] + list(s) + [s0])
                    nums.update(gen_nums(loop_array))
        write_file(nums, option_type)
        print time.time() - start, " time elapsed\n"

    #Laabbc
    if option == 2 or all_options:
        option_type = "Laabbc"
        print option_type, option
        nums = {}
        for s in itertools.permutations(s_array, 3): #does this need to be permutations?
            for L in L_array:
                loop_array = itertools.permutations([L] + list(s) + [s[0],s[1]])
                nums.update(gen_nums(loop_array))
        write_file(nums, option_type)
        print time.time() - start, " time elapsed\n"

    #LLabcd
    if option == 3 or all_options:
        option_type = "LLabcd"
        print option_type, option
        nums = {}
        for s in itertools.combinations(s_array, 4):
            for L in itertools.combinations(L_array, 2):
                loop_array = itertools.permutations(list(L) + list(s))
                nums.update(gen_nums(loop_array))
        write_file(nums, option_type)
        print time.time() - start, " time elapsed\n"

    #LLaabc
    if option == 4 or all_options:
        option_type = "LLaabc"
        print option_type, option
        nums = {}
        for s in itertools.combinations(s_array, 3):
            for L in itertools.combinations(L_array, 2):
                for s0 in s:
                    loop_array = itertools.permutations(list(L) + list(s) + [s0])
                    nums.update(gen_nums(loop_array))
        write_file(nums, option_type)
        print time.time() - start, " time elapsed\n"
        #print count, ncr(4,2)*10*ncr(9,2)*720/2

    #LLaabb
    if option == 5 or all_options:
        option_type = "LLaabb"
        print option_type, option
        nums = {}
        for s in itertools.combinations(s_array, 2):
            for L in itertools.combinations(L_array, 2):
                loop_array = itertools.permutations(list(L) + list(s) + list(s))
                nums.update(gen_nums(loop_array))
        write_file(nums, option_type)
        print time.time() - start, " time elapsed\n"

    #LLLabc
    if option == 6 or all_options:
        option_type = "LLLabc"
        print option_type, option
        nums = {}
        for s in itertools.combinations(s_array, 3):
            for L in itertools.combinations(L_array, 3):
                loop_array = itertools.permutations(list(L) + list(s))
                nums.update(gen_nums(loop_array))
        write_file(nums, option_type)
        print time.time() - start, " time elapsed\n"

    #LLLaab
    if option == 7 or all_options:
        option_type = "LLLaab"
        print option_type, option
        nums = {}
        for s in itertools.combinations(s_array, 2):
            for L in itertools.combinations(L_array, 3):
                for s0 in s:
                    loop_array = itertools.permutations(list(L) + list(s) + [s0])
                    nums.update(gen_nums(loop_array))
        write_file(nums, option_type)
        print time.time() - start, " time elapsed\n"

    #LLLLab
    if option == 8 or all_options:
        option_type = "LLLLab"
        print option_type, option
        nums = {}
        for s in itertools.permutations(s_array, 2):
            loop_array = itertools.permutations(L_array + list(s))
            nums.update(gen_nums(loop_array))
        write_file(nums, option_type)
        print time.time()-start, " time elapsed\n"

    #LLLLaa
    if option == 9 or all_options:
        option_type = "LLLLaa"
        nums = {}
        for a in s_array:
            loop_array = itertools.permutations(L_array+[a,a])
            nums.update(gen_nums(loop_array))
        write_file(nums, option_type)
        print time.time()-start, " time elapsed\n"


if __name__ == '__main__':
    main()
