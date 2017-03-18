from multiprocessing import Pool

def f(x):
    return x*x


# pool is used for parallesim for when multiple inputs are provided to the function,
# thus processing all the functions at the same time
if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))
