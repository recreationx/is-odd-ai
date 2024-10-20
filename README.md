# is-odd-ai
A project inspired by the npm version [`is-odd-ai`](https://github.com/rhettlunn/is-odd-ai)

`is-odd-ai` uses OpenAI's GPT-4o-mini model to determine if a number is odd or even. AI to the moon 🚀🚀🌝!

## Installation
To install `is-odd-ai`, use pip:
```
pip install is-odd-ai
```

## Usage
To use `is-odd-ai`, you will need an OpenAI key.

Here is an example.
```py
from is_odd_ai import OddChecker

odd_checker = OddChecker("api key here")
odd_checker.is_odd(5) # True
odd_checker.is_odd(6) # False
odd_checker.is_odd("abc") # Hopefully a ValueError. AI to the moon!
```

## Contributing
Be part of this project! Open to contributions.

## License
MIT License.