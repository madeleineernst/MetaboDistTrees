# MetaboDistTrees

MetaboDistTrees is a python module for building chemically informed distance trees, these can be either based on chemical class or substructure information.

### Table of contents

* [Installation](#installation)
* [Dependencies](#dependencies)
* [Main citation](#main_citation)
* [Other citations](#other_citations)
* [License](#license)

## Installation

Install MetaboDistTrees with:

 `pip install metabodisttrees`
 
 
## Dependencies

python 3.6.5, networkx 2.1, numpy 1.13.3, obonet 0.2.3, os, pandas 0.22.0,  pkg_resources, scipy 1.1.0 

## Main citation <a name="main_citation"></a>
https://github.com/madeleineernst/MetaboDistTrees

## Other citations <a name="other_citations"></a>

MetaboDistTrees uses MolNetEnhancer:
https://github.com/madeleineernst/pyMolNetEnhancer

MolNetEnhancer uses molecular networking through GNPS: <br>
Wang, M.; Carver, J. J.; Phelan, V. V.; Sanchez, L. M.; Garg, N.; Peng, Y.; Nguyen, D. D.; Watrous, J.; Kapono, C. A.; Luzzatto-Knaan, T.; et al. Sharing and Community Curation of Mass Spectrometry Data with Global Natural Products Social Molecular Networking. Nat. Biotechnol. 2016, 34 (8), 828–837.
https://www.nature.com/articles/nbt.3597

MolNetEnhancer uses untargeted substructure exploration through MS2LDA: <br>
van der Hooft, J.J.J.; Wandy, J.; Barrett, M.P.; Burgess, K.E.V.; Rogers, S. Topic modeling for untargeted substructure exploration in metabolomics. PNAS 2016, 113 (48), 13738-13743.
https://www.pnas.org/content/113/48/13738

MolNetEnhancer uses Network Annotation Propagation (NAP): <br>
da Silva, R. R.; Wang, M.; Nothias, L.-F.; van der Hooft, J. J. J.; Caraballo-Rodríguez, A. M.; Fox, E.; Balunas, M. J.; Klassen, J. L.; Lopes, N. P.; Dorrestein, P. C. Propagating Annotations of Molecular Networks Using in Silico Fragmentation. PLoS Comput. Biol. 2018, 14 (4), e1006089.
http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006089

MolNetEnhancer uses DEREPLICATOR: <br>
Mohimani, H.; Gurevich, A.; Mikheenko, A.; Garg, N.; Nothias, L.-F.; Ninomiya, A.; Takada, K.; Dorrestein, P.C.; Pevzner, P.A. Dereplication of peptidic natural products through database search of mass spectra. Nat. Chem. Biol. 2017, 13, 30-37.
https://www.nature.com/articles/nchembio.2219

MolNetEnhancer uses automated chemical classification through ClassyFire: <br>
Feunang, Y. D.; Eisner, R.; Knox, C.; Chepelev, L.; Hastings, J.; Owen, G.; Fahy, E.; Steinbeck, C.; Subramanian, S.; Bolton, E.; Greiner, R.; Wishart, D.S. ClassyFire: automated chemical classification with a comprehensive, computable taxonomy. J. Cheminform. 2016, 8, 61.
https://jcheminf.biomedcentral.com/articles/10.1186/s13321-016-0174-y

Chemically informed distance trees using chemical class information is based on the chemical ontology retrieved from: http://classyfire.wishartlab.com/downloads

## License
This repository is available under the following license https://github.com/madeleineernst/MetaboDistTrees/blob/master/LICENSE

