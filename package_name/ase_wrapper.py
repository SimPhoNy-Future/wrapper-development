import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms

# TODO: - Add function to retrieve atom properties from UUID
#       - Visualize UUID with native ASE GUI
#       - Integrate data properties with CUDS
#       - For adding a UUID to an atom objet, a way to add UUID to the whole atom (group) as well as individual atoms in molecule is needed


class ASEWrapper:

    '''A wrapper for UUIDs and Atoms object in ASE.

    Parameters:
       add_uuid : adds UUID to an Atoms object
       print_uuid: prints UUID with atoms index and symbol
       view_uuid: visualize atoms and corresponding UUID

       '''
    def __init__(self):
        self._mapper = {}
        self._mapped_atoms = 0

    def add_uuid(self, atoms, uuids):

        """Add the predefined UUIDs as properties to the atoms object's info dictionary"""
        atoms.info['uuids'] = uuids

    def print_uuid(self, atoms):

        """Print UUID as well as corresponding symbol and atom index of Atoms object """

        molecule_symbol = atoms.get_chemical_formula()
        print(f"Group: Symbol = {molecule_symbol}")
        for i, atom in enumerate(atoms):
            atom_symbol = atom.symbol
            atom_uuid = atoms.info['uuids'][i]
            print(f"Atom {i}: Symbol = {atom_symbol}, UUID = {atom_uuid}")

    def view_uuid(self, atoms):

        """View Atoms object and corresponding UUID with ASE plot_atoms"""

        # Create a Matplotlib figure and axis
        fig, ax = plt.subplots()

        # Plot the atoms
        plot_atoms(atoms, ax, radii=0.3)

        # Extract UUIDs from the info dictionary and add them as annotations
        uuids = atoms.info.get('uuids', [])
        for i, atom in enumerate(atoms):
            atom_position = atom.position
            atom_uuid = uuids[i] if i < len(uuids) else ''
            annotation_text = f"UUID: {atom_uuid}"  # Customize the annotation as needed
            ax.text(atom_position[0], atom_position[1], annotation_text, fontsize=8, ha='center', va='center')

        # Show the plot
        plt.show()