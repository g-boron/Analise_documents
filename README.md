# Analise documents 📰
App in Python responsible for downloading papers and analyse them.

### How to use ⚙️
Type in console `python main.py -h` or `python main.py --help` to see the syntax.

To download papers use `python main.py -d <number of papers> -k <keyword>` or `python main.py --download <number of papers> --keyword <keyword>`

If you want to want to see the statistics of papers (File name, number of words, chars, chars without spaces and number of specific words) use `python main.py -s y` or `python main.py --stats y` then you can draw a plot or get statistics such as mean, min and max value of specific collumn.

You can also find the number of occurrences of the entered word using `python main.py -w <word>` or `python --count_words <word>` or if you don't use `-w` there will be number of occurrences of keyword in articles.

## About the project :computer:

<b>The idea for the project came from my classes at university. I had to download science papers and analyse them manually, so it took hours. Clicking article one by one, download them and then using e.g. Word for counting words, chars etc. I wanted to do it quicker and more automatic, so I write this console app in Python.
  
I used `sys.argv`, because I wanted this app to have options - if you want only download papers, you can do it. If you want analyse papers you have on your disk without downloading it - you also can do it!
  
As a result, I achieved all goals that I have set and this app works well. It helped me automate my tasks and thanks to this I saved a lot of time.
  
### Used libraries 📚
  
For downloading papers I used `arxiv` library, which isn't difficult to use and has everything I wanted. Library `PyPDF2` helped me get data from pdfs that I needed to use later. At the end two necessary libraries are `pandas` and `matplotlib`. They are essential for data analysis and visualise it.<b>
