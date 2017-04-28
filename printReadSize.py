import pysam, sys

def main(argv):
    if len(argv) == 3:
        samfile = pysam.AlignmentFile(argv[1], "rb")
        outfile = open(argv[2], 'w')
        outfile.write('pos, size')
        i=0
        iter = samfile.fetch(until_eof = True)
        try:
           while True:
                read = next(iter)
                mate = next(iter)
                if read.query_name == mate.query_name:
                    dist1 = mate.reference_end - read.reference_start
                    dist2 = read.reference_end - mate.reference_start
                    dist = max(dist1, dist2)
                    #if dist > 0:
                        #dist = dist * (-1)
                    line = '\n' + str(i) + ', ' + str(dist)
                    outfile.write(line)
                    if i%10000000==0:
                        print(dist)
                i=i+1
        except StopIteration:
            pass
        outfile.close()
        samfile.close()
    else:
        print("usage: printReadSizes.py inputfile.bam(sorted by readname) outputfile.csv")

if __name__ == "__main__":
    main(sys.argv)
