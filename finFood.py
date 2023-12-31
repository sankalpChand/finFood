import streamlit as st 



import yfinance as yf

def projectDescription():
    st.title("Welcome to FinFood! The Ultimate Stock App for Foodies!") #NEW
    st.image("images/mcdCover.jpg",width = 700)
    st.header("Stock Data of the Most Popular Restaurant Chains!")
    st.write("Hello, welcome to FinFood! This app was curated with the purpose of delivering stock information for various popular food chains!")
    st.write("    ")
    st.write("FinFood works to provide financial data for the following 6 food chains. Ticker symbols for each chain are included below: ")
    st.write(" ")
    
    st.write("McDonald's: MCD")
    
    st.write("The Coca-Cola Company: KO")
    
    st.write("PepsiCo, Inc.: PEP")
    
    st.write("Chipotle: CMG")
    
    st.write("Domino's Pizza: DPZ")
    
    st.write("Wendy's: WEN")

    st.write("---")


    
    
    
    

projectDescription()

def companySummary():

    valid_symbols = ["MCD", "KO", "PEP", "CMG", "DPZ", "WEN"]
    st.header("Want to learn more about each company? Select an option and read the bio!")
    st.image("images/secondPhoto.jpg",width = 700)

    userInput = st.selectbox("Select one of the following food chains", valid_symbols, key = "bio") #NEW

    stock = yf.Ticker(userInput)

    mainDict = stock.info

    

    st.write(mainDict["longBusinessSummary"])

    st.write("---")

companySummary()


def ceoSummary():
    valid_symbols = ["MCD", "KO", "PEP", "CMG", "DPZ", "WEN"]
    

    st.header("Learn more about the CEO running the company! Select one!")
    st.image("images/cash.jpg",width = 700)

    userInput2 = st.selectbox("Select one of the following food chains", valid_symbols, key ="ceo")

    stock = yf.Ticker(userInput2)

    mainDict = stock.info

    name = mainDict["companyOfficers"][0]["name"]
    age = mainDict["companyOfficers"][0]["age"]
    title = mainDict["companyOfficers"][0]["title"]
    totalPay = mainDict["companyOfficers"][0]["totalPay"]

    st.write(f"Name: {name},  Age: {age},  Title: {title},  Salary: ${totalPay}")

   


ceoSummary()



def finanicalInfo():
    valid_symbols = ["MCD", "KO", "PEP", "CMG", "DPZ", "WEN"]

    

    

    #st.write(mainDict["longBusinessSummary"])

    st.write("---")


    st.header("Select a company to find important finanical data!")

    userInput2 = st.selectbox("Select one of the following food chains", valid_symbols, key ="finance")

    stock = yf.Ticker(userInput2)

    mainDict = stock.info

    revenue = mainDict["totalRevenue"]
    totalCash = mainDict["totalCash"]
    currentStockPrice = mainDict["currentPrice"]
    debt = mainDict["totalDebt"]
    profit = mainDict["grossProfits"]
    buyRec = mainDict["recommendationKey"]


    
        


    st.write(f"Revenue: ${revenue}")
    st.write(f"Cash on Hand: ${totalCash}")
    st.write(f"Current Price: ${currentStockPrice}")
    st.write(f"Debt: ${debt}")
    st.write(f"Profit: ${profit}")
    st.write(f" Analyst Recommendation: {buyRec}")

finanicalInfo()


def history():

    st.header("View Stock Price History (1 Month)")

    valid_symbols = ["MCD", "KO", "PEP", "CMG", "DPZ", "WEN"]

    userInput = st.selectbox("Select one of the following food chains", valid_symbols, key = "history") #NEW

    stock = yf.Ticker(userInput)

    history = stock.history(period = "1mo")
    st.line_chart(history["Close"])


history()

    


    
    

   




   
    


