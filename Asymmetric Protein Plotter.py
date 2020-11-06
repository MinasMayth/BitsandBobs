"""
Asymmetric 3D Protein Plotter

Author: samya
"""
from Bio.PDB import *
import numpy as np

def protein_plotter(protein_code):
    #The protein code to search for
    #protein_code = "3chv"
    
    pdbl = PDBList() 
    pdbl.retrieve_pdb_file(protein_code.upper(), pdir = '.', file_format = 'pdb')
    
    parser = PDBParser(PERMISSIVE = True, QUIET=True)
    data = parser.get_structure("%s", "pdb%s.ent" % protein_code)
    
    print("Identification:",data.header["name"]) 
    print(data.header["release_date"]) 
    
    #The Structure.get_models() method returns an iterator over the models. It is defined below −
    models = data.get_models() 
    models = list(models) 
    #Here, a Model describes exactly one 3D conformation. It contains one or more chains.
    
    
    x = []
    y = []
    z = []
    
    for model in list(models):
        for chain in model.get_chains():
            for residue in list(chain.get_residues()):
                atoms = list(residue.get_atoms())
                    
                x_temp = np.array([i.get_vector()[0] for i in atoms])
                y_temp = np.array([i.get_vector()[1] for i in atoms])
                z_temp = np.array([i.get_vector()[2] for i in atoms])
                
                for i in x_temp:
                    x.append(i)
                for i in y_temp:
                    y.append(i)
                for i in z_temp:
                    z.append(i)
                
                
    x, y, z = np.array(x), np.array(y), np.array(z)                
                    
    import matplotlib.pyplot as plt
    from mpl_toolkits import mplot3d
    
    
    fig=plt.figure() #Defines the figure
    axes = plt.axes(projection='3d') #Creates a blank 3D Axis
                   
    #Labels the Axis'
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    axes.set_zlabel("z")
                    
    axes.plot(x,y,z,'green')
    
protein_plotter(input("Please enter the PBD ID of the Protein you wish to plot: ").lower())