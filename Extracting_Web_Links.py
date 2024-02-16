from duckduckgo_search import DDGS


# result from DDGS contains - title, href, body;
def get_relevant_links(query):
    search = DDGS()
    answers = {}
    results = search.text(keywords=query, max_results=10)
    print(results)
    print("\n")
    for r in results:
        link = r['href']
        if not any(link.endswith(ext) for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx']) and link.startswith(
                "https://"):
            if query not in answers:
                answers[query] = []
            answers[query].append(link)
    return answers


def get_links():
    queries = [
        "Identify the industry in which Canoo operates, along with its size, growth rate, trends, and key players",
        "Analyze Canoo's main competitors, including their market share, products or services offered, pricing strategies, and marketing efforts",
        "Identify key trends in the market, including changes in consumer behavior, technological advancements, and shifts in the competitive landscape",
        "Gather information on Canoo's financial performance, including its revenue, profit margins, return on  investment, and expense structure"
    ]

    links1 = []

    for query1 in queries:
        links1.append(get_relevant_links(query1))

    return links1


def save_links_to_file(links, filename):
    with open(filename, 'w') as f:
        for link_dict in links:
            for query, link_list in link_dict.items():
                f.write(f"{query}\n")
                for link in link_list:
                    f.write(f"{link}\n")


def main():
    links1 = get_links()
    save_links_to_file(links1, 'Web_Links_for_Canoo_4_queries_Analysis.txt')


if __name__ == "__main__":
    main()

