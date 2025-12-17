## create your Rag based ai teaching assitence follow these steps 

# step-1 
first paste your vedios in vedios folder

# step-2
 convert your vedios into audio by using convert_vedio_into_audio.py and placed them in speech folder

# step-3

convert your speech into json chunks by using voice_into_text and placed them in output

# step-4

convert these json chunks into embedding and make the dataframe of these embeddings and safe it mydata.joblib using the convert_into_embeddig.py

 # step-5

now use these mydata.joblib and check the cosine similarity and take top 5 data as per query and send them to llm model now llm model gives you answer .All these steps done in 
# check_cosine_similarity.py

## we now preprocess the model to increase it accuracy we join chunks together from each json for make it less like 5-5 chunks from each json 

now we store tese chunks in newChunks and all things gone same from step-4 to step - 5

## conclude the project