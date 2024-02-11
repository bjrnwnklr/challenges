def order_weight(strng):
    return ' '.join(sorted(strng.strip().split(), key = lambda x: (sum(int(n) for n in x), x)))

print(order_weight("103 123 4444 99 2000"))
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))

'''
Test.it("Basic tests")
Test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
Test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
'''