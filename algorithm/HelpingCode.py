import random;
for x in range(10):
    a = random.randint(1,6);
    b = random.randint(1,6);
    c = random.randint(1,6);

    smallest = min(a,b,c);
    biggest = max(a,b,c)
    median = a+b+c-smallest-biggest

    print('Smallest value: '+ str(smallest));
    print('Median: '+ str(median));
    print('Biggest value: '+ str(biggest));

    if median - smallest == biggest - median:
        print('The medianen is in between the largest and smallest value.')
    else:
        print('The medianen is not between the largest and smallest value.')