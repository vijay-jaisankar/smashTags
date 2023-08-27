"""
    @note This file contains the API routes to inference clarif.ai workflows.
    Functionalities
        - Base route to check if the infra is up.
"""
from configparser import ConfigParser
from flask import Flask, request
from clarifai_setup import get_data_objects
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2


# Set up ConfigParser
config = ConfigParser()
config.read("settings.ini")


app = Flask(__name__)

"""
    Base API Route
        - Checks if the site is up
        - Text to hashtags
"""
@app.route("/", methods = ["GET"])
def index():
    output_dict = {
        "status" : "up"
    }
    return output_dict


"""
    Text to Hashtags generator
    Calls `llama2-7b-chat`
"""
@app.route("/api/text/", methods = ["POST"])
def get_hashtags_for_text():
    input_json = request.get_json()
    input_text = input_json["input_text"]
    print(f"Input text received: {input_text}")

    # Initialise auth objects
    metadata, user_data_object = get_data_objects(
        token_value = str(config['TEXT']['pat']),
        user_id = str(config['TEXT']['user_id']),
        app_id = str(config['TEXT']['app_id']))
    
    PAT = 'sample_pat_here'
    USER_ID = 'meta'
    APP_ID = 'Llama-2'
    MODEL_ID = 'llama2-7b-chat'
    MODEL_VERSION_ID = 'e52af5d6bc22445aa7a6761f327f7129'

    metadata = (('authorization', 'Key ' + PAT),)

    user_data_object = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)
    
    # Call the model
    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    # Create the prompt
    prompt = f"Generate hashtags based on keywords included in the given text which are relevant and can maximize my social media reach. Do not include any filler text and separate the hashtags by commas. \n {input_text}"

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=user_data_object,  
            # model_id=str(config['TEXT']['model_id']),
            # version_id=str(config['TEXT']['version_id']),
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            raw=prompt
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )

    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        raise Exception(f"Post model outputs failed, status: {post_model_outputs_response.status.description}")

    hashtag_output = post_model_outputs_response.outputs[0]

    prompt = f"Generate a one-word topic for the given text. Do not add any content and please only output only one word. \n {input_text}"

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=user_data_object,  
            # model_id=str(config['TEXT']['model_id']),
            # version_id=str(config['TEXT']['version_id']),
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            raw=prompt
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )

    topic_output = post_model_outputs_response.outputs[0]
    output_dict = {
        "hashtags" : hashtag_output.data.text.raw,
        "topic" : topic_output.data.text.raw
    }

    return output_dict



# Launch the app
if __name__ == "__main__":
    app.run(debug = True)