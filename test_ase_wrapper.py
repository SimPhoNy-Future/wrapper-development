from package_name.ase_wrapper import ASEWrapper
from ase import Atoms

'''Simple example of working with UIDs and ASE, where you can assign a UUID to 
an Atom object, print UUID and then visualize it'''



atoms = Atoms('H2', positions=[(0, 0, 0), (1, 1, 1)])
uuids = ['290ad2a7-2fcb-4da3-8669-a43493b3f915', '290ad2a7-2fcb-4da3-8669-a43493b3f916']

# OB 06/09/23: This all has the wrong naming, but I'm committing what I've done today

ase_wrapper = ASEWrapper()

ase_wrapper.add_uuid(atoms, uuids)

ase_wrapper.print_uuid(atoms)

ase_wrapper.view_uuid(atoms)

