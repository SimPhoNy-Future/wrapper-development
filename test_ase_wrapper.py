from package_name.ase_wrapper import ASEWrapper
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize.bfgs import BFGS

'''Simple example of working with UUIDs and ASE, where you can assign a UUID to 
an Atom objects, print UUID and then visualize it'''

#Create a H-H molecule with ASE and run an optimisation

atoms = Atoms('H2', positions=[(0, 0, 0), (1, 1, 1)])

atoms.set_calculator(EMT())

opt = BFGS(atoms)
opt.run(fmax=0.01)


# Create a H-H individual with SimPhoNy

from simphony_osp.tools import export_file, import_file, pretty_print, search
from simphony_osp.tools.search import sparql
from simphony_osp.tools.pico import install, namespaces, packages, uninstall
from simphony_osp.namespaces import miso


install('../miso/miso.yml')

HH = miso.Molecule()
H1 = miso.H()
H2 = miso.H()

HH[miso.hasPart] = {H1, H2}

# Pretty_print and check ontology individuals and identifiers

pretty_print(HH)

# Get the identifiers and store them as variables

uuid_H1 = ASEWrapper.get_identifier(H1)
uuid_H2 = ASEWrapper.get_identifier(H2)
uuids = [uuid_H1, uuid_H2]

#Add the indentifiers to the ASE atoms (H-H) object above

ase_wrapper = ASEWrapper()
ase_wrapper.add_uuid(atoms, uuids)

#print the new uuids of the atoms and check whether they correspond to the above

ase_wrapper.print_uuid(atoms)

#Visualise the uuids and correspondning atoms

ase_wrapper.view_uuid(atoms)


# View details from the optimisation simulation through the uuid

details = ASEWrapper.get_simulation_details(atoms,opt,uuid_H1)
