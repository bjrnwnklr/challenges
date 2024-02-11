inp_val = 'ttftff'
inp_op = '|&^&&'

conv_bool = {'t': True, 'f': False}
conv_str = {True: 't', False: 'f'}

def solve(s, ops):
    counter = 0
    if len(s) == 1 and len(ops) == 0:
        return s[0]
    elif len(s) == 2 and len(ops) == 1:
        a_l = s[0]
        a_r = s[1]
        return conv_str[eval_pair(a_l, a_r, ops)]
    elif len(s) > 2 and len(ops) == len(s) - 1:
        for i in range(len(ops)):
            o = ops[i] # current operator
            s_l = s[:i+1] # left side of values to process with operator
            s_r = s[i+1:] # right side of values to process with operator       
            print('\tOne iteration: %s %s %s, c = %d' % (s_l, o, s_r, counter))
            res = eval_pair(solve(s_l, ops[:i]), solve(s_r, ops[i+1:]), o)
            counter += res
            return conv_str[res]
        #return counter
    else:
        print('Error in solve:', s, ops)
        return -1000

def eval_pair(a_l, a_r, ops):
    print('eval 2: %s %s %s' % (a_l, ops, a_r))
    statement = str(conv_bool[a_l]) + ops + str(conv_bool[a_r])
    return eval(statement)


'''
Test.assert_equals(solve("tft","^&"),2)
Test.assert_equals(solve("ttftff","|&^&&"),16)
Test.assert_equals(solve("ttftfftf","|&^&&||"),339)
Test.assert_equals(solve("ttftfftft","|&^&&||^"),851)
Test.assert_equals(solve("ttftfftftf","|&^&&||^&"),2434)


t | t & f ^ f
(((t | t) & f) ^ f)
((t | t) & (f ^ f))
((t | (t & f)) ^ f)
(t | ((t & f) ^ f))
((t | t) & (f ^ f)) --- double
(t | (t & (f ^ f)))


ttff |&^

xor(and(or(t, t), f), f)
xor(or(t, and(t, f)), f)
or(t, xor(and(t, f), f))
or(t, and(t, xor(f, f)))
and(or(t, t), xor(f, f))
'''