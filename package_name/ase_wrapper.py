import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms

import sys
from functools import reduce
from operator import add
from typing import Iterable, Optional, Set, Union

from simphony_osp.namespaces import owl
from simphony_osp.ontology.attribute import OntologyAttribute
from simphony_osp.ontology.composition import Composition
from simphony_osp.ontology.entity import OntologyEntity
from simphony_osp.ontology.individual import OntologyIndividual
from simphony_osp.ontology.oclass import OntologyClass
from simphony_osp.ontology.relationship import OntologyRelationship
from simphony_osp.ontology.restriction import Restriction


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

    # def get_uuid_label(entity: OntologyEntity) -> Optional[str]:
    #     """
    #     Get the UUID label from an ontology entity if it has one assigned.
    #
    #     Args:
    #         entity (OntologyEntity): The ontology entity to extract the UUID label from.
    #
    #     Returns:
    #         Optional[str]: The UUID label if present, otherwise None.
    #     """
    #     # Check if the entity has a label property representing the UUID
    #     uuid_label = entity.label
    #     if uuid_label is not None:
    #         return uuid_label
    #     else:
    #         return None

    from typing import Optional
    from simphony_osp.ontology.entity import OntologyEntity
    from simphony_osp.ontology.individual import OntologyIndividual

    def get_identifier(entity: OntologyEntity) -> Optional[str]:
        """
        Get the identifier (UUID) for an ontology entity if it has one assigned.

        Args:
            entity (OntologyEntity): The ontology entity to extract the identifier from.

        Returns:
            Optional[str]: The identifier (UUID) if present, otherwise None.
        """
        # Check if the entity is an individual and has an identifier
        if isinstance(entity, OntologyIndividual):
            return entity.uid
        else:
            return None


    def get_simulation_details(atoms, opt, uuid):

        """ TODO: - this is pretty basic and needs refining
                  - how is this different to a SPARQL query of the CUDS properties
                  if you add the simulation data to a CUDS? """
        
        # Find the index of the atom with the specified UUID
        index = atoms.info['uuids'].index(uuid)

        details = {
            'forces': atoms.get_forces()[index],
            'energy': atoms.get_potential_energy(),
            'time_step': opt.get_number_of_steps(),
        }

        # Print the simulation details
        print(f"Simulation Details for Atom with UUID '{uuid}':")
        print(f"Forces: {details['forces']} eV/Ã")
        print(f"Energy: {details['energy']} eV")
        print(f"Time Step: {details['time_step']}")






