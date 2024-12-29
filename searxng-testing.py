import os
from dotenv import load_dotenv
import requests
import time
import random

# Load the .env file
load_dotenv()

# Set the URL of the search engine from .env file
url = os.getenv("SEARCH_ENGINE_URL")

# Set the search query
search_queries = ["test query 1", "test query 2", "test query 3"]

# Set the number of iterations
num_iterations = 5

# Set the delay between requests in seconds
delay = 1.00

# Start the timer
start_time = time.time()

# Request number
requests_num = 0

# Initialize a variable to track the number of pending requests
pending_requests = num_iterations

# Loop through the search queries and send requests
for i in range(num_iterations):
    # Elapsed time
    elapsed_time =  time.time() - start_time 
    # Choose a random search query
    
    query = random.choice(search_queries)
    
    # Requests
    pending_requests -= 1
    requests_num += 1

    # Send a GET request to the search engine
    response = requests.get(url, params={"q": query})

    # Check the status code of the response
    if response.status_code == 200:
        # Print the search results
        print(f"Search query: {query}")
        print(response.text)
        # Print the elapsed time
        print(f"Elapsed time: {elapsed_time} seconds")
        # Print the number of pending requests
        print(f"Requests: {requests_num}")
        # Print the number of pending requests
        print(f"Pending requests: {pending_requests}")
    

    else:
        # Print an error message
        print(f"Error: {response.status_code}")

    # Wait for the specified delay
    time.sleep(delay)
    if elapsed_time >= 10:
        break
    # Wait for number of requests
    #else:
    #    requests_num == 20
    #    break