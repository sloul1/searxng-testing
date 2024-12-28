import os
from dotenv import load_dotenv

import concurrent.futures
import time
from requests import get as requests_get

# Load the .env file
load_dotenv()

def search(query):
    url = os.getenv("SEARCH_ENGINE_URL").format(query)

    response = requests_get(url)
    
    if response.status_code == 200:
        return response.text
    
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    start_time = time.time()
    
    # Search queries
    search_queries = [
        "python",
        "machine learning",
        "deep learning",
        "natural language processing"
    ]
    
    num_threads = 2
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for _ in range(25):
            for query in search_queries:
                future = executor.submit(search, query)
                futures.append(future)
                #time.sleep(0.1)  # Uncomment to add delay (in seconds) between searches
        
        pending_requests = len(futures)
        requests_num = 0
        
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result is not None:
                elapsed_time = time.time() - start_time
                requests_num += 1
                pending_requests -= 1
                print(f"Search query: {query}")
                print(result[:200])
                print("\n")
                
                print(elapsed_time)
                print(requests_num)
        
        if pending_requests == 0 and requests_num == len(futures):
            elapsed_time = time.time() - start_time
            print(f"\nSearch finished in {elapsed_time:.2f} seconds")
    
    return

if __name__ == "__main__":
    main()