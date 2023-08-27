"""
    @note This file contains utility functions to load credentials and set up clarif.ai
    List of functionalities
        - Get authentication objects
"""

from clarifai_grpc.grpc.api import resources_pb2

"""
    Get data objects
        Constructs and returns the metadata tuple and userdata objects
    @note Could be scoped out in the future
"""
def get_data_objects(token_value, user_id, app_id):
    # Construct metadata tuple
    metadata = (
        ("authorization", "Key " + token_value),
    )

    # Construct user data object
    user_data_object = resources_pb2.UserAppIDSet(
        user_id = user_id,
        app_id = app_id
    )

    return metadata, user_data_object