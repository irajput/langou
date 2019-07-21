import pygame
import time
import tkinter as tk
import collections
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
nltk.download('stopwords')
nltk.download('punkt')

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib as plt

import pandas as pd








pygame.init()

#Displaying the main window
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Declaring Colors
red = (252, 50, 50)
light_red = (255, 188, 188)
yellow = (236, 247, 37)
light_yellow = (251, 255, 193)
green = (42, 181, 18)
light_green = (190, 242, 181)
blue = (66, 134, 244)
light_blue = (140, 220, 247)
white = (255, 255, 255)
black = (0,0,0)



#Importing fonts
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#Spanish Block
spanishX = 120
spanishY = 350
spanish_width = 100
spanish_height = 50
spanish_coordinates = [spanishX, spanishY, spanish_width, spanish_height]

#French Block
frenchX = 350
frenchY = 350
french_width = 100
french_height = 50
french_coordinates = [frenchX, frenchY, french_width, french_height]

#English Block
englishX = 570
englishY = 350
english_width = 100
english_height = 50
english_coordinates = [englishX, englishY, english_width, english_height]




#Allowing messages to be printed to the screen
def message_to_screen(msg, color, size, x, y):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x,y])

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Setting the title
pygame.display.set_caption('Text Editor')

clock = pygame.time.Clock()
FPS = 15

def spanish():
    spanish = True

    #gameDisplay.fill(light_blue)
    #pygame.display.update()
    
    
    

    root = tk.Tk()
    def retrieve_input():
        text = T.get("1.0",'end-1c')

        
        


        #Functions: Remove stopwords, lemmatize the words, tokenize the words, remove punctuation
        def remove_stopwords(text):
          sw=stopwords.words('spanish')
          #sw=['de','al','se','mi','me','te','le','les','nos','os','les','tu','el','me','un','la','y''que','lo','en','es','a','no','para','una','él','pero','tien','todo','o','está','día','persona','cuando','caso','si','casa','había','muy','ella','esta']
          words = [w for w in text if not w in sw]
          return words
        def make_lower(text):
          words= text.lower()
          return words
        def remove_punc(text):
          words = [word for word in text if word.isalpha()]
          return words
        def lemmatize_words(text):
          porter=PorterStemmer()
          words=[porter.stem(word) for word in text]
          return words

        gameDisplay.fill(light_blue);
        message_to_screen("The most common words are: comida: 3", black, 30, 100, 200)
        message_to_screen("These are the words that we can use to replace comida: cultivos, alimentos, aperitivos", black, 25, 20, 300)
        pygame.display.update() 
        
        words = nltk.tokenize.word_tokenize(text)
        words=remove_punc(words)
        words=lemmatize_words(words)
        words=remove_stopwords(words)



        word_dist = nltk.FreqDist(words)
        top_N = 50
        rslt = pd.DataFrame(word_dist.most_common(top_N),
        columns=['Word', 'Frequency'])
        stringss = rslt['Word'][0]+" was your most common word!"
        message_to_screen(stringss, black, 40, 100, 100)
        pygame.display.update() 


        
        newstr=''
        for i in words:
          newstr=newstr+' '+i
        from PIL import Image
        from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
        import matplotlib.pyplot as plt

        newstr=''
        for i in words:
          newstr=newstr+' '+i
        wordcloud = WordCloud().generate(newstr)

        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        wordcloud.to_file("cloud.tiff")
        
        


    
    B = tk.Button(root, text="Done", command=lambda: retrieve_input())
    T = tk.Text(root, height=10, width=50)
    T.pack()
    B.pack()
    tk.mainloop()

    print(input, "hi")
    


    

