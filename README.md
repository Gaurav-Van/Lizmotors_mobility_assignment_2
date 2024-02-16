# <b>Lizmotors Mobility Assignment_2</b>
This is the Repository containing the material required for the 2nd assignment of Lizmotors mobility for the role of AI/ML Engineering Intern. <hr>

## <b>Initial Understanding of the Assignment</b>
Building a Basic RAG (Retrieval-Augmented-Generation) or Vector Search System for an EV based Company called Canoo. We can Define RAG in simple terms: When connecting a Language Model (LLM) to a datastore, we augment it by adding extra data to a vector database (DB). The prompt is meticulously crafted to enable the LLM to not only consider the original input but also consult the vector DB for the most relevant response.

#### Basic RAG / Vector Search Architecture

```
Data Extraction -> Chunks -> Vector Embeddings -> Vector Database 

Retrieval: User Query -> Vector Embeddings -> Search (Vector similarity search) from Vector Database -> Result (summarized, keywords, etc..)

Result from Retrieval stage is then synthesized with the LLM
```
![image](https://github.com/Gaurav-Van/Lizmotors_mobility_assignment_2/assets/50765800/344a65c4-1cbf-450c-8dda-7d234c38a47c)

### Task Given: Extraction Part of RAG Architecture
```
1) Based on 4 queries, find relevant web links of each query using Internet search APIs
2) Scrap relevant data from those web links and store as CSV files
   
Based on similarity or disimilarity between the data of all 4 queries the decision to make single or 4 CSV will be decided. 
```
<hr> 

## My Approach 
1) Place those 4 queries in a List
![image](https://github.com/Gaurav-Van/Lizmotors_mobility_assignment_2/assets/50765800/9744791f-96ff-4cf2-b447-0b50a7152be3)

2) For queries within the list, extract 10 web links each using duckduckgo API and store them in a text file consisting of links and their respective query

3) Read the Text file and extract the non_link and link part in sepeate lists. Topic = non_link part or the Queries 

4) Scrape each link using the combination of Selenium and BeautifulSoup. I am extracting their p and span tag.

5) Then I am using GEMINI API to extract relevant information on the basis of respective Topic from scraped text in clean and clear format. Helps in reducing the task of data cleaning.

6) Storing Data in a CSV with following Structure. Information Column Data is in Json Format <br>
   | Query / Topic | url | Information |
   | ------------- | --  | ----------- |

**Note**: _csv files contains extracted Information based on respective Query on each and every respevtive url so some NaN results are expected_
<hr>

### Dependencies
 - duckduckgo API
 - csv
 - google_api_core.exceptions
 - google.generativeai
 - genai
 - BeautifulSouo
 - Selenium

