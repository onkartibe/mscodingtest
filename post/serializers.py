from rest_framework import serializers
from post.models import Post

from collections import Counter

stopWords = ["#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
              "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", 
              "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
              "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
              "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", 
              "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
              "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
              "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
              "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
              "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
              "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
              "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
              "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
              "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
              "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
              "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
              "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
              "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
              "yourself", "yourselves"]

def fn_get_top5_words(strText):

        #remove stop words from text
        querywords = strText.split()
        resultwords  = [word for word in querywords if word not in stopWords]

        #Get a top workds from text
        word_counts = Counter(resultwords).most_common(5)
        lst_words  = [top_word for top_word, cnt in word_counts]
        return lst_words

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField("fn_get_tag")

    def fn_get_tag(self, Post):
        str_post_tags = fn_get_top5_words(Post.description)
        return str_post_tags

    class Meta:
        model = Post
        fields = ("id", "created", "title", "author", "slug", "description","tags")
