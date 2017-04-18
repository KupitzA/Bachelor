import pysam, sys

def main(argv):
    if len(argv) == 3:
        samfile = pysam.AlignmentFile(argv[1], "rb")
        outfile = open(argv[2], "w")
        i=0
        for read in samfile.fetch():
            if read.template_length > 0:
                mate = samfile.mate(read)
                dist = mate.reference_start - read.reference_end
                outfile.write(str(dist))
                if i%10000==0:
                   print(read.reference_start)
            i=i+1
        outfile.close()
        samfile.close()
    else:
        print("usage: printInsertSize.py inputfile.bam outputfile.log")

if __name__ == "__main__":
    main(sys.argv)
