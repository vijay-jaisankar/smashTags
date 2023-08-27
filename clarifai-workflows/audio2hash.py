USER_ID = 'akshatgarg'
# Your PAT (Personal Access Token) can be found in the portal under Authentification
PAT = 'PAT'
APP_ID = 'audio-to-text'
# Change these to make your own predictions
WORKFLOW_ID = 'workflow-a34cd2'
AUDIO_FILE_LOCATION = './sample-inputs/noise_cleaned.mpga'

##########################################################################
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE TO RUN THIS EXAMPLE
##########################################################################

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)

metadata = (('authorization', 'Key ' + PAT),)

userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID) # The userDataObject is required when using a PAT

with open(AUDIO_FILE_LOCATION, "rb") as f:
    file_bytes = f.read()

print(len(file_bytes))

post_workflow_results_response = stub.PostWorkflowResults(
    service_pb2.PostWorkflowResultsRequest(
        user_app_id=userDataObject,  
        workflow_id=WORKFLOW_ID,
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    audio=resources_pb2.Audio(
                        base64=file_bytes
                    )
                )
            )
        ]
    ),
    metadata=metadata
)
if post_workflow_results_response.status.code != status_code_pb2.SUCCESS:
    print(post_workflow_results_response.status)
    # print(post_workflow_results_response.status)
    raise Exception("Post workflow results failed, status: " + post_workflow_results_response.status.description)


# We'll get one WorkflowResult for each input we used above. Because of one input, we have here one WorkflowResult
results = post_workflow_results_response.results[0]

# Each model we have in the workflow will produce its output
count = 0
for output in results.outputs:    
    model = output.model    
    count +=1
    # print("Output for the model: `%s`" % model.id)   
    if count == 3:
        for concept in output.data.concepts:        
            print("\t%s %.2f" % (concept.name, concept.value)) 
    print(output.data.text.raw)     

# Uncomment this line to print the full Response JSON
#print(results)