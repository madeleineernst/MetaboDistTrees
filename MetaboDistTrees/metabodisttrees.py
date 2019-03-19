#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:19:11 2018

@author: madeleineernst
"""
import scipy
from scipy.cluster import hierarchy
import numpy as np
import pandas as pd
import obonet
import networkx
import os


# from https://stackoverflow.com/questions/28222179/save-dendrogram-to-newick-format
def getNewick(node, newick, parentdist, leaf_names):
    if node.is_leaf():
        return "%s:%.2f%s" % (leaf_names[node.id], parentdist - node.dist, newick)
    else:
        if len(newick) > 0:
            newick = "):%.2f%s" % (parentdist - node.dist, newick)
        else:
            newick = ");"
        newick = getNewick(node.get_left(), newick, node.dist, leaf_names)
        newick = getNewick(node.get_right(), ",%s" % (newick), node.dist, leaf_names)
        newick = "(%s" % (newick)
        return newick

def get_motiftrees(motifs, buckettable, method = "ward", metric = "euclidean", outputdir = "MotifTree/"):
    
    os.mkdir(outputdir)
    
    # select only features present in tree
    bt_sel = buckettable[buckettable['#OTU ID'].isin(list(set(buckettable['#OTU ID']) & set(motifs['scans'])))]
    bt_sel.to_csv(outputdir + 'Buckettable_Motifs.tsv', sep = '\t', index = False)
    
    motifs = motifs[pd.notnull(motifs['motif'])] # remove features, which do not contain any motif
    motifs = motifs.loc[:, (motifs != 0).any(axis=0)]
    motifs.index = motifs['scans']
    motifs = motifs.filter(like='motif_') # select all motif columns
    
    Z = scipy.cluster.hierarchy.linkage(motifs, method=method, metric=metric)
    leaf_names = motifs.index # remove white space from leaf labels
    tree = hierarchy.to_tree(Z,False)
    
    f = open(outputdir + 'Tree_Motifs.txt','w')
    f.write(getNewick(tree, "", tree.dist, leaf_names))
    f.close()
    
    
def get_classytrees(cf,buckettable, lev,outputdir = "ClassyTree/"):
    
    os.mkdir(outputdir)
     
    # remove inorganic compounds by default
    cf = cf[cf.CF_kingdom != 'Inorganic compounds']
    cf = cf.rename(columns = {'cluster index':'cluster.index'})
    
    graph = obonet.read_obo('../data/ChemOnt_2_1.obo')
    
    # Mapping from term ID to name
    id_to_name = {id_: data['name'] for id_, data in graph.nodes(data=True)}
    name_to_id = {data['name']: id_ for id_, data in graph.nodes(data=True) if 'name' in data}
    
    for i in range(len(lev)):
        
        if lev[i] == 'cluster.index':
            
            all_subclasses = list(set(cf['CF_Dparent']))
            all_subclasses = [x for x in all_subclasses  if str(x) != 'nan']
            all_subclasses = [x for x in all_subclasses  if str(x) != 'no matches']
            all_subclasses = [x for x in all_subclasses  if str(x) != ' ']
            
            a = []
            for j in all_subclasses:
                paths = networkx.all_simple_paths(
                        graph,source=name_to_id[j],
                        target=name_to_id['Organic compounds'])
                for path in paths:
                    a.append('#'.join(id_to_name[node] for node in path))
                             
            
            notintree = list(set(cf['CF_Dparent']) - set(all_subclasses))
            cf = cf[~cf['CF_Dparent'].isin(notintree)]
            #b = list(set(cf[lev[i]]))
            b = list(cf['CF_Dparent'])
            for index,item in enumerate(b):
                b[index] = '#'.join([str(list(cf[lev[i]])[index]) ,a[all_subclasses.index(item)]])  
            
            inames = []
            for index, item in enumerate(b): 
                inames.append(b[index].split('#', 1)[0])
                b[index] = b[index].split('#', 1)[-1]
            
            df = pd.DataFrame(b)
            df = df.iloc[:,0].str.get_dummies(sep='#')
            df.index = inames
            
            df.to_csv(outputdir + 'Classlist_' + lev[i] + '.tsv',sep='\t',index=True)
            
            # do hierarchical cluster analysis on classlist and convert to newick format
            Z = scipy.cluster.hierarchy.linkage(df, method='average', metric='jaccard')
            
            leaf_names = df.index # remove white space from leaf labels
            tree = hierarchy.to_tree(Z,False)
            
            f = open(outputdir + 'NewickTree_' + lev[i] + '.txt','w')
            f.write(getNewick(tree, "", tree.dist, leaf_names))
            f.close()
        
        else:
            all_subclasses = list(set(cf[lev[i]]))
            all_subclasses = [x for x in all_subclasses  if str(x) != 'nan']
            all_subclasses = [x for x in all_subclasses  if str(x) != 'no matches']
            all_subclasses = [x for x in all_subclasses  if str(x) != ' ']
            
            a = []
            for j in all_subclasses:
                paths = networkx.all_simple_paths(
                        graph,source=name_to_id[j],
                        target=name_to_id['Organic compounds'])
                for path in paths:
                    a.append('#'.join(id_to_name[node] for node in path))
            
            inames = []
            for index, item in enumerate(a): 
                inames.append(a[index].split('#', 1)[0])
                a[index] = a[index].split('#', 1)[-1]
            
            df = pd.DataFrame(a)
            df = df.iloc[:,0].str.get_dummies(sep='#')
            df.index = [num.replace(' ', '.') for num in inames]
            df.index = [num.replace(',', '.') for num in df.index]
            df.index = [num.replace('(', '.') for num in df.index]
            df.index = [num.replace(')', '.') for num in df.index]
            df.index = [num.replace("'", '') for num in df.index]
            df.index = [num.replace('[', '.') for num in df.index]
            df.index = [num.replace(']', '.') for num in df.index]
            
            df.to_csv(outputdir + 'Classlist_' + lev[i] + '.tsv',sep='\t',index=True)
            
            # do hierarchical cluster analysis on classlist and convert to newick format
            Z = scipy.cluster.hierarchy.linkage(df, method='average', metric='jaccard')
            
            leaf_names = df.index # remove white space from leaf labels
            tree = hierarchy.to_tree(Z,False)
            
            f = open(outputdir + 'NewickTree_' + lev[i] + '.txt','w')
            f.write(getNewick(tree, "", tree.dist, leaf_names))
            f.close()
            
    # select only features present in tree
    bt_sel = buckettable[buckettable['#OTU ID'].isin(list(set(buckettable['#OTU ID']) & set(cf['cluster.index'])))]
    bt_sel.to_csv(outputdir + 'Buckettable_ChemicalClasses.tsv', sep = '\t', index = False)


