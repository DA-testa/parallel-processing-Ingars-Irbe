# python3
import math

def parallel_processing(n, m, data):
    output = []
    check = [0] * n
    num = 0
    for c in range(math.ceil(m/n)):
        for i in range(n):
            output.append((i, check[i]))
            check[i] += data[num] 
            num += 1
            if num >= m:
                break

            







    return output

def main():
    # TODO: create input from keyboard
    sk = input()
    sk = sk.split()
    # first line - n and m
    # n - thread count 
    # m - job count
    n = int(sk[0])
    m = int(sk[1])
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))


    # TODO: create the function

    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
