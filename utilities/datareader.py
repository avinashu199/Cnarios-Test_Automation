import pandas as pd
class DataReader:
    def payment_details(self):
        df=pd.read_excel("C:\\Users\\91741\\PycharmProjects\\Cnarios\\data\\test_data.xlsx", sheet_name="payment details")
        return df.values.tolist()
    def url(self):
        df=pd.read_excel("C:\\Users\\91741\\PycharmProjects\\Cnarios\\data\\test_data.xlsx",sheet_name="basic details")
        url=df.iat[0,0]
        return url
    def file_location(self):
        df = pd.read_excel("C:\\Users\\91741\\PycharmProjects\\Cnarios\\data\\test_data.xlsx", sheet_name="file upload")
        path = df.iat[0, 0]
        return path