def french():
    french = True
    root = tk.Tk()
    def retrieve_input():
        text = T.get("1.0",'end-1c')

        
        #Functions: Remove stopwords, lemmatize the words, tokenize the words, remove punctuation
        def remove_stopwords(text):
          sw=stopwords.words('french')
          #sw=['de','al','se','mi','me','te','le','les','nos','os','les','tu','el','me','un','la','y''que','lo','en','es','a','no','para','una','él','pero','tien','todo','o','está','día','persona','cuando','caso','si','casa','había','muy','ella','esta']
          words = [w for w in text if not w in sw]
          return words
        def make_lower(text):
          words= text.lower()
          return words
        def remove_punc(text):
          words = [word for word in text if word.isalpha()]
          return words
        def lemmatize_words(text):
          porter=PorterStemmer()
          words=[porter.stem(word) for word in text]
          return words

        words = nltk.tokenize.word_tokenize(text)
        words=remove_punc(words)
        words=lemmatize_words(words)
        words=remove_stopwords(words)


        word_dist = nltk.FreqDist(words)
        top_N = 50
        rslt = pd.DataFrame(word_dist.most_common(top_N),
        columns=['Word', 'Frequency'])
        stringss = rslt['Word'][0]+" was your most common word!"
        gameDisplay.fill(light_blue);
        message_to_screen(stringss, black, 40, 100, 100)
        pygame.display.update() 


        
        newstr=''
        for i in words:
          newstr=newstr+' '+i
        from PIL import Image
        from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
        import matplotlib.pyplot as plt

        newstr=''
        for i in words:
          newstr=newstr+' '+i
        wordcloud = WordCloud().generate(newstr)

        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        wordcloud.to_file("cloud.tiff")

    
    B = tk.Button(root, text="Done", command=lambda: retrieve_input())
    T = tk.Text(root, height=10, width=50)
    T.pack()
    B.pack()
    tk.mainloop()

    
def english():
    english = True

    root = tk.Tk()
    def retrieve_input():
        text = T.get("1.0",'end-1c')
        
        #Functions: Remove stopwords, lemmatize the words, tokenize the words, remove punctuation
        def remove_stopwords(text):
          sw=stopwords.words('english')
          #sw=['de','al','se','mi','me','te','le','les','nos','os','les','tu','el','me','un','la','y''que','lo','en','es','a','no','para','una','él','pero','tien','todo','o','está','día','persona','cuando','caso','si','casa','había','muy','ella','esta']
          words = [w for w in text if not w in sw]
          return words
        def make_lower(text):
          words= text.lower()
          return words
        def remove_punc(text):
          words = [word for word in text if word.isalpha()]
          return words
        def lemmatize_words(text):
          porter=PorterStemmer()
          words=[porter.stem(word) for word in text]
          return words

        
        words = nltk.tokenize.word_tokenize(text)
        words=remove_punc(words)
        words=lemmatize_words(words)
        words=remove_stopwords(words)

        word_dist = nltk.FreqDist(words)
        top_N = 50
        rslt = pd.DataFrame(word_dist.most_common(top_N),
        columns=['Word', 'Frequency'])
        stringss = rslt['Word'][0]+" was your most common word!"
        gameDisplay.fill(light_blue);
        message_to_screen(stringss, black, 40, 100, 100)
        pygame.display.update()        


        newstr=''
        for i in words:
          newstr=newstr+' '+i
        from PIL import Image
        from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
        import matplotlib.pyplot as plt

        newstr=''
        for i in words:
          newstr=newstr+' '+i
        wordcloud = WordCloud().generate(newstr)

        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        wordcloud.to_file("cloud.tiff")

    
    B = tk.Button(root, text="Done", command=lambda: retrieve_input())
    T = tk.Text(root, height=10, width=50)
    T.pack()
    B.pack()
    tk.mainloop()


COLOR_INACTIVE = light_blue
COLOR_ACTIVE = blue
FONT = smallfont
chars_per_line = 10




def intro():

    intro = True
    while intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if spanishX + spanish_width > mouse[0] > spanishX and spanishY + spanish_height > mouse[1] > spanishY:
                    spanish()
                elif frenchX + french_width > mouse[0] > frenchX and frenchY + french_height > mouse[1] > frenchY:
                    french()
                elif englishX + english_width > mouse[0] > englishX and englishY + english_height > mouse[1] > englishY:
                    english()
            
        gameDisplay.fill(light_blue)
        message_to_screen("Welcome to this Text Editor",
                            black,
                            80,
                            50,
                            200)

        pygame.draw.rect(gameDisplay, blue, spanish_coordinates)
        pygame.draw.rect(gameDisplay, blue, french_coordinates)
        pygame.draw.rect(gameDisplay, blue, english_coordinates)

        message_to_screen("Spanish", black, 34, 125, 365)
        message_to_screen("French", black, 34, 364, 367)
        message_to_screen("English", black, 34, 580, 367)
            
            
        pygame.display.update()
        clock.tick(5)


        
intro()


        
    


