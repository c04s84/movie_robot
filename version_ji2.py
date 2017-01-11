#沒問題version #第二次沒問題version
#### 最後最後version#####
# yes/no 想法可忽略大小寫
# genre input 可忽略大小寫

import json
import random
from textblob import TextBlob
from collections import namedtuple
from collections import Counter
from textblob.taggers import NLTKTagger
from nltk.corpus import stopwords


with open('movieNew.json') as data_file:
    data = json.load(data_file)


random_movie = []
genre_movie = []
comment_movie = []


input_1 = input('你有想法嗎？(yes/no)：').lower()
if input_1 == "no":
    for i in data:
        Name = str(i[0])
        Genre = str(i[1])
        Stars = int(i[2])
        Review = list(i[-1])
        random_movie.append((Name))
    print("我們為您推薦的電影是：",random.sample(random_movie, 3))

    input_4 = input('輸入電影名稱看看大家怎麼說：')
    for g in data:
        g_Name = str(g[0])
        g_Genre = str(g[1])
        g_Stars = int(g[2])
        g_Review = list(g[-1])
        genre_movie.append((g_Name, g_Genre, g_Stars, g_Review))
        sentiment = 0
        for film in range(len(genre_movie)+1):

            if g_Name == input_4:
                for index in range(len(g_Review)-2):
                    testimonial = TextBlob(g_Review[index])
                    testimonial.sentiment
                    testimonial.sentiment.polarity
                    sentiment += testimonial.sentiment.polarity

                sentiment /=(len(g_Review)-2)
                if sentiment >= 0.5:
                    print("Great! Recommended!")
                elif sentiment >= 0 and sentiment < 0.5:
                    print("Okay! This movie seems not bad!")
                elif sentiment >= -0.5 and sentiment < 0:
                    print("Humm... This movie seems mediocre!")
                else:
                    print("Bad! Not recommended!")

                print("The average sentiment score is:",sentiment)

#                    if g_Name == input_4:
                for indexes in range(len(g_Review)-2):
                    nltk_tagger = NLTKTagger()
                    taggedword = TextBlob(g_Review[indexes],pos_tagger=nltk_tagger)
                    taggedword = taggedword.pos_tags

                    wordTagged = []
                    for TaggedItem in taggedword:
                        Word = str(TaggedItem[0])
                        POS = str(TaggedItem[1])
                        if POS == 'JJ':
                            wordTagged.append((Word))
                            count_JJ = Counter(wordTagged)
                for k, v in sorted(count_JJ.items(),key = lambda x: x[1], reverse=True ):
                    print ("有",v,"個人覺得這部電影",k)



        #                        print(taggedword)

                break



else:
    input_2 = input('你想看什麼類型？').capitalize()
    input_3 = input('你想看幾顆星的呢？')
    for g in data:
        g_Name = str(g[0])
        g_Genre = str(g[1])
        g_Stars = int(g[2])
        g_Review = list(g[-1])
        genre_movie.append((g_Name, g_Genre, g_Stars, g_Review))
        if input_2 in g_Genre:
            if g_Stars >= int(input_3):
                print("我們為您推薦的電影是：", g_Name, "它被評選為：", g_Stars, "顆星")
            #else:
                #print("麻煩您自己去google")
    input_4 = input('輸入電影名稱看看大家怎麼說：')
    for g in data:
        g_Name = str(g[0])
        g_Genre = str(g[1])
        g_Stars = int(g[2])
        g_Review = list(g[-1])
        genre_movie.append((g_Name, g_Genre, g_Stars, g_Review))
        sentiment = 0
        for film in range(len(genre_movie)+1):

            if g_Name == input_4:
                for index in range(len(g_Review)-2):
                    testimonial = TextBlob(g_Review[index])
                    testimonial.sentiment
                    testimonial.sentiment.polarity
                    sentiment += testimonial.sentiment.polarity

                sentiment /=(len(g_Review)-2)
                if sentiment >= 0.5:
                    print("Great! Recommended!")
                elif sentiment >= 0 and sentiment < 0.5:
                    print("Okay! This movie seems not bad!")
                elif sentiment >= -0.5 and sentiment < 0:
                    print("Humm... This movie seems mediocre!")
                else:
                    print("Bad! Not recommended!")

                print("The average sentiment score is:",sentiment)

#                    if g_Name == input_4:
                for indexes in range(len(g_Review)-2):
                    nltk_tagger = NLTKTagger()
                    taggedword = TextBlob(g_Review[indexes],pos_tagger=nltk_tagger)
                    taggedword = taggedword.pos_tags

                    wordTagged = []
                    for TaggedItem in taggedword:
                        Word = str(TaggedItem[0])
                        POS = str(TaggedItem[1])
                        if POS == 'JJ':
                            wordTagged.append((Word))
                            count_JJ = Counter(wordTagged)
                for k, v in sorted(count_JJ.items(),key = lambda x: x[1], reverse=True ):
                    print ("有",v,"個人覺得這部電影",k)



        #                        print(taggedword)

                break
