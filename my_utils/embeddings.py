import numpy as np

def get_embeddings(path, wrd2idx):

    """
        Recover an embedding matrix consisting of the relevant
        vectors for the given set of words
    """
    with open(path) as fid:
        voc_size = len(wrd2idx)        
        _, emb_size = fid.readline().split()        
        E = np.zeros((int(emb_size), voc_size))
        for line in fid.readlines():
            items = line.split()
            wrd   = items[0]
            if wrd in wrd2idx:
                E[:, wrd2idx[wrd]] = np.array(items[1:]).astype(float)
    # Number of out of embedding vocabulary embeddings
    n_OOEV = np.sum((E.sum(0) == 0).astype(int))
    perc = n_OOEV*100./len(wrd2idx)
    print ("%d/%d (%2.2f %%) words in vocabulary found no embedding" 
           % (n_OOEV, len(wrd2idx), perc)) 
    return E

def filter_embeddings(path_in, path_out, wrd2idx):

    """
        Filter embeddings file to contain only the relevant set
        of words (so that it can be loaded faster)
    """
    with open(path_out,"w") as fod:
        with open(path_in,"r") as fid:
            voc_size = len(wrd2idx)
            _, emb_size = fid.readline().split()        
            fod.write(str(voc_size)+"\t"+str(emb_size)+"\n")
            for line in fid.readlines():
                items = line.decode("utf-8").split()
                wrd   = items[0]
                if wrd in wrd2idx:
                    fod.write(line.encode("utf-8"))
    