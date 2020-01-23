# Maybe some copyright stuff goes here

# TODO: Import the python connection to the engine

from osp.core.session import SimWrapperSession


class SomeSimulationSession(SimWrapperSession):
    """
    Session class for some engine.
    """

    def __init__(self, engine=None, **kwargs):
        # TODO: Instantiate or connect the engine
        super().__init__(engine, **kwargs)

    def __str__(self):
        # TODO: Define the output of str(SomeSimulationSession())
        return "Some Wrapper Session"

    # OVERRIDE
    def _run(self, root_cuds_object):
        """Call the run command of the engine."""
        # TODO: call the run method in the engine

    # OVERRIDE
    def _load_from_backend(self, uids, expired=None):
        """Loads the cuds object from the simulation engine"""
        # TODO load cuds objects from the backend

    # OVERRIDE
    def _apply_added(self, root_obj, buffer):
        """Adds the added cuds to the engine."""
        # TODO: What should happen in the engine
        # when the user adds a certain cuds?
        # The given buffer contains all the added CUDS object in a dictionary

    # OVERRIDE
    def _apply_updated(self, root_obj, buffer):
        """Updates the updated cuds in the engine."""
        # TODO: What should happen in the engine
        # when the user updates a certain cuds?
        # The given buffer contains all the updated CUDS object in a dictionary

    # OVERRIDE
    def _apply_deleted(self, root_obj, buffer):
        """Deletes the deleted cuds from the engine."""
        # TODO: What should happen in the engine
        # when the user removes a certain cuds?
        # The given buffer contains all the deleted CUDS object in a dictionary
