# Richard and Iju   
# content : all the comment and rating etc. from web.
# load library #請先執行這行，下方的再另外執行
import requests
from bs4 import BeautifulSoup

#


movie_num = 0
page_num = 1
with open('movie.txt','w') as moviecontent:
    print('正在進行IMDB資料爬取程序...\n')
    while page_num > 0:
        if page_num == 1:
            url = "http://www.imdb.com/search/title?year=2016,2016&title_type=feature&explore=has&sort=year,desc&page=1&ref_=adv_nxt"
        elif page_num > 2:
            break
        else:
            url = "http://www.imdb.com/search/title?year=2016,2016&title_type=feature&explore=has&sort=year,desc&page={}&ref_=adv_nxt".format(page_num)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        movieurl = soup.findAll("h3", {"class":"lister-item-header"})

        print("正在載入網頁內容第{}頁...".format(page_num))
        
        for i in range(len(movieurl)):
            url = movieurl[i].findAll('a', href=True)
            title = movieurl[i].select('a')
            
            print (url, title)
        
            for idx in range(len(url)):
                movies = requests.get("http://www.imdb.com/" + url[idx]['href'])
                movies_soup = BeautifulSoup(movies.text, "lxml")

                #movie title
                for tag_titles in movies_soup.find("title"):
                    titles = tag_titles.encode('utf-8')
                    moviecontent.write('Movie title: ' + str(titles)[1:] + '\n')  #started from index one to remove the 'b'

                #movie genre
                for tag in movies_soup.findAll("span", itemprop="genre"):
                    genre = tag.string
                    moviecontent.write('Movie genre: ' + genre + '\n')

                #movie ratings
                ratings = movies_soup.find("span", {"itemprop":"ratingValue"})
                if ratings == None:
                    moviecontent.write('User ratings: No rating yet' + '\n')
                    pass
                else: 
                    for ratings in movies_soup.find("span", {"itemprop":"ratingValue"}): ###Some of movies do not have ratings###
                        moviecontent.write('User ratings: ' + ratings + '\n')

                #movie director
                director = movies_soup.find("span", {"itemprop":"director"})
                if director == None:
                    moviecontent.write('No director.' + '\n')
                    pass
                else:
                    for d_tag in movies_soup.find("span", {"itemprop":"director"}).select("span"):
                        director = d_tag.string.encode('utf-8')
                        moviecontent.write('Director: ' + str(director)[1:] + '\n')
                        
                #movie actors
                for a_list in movies_soup.findAll("span", itemprop="actors"):
                    for a_tag in a_list.select("span"):
                        actor = a_tag.string.encode('utf-8')
                        moviecontent.write('Movie actors: ' + str(actor)[1:] + '\n')


                #movie summary
                for summary in movies_soup.find("div", {"class":"summary_text"}):
                    s = summary.string.encode('utf-8')
                    moviecontent.write('Movie summary: '+ str(s)[4:].strip(' ') + '\n')  #started from index four to remove html
                                                                                        #and use strip() to remove whitespace
                
                
                #movie comments
                see = movies_soup.findAll('div', {'class': 'see-more'})
                if see[-2].span == None:
                    moviecontent.write('No comment.' + '\n')
                    pass
                else:
                    review_link = see[-2].span.next_sibling.next_sibling['href']
                    prefix = 'http://www.imdb.com/'
                    reviews = requests.get(prefix + review_link).text
                    review_soup = BeautifulSoup(reviews)
                    for review in review_soup.select('p')[11:]:
                        comment = review.getText().encode('utf-8')
                        moviecontent.write('Comment: ' + str(comment)[4:] + '\n')                        
        
                        
                moviecontent.write('\n')
                


        page_num += 1


## do not include the crawler codes in the final data, precrawel all the movie content before all the function are processed. ##