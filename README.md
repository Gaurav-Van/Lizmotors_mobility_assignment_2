# <b>Lizmotors Mobility Assignment_2</b>
This is the Repository containing the material required for the 2nd assignment of Lizmotors mobility for the role of AI/ML Engineering Intern. <hr>

## <b>Initial Understanding of the Assignment</b>
Building a Basic RAG (Retrieval-Augmented-Generation) or Vector Search System for an EV based Company called Canoo. 

We can Define RAG in simple terms: When connecting a Language Model (LLM) to a datastore, we augment it by adding extra data to a vector database (DB). The prompt is meticulously crafted to enable the LLM to not only consider the original input but also consult the vector DB for the most relevant response.

Both the data and the prompt are transformed into vector embeddings, allowing them to be matched using vector search techniques. This approach serves two purposes: it mitigates hallucinations and reduces the risk of the LLM generating responses from out-of-source information.

In summary, this method defines a Retrieval-Augmented Generation (RAG) system, which combines the strengths of vector-based retrieval and language generation to enhance the quality and relevance of responses.

#### Basic RAG / Vector Search Architecture

```
Data Extraction -> Chunks -> Vector Embeddings -> Vector Database 

Retrieval: User Query -> Vector Embeddings -> Search (Vector similarity search) from Vector Database -> Result (summarized, keywords, etc..)

Result from Retrieval stage is then synthesized with the LLM
```
![image](https://github.com/Gaurav-Van/Lizmotors_mobility_assignment_2/assets/50765800/344a65c4-1cbf-450c-8dda-7d234c38a47c)

![image](https://github.com/Gaurav-Van/Lizmotors_mobility_assignment_2/assets/50765800/87812702-bd55-44f0-bff8-fe5f6c8490e0)

### Task Given: Extraction Part of RAG Architecture
```
1) Based on 4 queries, find relevant web links of each query using Internet search APIs
2) Scrap relevant data from those web links and store as CSV files
   
Based on similarity or disimilarity between the data of all 4 queries the decision to make single or 4 CSV will be decided. 
```
<hr> 
