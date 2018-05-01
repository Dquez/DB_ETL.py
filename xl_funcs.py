import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
import xlwt

def xl_write(data, db):
    if db == "mysql":
        
        # Initialize a workbook 
        top_albums_book = xlwt.Workbook(encoding="utf-8")
    
        # Add a sheet to the workbook 
        top50 = top_albums_book.add_sheet("Top 50 Songs") 

        top_row = ["position", "artist", "song", "year", "raw_total", "raw_usa", "raw_uk", "raw_eur", "raw_row"]
        # Write to the sheet of the workbook
        for i in range(len(top_row)):
            top50.write(0, i, top_row[i]) 
        for i in range(len(data)):
            for j in range(len(data[i])):
                top50.write(i+1, j, data[i][j])            
        # Save the workbook 
        top_albums_book.save("topalbums.xls")
 
    else:
        medium_articles= xlwt.Workbook(encoding="utf-8")
        # Add a sheet to the workbook 
        top_medium_articles = medium_articles.add_sheet("Top Articles From Medium.com") 
        top_row = ["Headline","Notes", "Summary", "Url", "ImgUrl"]
        # Write to the sheet of the workbook
        
        for i in range(len(top_row)):
            top_medium_articles.write(0, i, top_row[i])
        i = 0
        for document in data:
            j = 0
            for key in document:
                                    
                if key != "_id" or key != "isSaved":
                    top_medium_articles.write(i+1, j, document[key])
                    j +=1
            i+=1
        # Save the workbook
        medium_articles.save("TopMediumArticles.xls")
