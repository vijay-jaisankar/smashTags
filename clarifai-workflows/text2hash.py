
######################################################################################################
# In this section, we set the user authentication, user and app ID, model details, and the URL of 
# the text we want as an input. Change these strings to run your own example.
######################################################################################################

# Your PAT (Personal Access Token) can be found in the portal under Authentification
PAT = 'PAT'
# Specify the correct user_id/app_id pairings
# Since you're making inferences outside your app's scope
USER_ID = 'meta'
APP_ID = 'Llama-2'
# Change these to whatever model and text URL you want to use
MODEL_ID = 'llama2-7b-chat'
MODEL_VERSION_ID = 'e52af5d6bc22445aa7a6761f327f7129'
# text = 'Generate hashtags for the following text: \nWikipedia is an encyclopedia written by volunteers to help people gain useful knowledge. Our encyclopedia is pretty comprehensive, but that does not mean we would cover every single topic that exists. Therefore, Wikipedia is not a social media, a place for promotion or advocacy, nor a place to announce new unpublished theories. Information from websites, blogs, forum posts, social media, wikis including Wikipedia, and self-published sources are generally not suitable for Wikipedia.In another way, our job is to summarize such high-quality and published sources from other places, in the form of Wikipedia articles. That really is all we do! Do make sure that anything you write on Wikipedia is based only on such sources.Sounds easy? Not quite. Many of the notable topics have already been written by people in the past, and the fact of the matter is, most new articles nowadays are written about fairly obscure subjects. That can make distinguishing topics that are suitable or not suitable on Wikipedia very difficult, and are often flashpoints for contentious disputes. No amount of editing can overcome a lack of notability of a topic. More than 200 articles are typically deleted from the English Wikipedia every day; most are deleted for this very reason. We dont want you to waste all of your effort just for it to be marked for deletion!Please avoid making an article that you have a conflict of interest in, meaning that you have a close connection to the subject as an employee, family member, friend, etc or your financial and other relationships. This is a very strict policy on Wikipedia. Conflicts of interest undermines public confidence and risks causing public embarrassment to the individuals and companies being promoted. In practice, articles created out of a conflict of interest are usually rejected/deleted on sight. (Further information: Help:Your first article § Are you closely connected to the article topic?)If you want to succeed at this endeavor, you should gain ample of experience beforehand and get a feel of what a suitable topic to write on Wikipedia would be. In fact, because the stakes are lower, this is a perfect opportunity to hone your editing skills! Do take a tour through the tutorial, ask around at the Teahouse, or read Wikipedia:Article development. Dont feel ashamed if you couldnt find a new topic to write about Wikipedia: plenty of distinguished editors here have only edited existing articles, but they are the one that turned the rubbish articles into great ones.Before creating an article, try to make sure there is not already an article on the same topic. If you dont find a match, perhaps try using a slightly different or broader search term'
text = """
Generate hashtags based on keywords included in the given text which are relevant and can maximize my social media reach:\n
India, a diverse and vibrant nation in South Asia, is a tapestry of cultures, traditions, and landscapes. With a rich history spanning millennia, it boasts iconic landmarks like the Taj Mahal and spiritual sites like Varanasi. Home to over 1.3 billion people, India's society encapsulates a blend of languages, religions, and lifestyles. Its cuisine, from spicy curries to delicate sweets, is renowned worldwide. The country's rapid technological advancement contrasts with rural life where age-old practices endure. Festivals like Diwali and Holi splash streets with color and light, reflecting the nation's celebratory spirit. India's complexities and contrasts make it a captivating and enigmatic global destination.

"""
############################################################################
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE TO RUN THIS EXAMPLE
############################################################################

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)

metadata = (('authorization', 'Key ' + PAT),)

userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        user_app_id=userDataObject,  # The userDataObject is created in the overview and is required when using a PAT
        model_id=MODEL_ID,
        version_id=MODEL_VERSION_ID,  # This is optional. Defaults to the latest model version
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    text=resources_pb2.Text(
                        raw=text
                    )
                )
            )
        ]
    ),
    metadata=metadata
)

if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    print(post_model_outputs_response.status)
    raise Exception(f"Post model outputs failed, status: {post_model_outputs_response.status.description}")

# Since we have one input, one output will exist here
output = post_model_outputs_response.outputs[0]

# print("Completion:\n")
print(output.data.text.raw)

# if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
#     print(post_model_outputs_response.status)
#     raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

# # Since we have one input, one output will exist here
# output = post_model_outputs_response.outputs[0]

# print("Predicted concepts:")
# for concept in output.data.concepts:
#     print("%s %.2f" % (concept.name, concept.value))

# # Uncomment this line to print the full Response JSON
# #print(output)

