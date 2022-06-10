#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import load_cube

Clean = load_cube.CUBE('/work/common/hxin_lab/ishanj13/solar_cells/cp2k/metals/I_lc/Pt/111/atop/clean/I_Pt-ELEC_POTENTIAL-v_hartree-1_24.cube')

#Pt_I = load_cube.CUBE('//work/common/hxin_lab/ishanj13/solar_cells/cp2k/metals/I_lc/Pt/111/atop/I_Pt-ELEC_POTENTIAL-v_hartree-1_5.cube')

#DATA = Clean.data
#np.savetxt('DATA.txt',np.sum(np.sum(DATA,axis=0),axis=0))

y_axis =  np.sum(np.sum(DATA,axis=0),axis=0)/Clean.NX/Clean.NY

z_len = 29.3727                     # this is the size of z coordinate
x = np.linspace(0,z_len,Clean.NZ)
plt.plot(x, y_axis*27.211, 'k')

Fermi_y = 0.02972356791997*27.211* np.ones(100)   # Fermi level is y = 0.134731

Fermi_x = np.linspace(0,25,100)
plt.plot(Fermi_x, Fermi_y)


#plt.plot(np.sum(np.sum(DATA,axis=0),axis=0))

plt.xlabel('z direction (Angstrom)')
plt.ylabel('Electron Potential (eV)')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)

plt.show()
plt.savefig('Electron_Potential_Pt-I (atop).pdf')
