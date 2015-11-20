# Python Markov Chain Generator
Just another Markov chain generator written in Python.

# Usage
`python main.py filenames [filenames ...]`

# Planned Fixes and Features

* Currently, text consumption is very naïve: i.e., we only split up strings based on whitespace. I think this could cause problems for texts with lots of whitespace. I would like to update the tokenization functionality to take this into account; or, better yet, to make tokenization incredibly flexible and customizable.

* The way `order` is used in the code is a bit misleading. Because of the nature of array indexing beginning at zero and slicing and whatnot, the true order of the Markov generator (that is, the n-grams it produces) are really `order - 1` n-grams. So, if you wanted 3-grams, `order` should be set to 4 (because when the function to get a list of words from a file returns, the length of the list is `order`, not `order - 1`).

* Changing the order of the generator from the command line would be pretty neat, although really order 3 seems to work the best.
