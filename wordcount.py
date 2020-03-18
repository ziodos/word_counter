import sys
 
def is_legal(chr):
    return ('A' <= chr <= 'Z') or ('a' <= chr <= 'z') or '0' <= chr <= '9' or chr == "'" or chr == '-'
 
def split_to_words(text):
    word_list = list()
    word = "" # current word
    for chr in text:
        # add chr to current word if legal chr
        if is_legal(chr):
            word += chr
            continue
        # if not legal char, and word is not "", then add to word_list
        if word:
            word_list.append(word)
        word = ""
    # don't forget the last word (only happens if last chr is legal)
    if word:
        word_list.append(word)
 
    return word_list
 
def get_counts(word_list):
    # loop through the word_list and keep track of counts
    counts = dict()
    for word in word_list:
        word = word.lower() # convert to lowercase
        counts[word] = counts.get(word, 0) + 1
    return counts
 
def output_to_file(count_tuples, filename):
    file = open(filename, 'w')
    for word, count in count_tuples:
        print(word, count, file=file)
    file.close()
 
def alphabetical_sortkey(item):
    # sort by word. item = (word, count)
    return item[0]
 
def most_popular_sortkey(item):
    # sort by -count, word. item = (word, count)
    return -item[1], item[0]
 
if __name__ == '__main__':
    filename = sys.argv[1]
    text = open(filename, 'r').read()
 
    word_list = split_to_words(text)
    counts = get_counts(word_list)
 
    count_tuples = sorted(counts.items(), key=alphabetical_sortkey)
    output_to_file(count_tuples, 'alphabetical.txt')
 
    count_tuples = sorted(counts.items(), key=most_popular_sortkey)
    output_to_file(count_tuples, 'most_popular.txt')
 
