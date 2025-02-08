from sentence_transformers import SentenceTransformer, util
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def generate_rating(user_query: str, url: str) -> dict:
    # Step 1 - Function to extract text from the URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive'
    }

    try:
        # Send request to the URL
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')  # Extract paragraphs
        content = ' '.join([para.get_text() for para in paragraphs])  # Join text from paragraphs
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error occurred: {err}"

    # Step 2 - Domain trust score (static for now, replace with actual logic)
    domain_trust = 60

    # Step 3 - Content Relevance
    model = SentenceTransformer('all-MiniLM-L6-v2')
    similarity_score = util.pytorch_cos_sim(model.encode(user_query), model.encode(content)).item() * 100

    # Step 4 - Fact-Checking (Placeholder function, implement actual logic)
    fast_check_score = fact_check_claim(content)

    # Step 5 - Sentiment Analysis
    sentiment_pipeline = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment")
    sentiment_result = sentiment_pipeline(content[:512])[0]
    bias_score = 100 if sentiment_result["label"] == "POSITIVE" else 50 if sentiment_result["label"] == "NEUTRAL" else 30

    # Step 6 - Citation Check (Placeholder, replace with actual logic)
    citation_count = check_google_scholar(url)  # Implement actual citation check
    citation_score = min(citation_count * 10, 100)

    # Step 7 - Final Score Calculation
    final_score = (
        (domain_trust * 0.3) +
        (similarity_score * 0.3) +
        (fast_check_score * 0.2) +
        (bias_score * 0.1) +
        (citation_score * 0.1)
    )

    return {
        "Domain Trust": domain_trust,
        "Content Relevance": similarity_score,
        "Fact-Check Score": fast_check_score,
        "Bias Score": bias_score,
        "Citation Score": citation_score,
        "Final Validity Score": final_score
    }

def fact_check_claim(claim: str) -> int:
    API_URL = f"https://toolbox.google.com/factcheck/api/v1/claimsearch?query={claim[:200]}"
    try:
      response = requests.get(API_URL)
      data = response.json()

      if "claims" in data and data["claims"]:
        return 80
      return 40
    except:
      return 50

def check_google_scholar (url: str) -> int:
  serpapi_key = "YOUR_KEY_HERE"
  params = {"q": url, "engine": "google_scholar","api_key": serpapi_key}
  try:
    response = requests.get("https://serpapi.com/search", params=params)
    data = reponse.json()
    return len(data.get("organic_results",[]))
  except:
    return 0


user_query = "i just had coffee, how long after until I brush my teeth? "
url_to_check = "https://www.generaldentistdurham.com/2022/07/14/should-you-brush-teeth-before-or-after-coffee/"

result = generate_rating(user_query, url_to_check)
print(result)