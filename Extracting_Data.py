import csv

import google.api_core.exceptions
import google.generativeai as genai
from bs4 import BeautifulSoup
from selenium import webdriver


def extract_text(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tags = soup.find_all(['p', 'span'])
    text = ' '.join([tag.get_text().strip() for tag in tags])
    driver.quit()

    return text


def cleaned_and_structured_extraction(topic, links, text):
    genai.configure(api_key="YOUR_API_KEY")

    # Set up the model
    generation_config = {
        "temperature": 0.8,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    prompt_parts = [

        f"""
            You have successfully scraped text from a website using Selenium and Beautiful Soup. This text is stored in a variable named 'Text'. 
            Your task is to analyze each element of the 'Text' variable and extract information that is relevant to a specific topic. The topic for this analysis is: {topic}. 
            Please note the following guidelines for your analysis:
            - Only consider the information present in the 'Text' variable. Do not use any external sources or databases for this analysis.
            - Focus your analysis on the given topic. Include any additional information from the 'Text' variable that pertains to this topic.
            - The every output of your analysis should be presented in JSON Format and not any other format 
            - If you cannot find any thing related to topic then just write "NaN", Do not write anything else just "NaN"
            
            Below is the text for your analysis:
    
            Text: {text}
            """
    ]

    try:
        response = model.generate_content(prompt_parts)
        with open("Canoo_Data_Analysis.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['Query / Topic ', 'url', 'Information'])
            writer.writerow([topic, links, response.text])
    except ValueError as e:
        print(e)
    except google.api_core.exceptions.InternalServerError:
        print("An internal error occurred, Skipping this one")


def main():
    with open('Web_Links_for_Canoo_4_queries_Analysis.txt', 'r') as file:
        lines = file.read()

    lines = lines.split('\n')
    non_link_texts = []
    link_texts = []

    for line in lines:
        if line.startswith('http'):
            link_texts.append(line)
        else:
            non_link_texts.append(line)

    flag = 0
    j = 0
    for link in link_texts:
        text = extract_text(link)
        cleaned_and_structured_extraction(non_link_texts[j], link_texts[flag], text)
        flag = flag + 1
        if flag % 10 == 0:
            j = j + 1
        print(f"{j} Done\n")


if __name__ == "__main__":
    main()
