from bloomfilter import BloomFilter
import uuid

def getRandomString():
	return str(uuid.uuid4())

def dblookuptimetest():
    print("Testing DB lookup time using bloom filter\n")
    bf = BloomFilter(500000, 7)
    huge = []

    lines = open("/usr/share/dict/american-english").read().splitlines()
    for line in lines:
        bf.add(line)
        huge.append(line)

    import datetime

    start = datetime.datetime.now()
    bf.contains("google")
    finish = datetime.datetime.now()
    print('Checking "google" using bloom filter in dictionary\n')
    print((finish - start).microseconds)

    start = datetime.datetime.now()
    for word in huge:
        if word == "google":
            break
    finish = datetime.datetime.now()
    print('Checking "google" without  using bloom filter in dictionary\n')
    print((finish - start).microseconds)

    print(bf.contains("Max"))
    print(bf.contains("mice"))
    print(bf.contains("3"))

    start = datetime.datetime.now()
    bf.contains("apple")
    finish = datetime.datetime.now()
    print((finish - start).microseconds)

    start = datetime.datetime.now()
    for word in huge:
        if word == "apple":
            break
    finish = datetime.datetime.now()
    print((finish - start).microseconds)


if __name__ == '__main__':
    dblookuptimetest()
	# filter of 1 Mb, 1 million bits, 20% elements entered, k=3
