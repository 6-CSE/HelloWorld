def run():
    import pandas as pd
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, STOPWORDS

    # 'Hello World' word cloud functions
    def generateHelloWorldPython():
        hello = pd.read_csv('HelloWorldText.csv', usecols = ['Terms'])


        pythonHello = " ".join(text for text in hello['Terms'])
        print(pythonHello)


        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(width=1500, height=500, background_color='white', stopwords=stopwords)
        wordcloud.generate(pythonHello)
        plt.figure(figsize=(20, 15))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

        wordcloud.to_file('HelloWorldPythonHF2.png')
    generateHelloWorldPython()

    def generateHelloWorldMultiLang():
        hello = pd.read_csv('HelloWorldText.csv')


        pythonHello = " ".join(text for text in hello['Text'])
        print(pythonHello)


        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(width=1500, height=500, background_color='white',stopwords=stopwords)
        wordcloud.generate(pythonHello)
        plt.figure(figsize=(20, 15))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

        wordcloud.to_file('HelloWorldPythonHFML2.png')
    generateHelloWorldMultiLang()

# def generateHelloWorldLanguageSample():
#     hello = pd.read_csv('HelloWorldText.csv')


#     pythonHello = " ".join(text for text in hello['Language'])
#     print(pythonHello)


#     stopwords = set(STOPWORDS)
#     wordcloud = WordCloud(width = 1500, height = 500,background_color='white',stopwords=stopwords)
#     wordcloud.generate(pythonHello)
#     plt.figure(figsize=(20, 15))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis("off")
#     plt.show()

#     wordcloud.to_file('HelloWorldPythonHFL2.png')
# generateHelloWorldLanguageSample()
run()