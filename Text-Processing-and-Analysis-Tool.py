import string

# Text Processing and Analysis Tool
# This program validates, processes, and analyzes English sentences.
#
# Features:
# - Validates English input
# - Removes user-selected text
# - Removes numbers connected to letters
# - Finds the longest word
# - Counts words, letters, and numbers
# - Allows the user to process multiple sentences


while True:

    # Get a valid English sentence
    while True:
        sentence = input("\nEnter your sentence: ")

        correct = True
        i = 0

        while i < len(sentence):

            if (
                sentence[i] in string.ascii_letters
                or sentence[i] in string.digits
                or sentence[i] == " "
                or sentence[i] in string.punctuation
            ):
                i += 1
            else:
                correct = False
                break

        if correct:
            break

        print(
            "Error! Only English letters, numbers, spaces, "
            "and punctuation are allowed."
        )

    # Remove selected text
    deleted = input("What would you like to remove from the sentence? ")
    sentence = sentence.replace(deleted, "")

    print("\nCorrected sentence:")
    print(sentence)

    # Remove numbers connected to letters
    new_sentence = ""
    i = 0

    while i < len(sentence):

        if sentence[i].isdigit():

            start = i

            while i < len(sentence) and sentence[i].isdigit():
                i += 1

            end = i - 1

            left = False
            right = False

            if start > 0:
                if sentence[start - 1] in string.ascii_letters:
                    left = True

            if end < len(sentence) - 1:
                if sentence[end + 1] in string.ascii_letters:
                    right = True

            # Keep the number only if it is not connected to a letter
            if not (left or right):

                j = start

                while j <= end:
                    new_sentence += sentence[j]
                    j += 1

        else:
            new_sentence += sentence[i]
            i += 1

    # Find the longest word
    longest_word = ""
    longest_length = 0

    i = 0

    while i < len(new_sentence):

        if new_sentence[i] in string.ascii_letters:

            start = i

            while (
                i < len(new_sentence)
                and new_sentence[i] in string.ascii_letters
            ):
                i += 1

            current_length = i - start

            if current_length > longest_length:

                longest_length = current_length
                longest_word = ""

                j = start

                while j < i:
                    longest_word += new_sentence[j]
                    j += 1

        else:
            i += 1

    # Count words, letters, and numbers
    word_count = 0
    letter_count = 0
    number_count = 0

    i = 0
    inside_word = False

    while i < len(new_sentence):

        if new_sentence[i] in string.ascii_letters:

            letter_count += 1

            if not inside_word:
                word_count += 1
                inside_word = True

        else:
            inside_word = False

            if new_sentence[i].isdigit():
                number_count += 1

        i += 1

    # Display the final results
    print("\n" + "=" * 40)
    print("          TEXT ANALYSIS")
    print("=" * 40)

    print("\nFinal sentence:")
    print(new_sentence)

    print("\nLongest word:", longest_word)
    print("Longest word length:", longest_length)

    print("Number of words:", word_count)
    print("Number of letters:", letter_count)
    print("Number of numbers:", number_count)

    print("=" * 40)

    # Ask if the user wants to continue
    again = input("\nWould you like to process another sentence? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank you for using the Text Processing Tool!")
        break