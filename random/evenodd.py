def funcArrange(inputArr):
    even = []
    odd = []
    for i in inputArr:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even+odd

def main():
    inputArr = []
    inputArr_size = int(input())
    for i in range(int(inputArr_size)):
        inputArr.append(int(input()))
    result = list(funcArrange(inputArr))
    print(",".join([str(res) for res in result]))
if __name__ == '__main__':
    main()










