def chuyen_tb3(dataframe):
    dataframe = dataframe.T
    dataframe = dataframe.replace(r'\n', ' ', regex=True)
    # dataframe = dataframe.to_excel('D:\ex_table3.xlsx')
    return dataframe

def table2(dataframe):
        dataframe = dataframe.replace('<table', '<table style="table-layout: fixed;"')
        # dataframe= dataframe.drop(columns=['IS'])
        # dataframe = dataframe.to_excel('D:\ex_table2.xlsx')
        return dataframe

def table1(dataframe):  
    dataframe = dataframe.dropna(thresh=2)
    dataframe = dataframe.fillna(' ')
    # dataframe = dataframe.to_excel('D:\ex_table1.xlsx')
    return dataframe