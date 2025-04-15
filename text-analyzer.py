<think>
Okay, I need to write a Python script that counts words, sentences, and characters in a given text. Let me think about how to approach each part.

First, for characters, that's straightforward. The length of the string should give the number of characters, including spaces and punctuation. So len(text) would work.

Next, words. Usually, splitting the text into words using split() method. But wait, split() by default splits on any whitespace, so that's okay for spaces, tabs, newlines. But maybe the text has hyphenated words? Like "well-known"? Hmm, the problem doesn't specify, so maybe just split on whitespace and count each element as a word. So words = text.split(), then len(words).

Sentences are trickier. Sentences usually end with . ! or ?. So I can split the text on those punctuation marks. But need to consider cases where there might be punctuation followed by spaces or different cases. For example, "Hello! How are you? I'm fine." Splitting on [.!?] but also need to handle if there are multiple punctuation or spaces after. Maybe split on [!.?], then filter out any empty strings. So sentences = [s for s in re.split(r'[.!?]', text) if s.strip() != ''] and then the length of that.

Wait, but need to use regular expressions for splitting. So I should import re. So the steps would be:

1. Import re.

Then, for the given text, process each part:

Characters: len(text)

Words: len(text.split())

Sentences: split using re.split(r'[.!?]', text), then count non-empty stripped strings.

Wait, but what about sentences that end with other punctuation, like commas? Probably, the standard approach is to split on .!? and then check if the sentence is non-empty. So that's the way to go.

Putting it all together:

The code structure would be:

import re

def count_text(text):
    chars = len(text)
    words = len(text.split())
    sentences = len([s for s in re.split(r'[.!?]', text) if s.strip()])
    return chars, words, sentences

But the task says to write a script, not a function. Oh right, the user wants a Python script. So maybe read from standard input, or perhaps the text is provided as a variable? Wait, the problem says "given text" but doesn't specify input method. Since the user just wants the code, perhaps the code should take input from the user via input() or perhaps read from a variable. Hmm, maybe the standard way is to read from a variable, but perhaps the user expects to have the code prompt for input.

Alternatively, maybe the script reads a string from the user. Let me think of a standard approach. Let's see, the code needs to be a script. So perhaps:

text = input("Enter text: ")

But maybe the user expects to process any given text, so perhaps the code should take the text as input, process it, and output the counts.

Wait, the output should return the code, so the code must be a script that does the counting. Let me write it step by step.

The code steps:

Read the text. Maybe via input(). But if the user is providing the text, perhaps the code should be written with a sample input? No, the code needs to be general. So the code should:

Read the text from the user, process, then output the counts.

Wait, but the problem says "given text" but doesn't specify how. Since the code is a script, perhaps it's better to read from stdin. So:

text = input().strip()

But maybe the input could have multiple lines. Hmm, but input() reads a line. Alternatively, read all lines until EOF. But maybe the problem expects a simple approach. Let's assume that the text is provided via input().

So:

text = input("Enter the text: ")

Then compute the three counts.

Then, print them. Wait, but the task says "Return only the code." and the output should be the code. The user didn't mention the output format of the script. The problem says "counts the number of words, sentences, and characters in a given text." So the code should compute and return those numbers, but as a script, perhaps it should print them. But the user's instruction says "Output: Return only the code." So the code itself should be the script that does the counting.

Putting it all together:

import re

text = input().strip()

chars = len(text)
words = len(text.split())
sentences = len([s for s in re.split(r'[.!?]', text) if s.strip()])

print(f"Characters: {chars}")
print(f"Words: {words}")
print(f"Sentences: {sentences}")

Wait, but maybe the problem expects the counts as output, but in what format? The user's task says the script should count and presumably output those numbers. Since the user wants the code only, and the code must be complete, this should be acceptable.

Wait but splitting sentences with re.split(r'[.!?]', text) might split on each occurrence. For example, if there are two periods in a row, like "Hello..", then split would create an entry for each. But the list comprehension checks if the split part is non-empty after stripping. Hmm, maybe better to split on r'([.!?])' and then check? Or maybe better to split on any of those as delimiters. Alternatively, perhaps use a regex that matches the sentence endings and split on that. Maybe the current approach works for most cases.

Wait, let's test with an example. Suppose text is "Hello! How are you? I'm fine. Thanks."

Split on [.!?], the split would be ["Hello", " How are you", " I'm fine", " Thanks", ""] ?

Wait, no. Wait, the split includes all elements. Let's see:

text = "Hello! How are you? I'm fine. Thanks."
split with re.split(r'[.!?]', text) gives:

['Hello', ' How are you', " I'm fine", ' Thanks', '']

Wait, the last element is because the last sentence ends with a period, so after splitting, the last split would have an empty string. But in the list comprehension, we check if s.strip() is not empty. So the empty string would be excluded.

Wait in the example, the sentences would be:

"Hello", "How are you", "I'm fine", "Thanks" → that's 4 sentences. Let's see:

Original split gives:

['Hello', ' How are you', " I'm fine", ' Thanks', ''].

After stripping each element:

First element 'Hello' → stripped is 'Hello' → valid.

Second ' How are you' → stripped is 'How are you' → valid.

Third " I'm fine" → stripped → "I'm fine".

Fourth ' Thanks' → → 'Thanks'.

Fifth is empty → stripped is '' → excluded.

So total 4, which is correct. So that works.

Another test case: "Hi there. What's up? Fine! Great..." → split would be on each of .?!, so the split on "Great..." would split on the . but the last part would have ???

Wait, the text "Great..." would split on the first '.'? Let's see:

The text "Great..." has three periods. The split would split on each '.' so:

["Great", "", "", ""] → but then when stripped, those would be empty. So in this case, "Great..." would be considered as one sentence before the first '.', but the rest would be empty. So the first part is "Great", which is non-empty, so that counts as a sentence. So the sentences would count that as 1 sentence here. Which is correct if the text ends with "...".

Hmm, maybe that's acceptable. The problem doesn't specify edge cases, so this approach should work for most cases.

Now, the code. The user wants the code only, no explanations. So putting it all together, the code is:

import re

text = input().strip()

chars = len(text)
words = len(text.split())
sentences = len([s for s in re.split(r'[.!?]', text) if s.strip()])

print(f"Characters: {chars}\nWords: {words}\nSentences: {sentences}")

Wait but the problem says "Return only the code." and the output should be the code. The code must be complete. However, maybe the user expects the counts to be returned as variables or printed? Since it's a script, the standard is to print them. The code above does that.

Alternatively, maybe the problem expects the counts to be returned in a specific format, but since the user didn't specify, the code should just compute and print each count.

Alternatively, perhaps the user wants the counts as separate outputs, but the code is okay as written.

Wait, looking back at the problem statement: the task is to write a Python script that counts those three, and the output is to return the code. So the code I have should be correct.

Wait, but maybe the sentences split can be done better. Let me think again: another approach could be to count the number of occurrences of sentence-ending punctuation. But that might not work because a sentence could end with a period inside quotes, or abbreviations, etc. But given the problem's simplicity, the split method is acceptable.

Another possible issue: the regex [.] matches a period, but in regex, '.' is a wildcard, so we need to escape it. Wait, in the regex r'[.!?]', the '.' is inside a character class, so it's treated as a literal period. So that's okay. The regex is correct.

So the code should be okay.