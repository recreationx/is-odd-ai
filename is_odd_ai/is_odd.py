import requests

class OddChecker:
    def __init__(self, api_key: str):
        """
        Args:
            api_key (str): OpenAI API key
        """
        self.api_key = api_key
        self.endpoint = "https://api.openai.com/v1/chat/completions"

    def is_odd(self, n: int | float) -> bool:
        """
        Args:
            n (int): Number to check
        Returns:
            bool: Whether the number is odd
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": f"Is {n} odd or even?"}],
            "temperature": 0.7
        }
        try:
            response = requests.post(self.endpoint, headers=headers, json=data)
            if response.status_code == 200:
                result = response.json()["choices"][0]["message"]["content"]
                if "odd" in result.lower():
                    return True
                elif "even" in result.lower():
                    return False
                else:
                    raise ValueError("Unable to determine if number is odd or even.")
            else:
                print(response)
        except Exception as e:
            print(f"Error querying OpenAI: {e}")