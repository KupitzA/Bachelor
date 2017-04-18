import pysam, sys

def main(argv):
    if len(argv) == 4:
        samfile = pysam.AlignmentFile(argv[1], "rb")
        outfile = pysam.AlignmentFile(argv[2], "wb", template=samfile)
        i=0
        for read in samfile.fetch():
            if read.template_length > 0:
                mate = samfile.mate(read)
                dist = mate.reference_start - read.reference_end
                if dist <= int(argv[3]) and read.is_paired:
                    outfile.write(read)
                    outfile.write(mate)
                    if i%10000==0:
                        print(read.reference_start)
            i=i+1
        outfile.close()
        samfile.close()
    else:
        print("usage: sortBam.py inputfile.bam outputfile.bam insertlength")

if __name__ == "__main__":
    main(sys.argv)
