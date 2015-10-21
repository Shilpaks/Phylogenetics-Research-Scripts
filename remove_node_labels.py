__author__ = 'michaelnute'

import sys, dendropy

def unlabel_newick_tree(infile,outfile):
    mytree = dendropy.Tree.get_from_stream(open(infile,'r'),schema='newick')
    outf = open(outfile,'w')

    for i in mytree.level_order_node_iter():
        if i.is_internal()==True:
            i._label=None

    mytree.reroot_at_midpoint()

    outf.write(mytree.as_string('newick'))
    outf.close()

def make_distribution_of_branch_lengths(infile, outfile):
    mytree = dendropy.Tree.get_from_stream(open(infile,'r'),schema='newick')
    outf = open(outfile,'w')
    print outf

    for i in mytree.level_order_edge_iter():
        outf.write(i.length)
        outf.write('\n')

    outf.close()
    pass

def list_tree_leaf_labels(infile):
    mytree = dendropy.Tree.get_from_stream(open(infile,'r'),schema='newick')
    labs = []

    for i in mytree.leaf_iter():
        labs.append(i.taxon.label)


    return labs

def print_help():
    print """
File uses dendropy to

Usage:
    --in:   path to input tree file (that includes labels on internal nodes)

    --out:  path to output tree file (which does not exist and excludes internal node labels)
            (will be overwritten if it exists)


example:
    python remove_node_labels.py --in /path/to/newick/file.tre --out /path/to/destination/file
    """


if __name__=='__main__':
    if sys.argv[1] in ['-h','--help']:
        print_help()
        sys.exit(0)
    else:
        infile = sys.argv[sys.argv.index('--in')+1]
        outfile = sys.argv[sys.argv.index('--out')+1]
        unlabel_newick_tree(infile, outfile)