inp_val = 'ttftff'
inp_op = '|&^&&'

conv_bool = {'t': True, 'f': False}
conv_str = {True: 't', False: 'f'}

def solve(s, ops):
    counter = 0
    if len(s) == 2 and len(ops) == 1:
        print('eval 2: %s, %s. Counter: %d' % (s, ops, counter))
        return eval_pair(s, ops)
    elif len(s) > 2 and len(ops) == len(s) - 1:
        for i in range(len(s)-1):
            x = conv_str[eval_pair(s[i:i+2], ops[i])]
            temp_s = s[:i] + x + s[i+2:]
            temp_ops = ops[:i] + ops[i+1:]
            print('recurse: %s, %s. Counter: %d' % (temp_s, temp_ops, counter))
            counter += solve(temp_s, temp_ops)
        return counter
    else:
        print('Error in solve:', s, ops)
        return -1000

def eval_pair(s, ops):
    if len(s) != 2 or len(ops) != 1:
        print('Error in eval_pairs:', s, ops)
        return -1
    else:
        statement = str(conv_bool[s[0]]) + ops + str(conv_bool[s[1]])
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