# Welcome to my AI program I built to help answer investing questions-Don
# import tkinter to set up graphical interface for the program.
import tkinter as tk


# Class set up for the investing Ai to set up window,screen size, color,window thickness all written in python
class InvestingChatbot:
    def __init__(self, window):
        self.window = window
        self.window.title("Investing Assistant AI")
        self.window.configure(bg="darkslateblue")
        self.window.configure(bg="lightblue")
        # Create a text widget to display the conversation
        self.conversation_display = tk.Text(window, height=20, width=120)
        self.conversation_display.pack()
        self.window.configure(highlightthickness=2)

        # Create a label and entry field for user input
        self.input_label = tk.Label(window, text="Ask a question:")
        self.input_label.pack()

        self.input_entry = tk.Entry(window, width=50)
        self.input_entry.pack()

        # Create a button to submit the user's question
        self.submit_button = tk.Button(window, text="Submit", command=self.submit_question)
        self.submit_button.pack()

        # Initialize the conversation with a welcome message
        self.conversation_display.insert(tk.END,
                                         "Investing Assistant AI: Welcome! What Investing questions do you have?\n")
        self.conversation_display.configure(state='disabled')

    def submit_question(self):
        user_question = self.input_entry.get()

        if not user_question:
            return

        self.conversation_display.configure(state='normal')
        self.conversation_display.insert(tk.END, "You: " + user_question + "\n")
        self.input_entry.delete(0, tk.END)

        # Add your custom AI logic here to provide investing advice based on user's question

        # Sample response based on user's question
        if "stock" in user_question:
            response = "Investing in stocks can provide high returns, but it also carries risks. It's important to do thorough research before investing in specific stocks."
        elif "real estate" in user_question:
            response = "Real estate can be a stable long-term investment option, especially if you choose properties in growing areas with high demand."
        elif "diversify" in user_question:
            response = "Diversifying your investment portfolio is a smart strategy to minimize risk. Consider investing in different asset classes, such as stocks, bonds, and real estate."
        else:
            response = "I'm sorry, I couldn't understand your question. Can you please rephrase or ask something else?"

            # Sample questions and answers for the Investing AI

            if "stock" in user_question:
                response = "Investing in stocks can provide high returns, but it also carries risks. " \
                           "It's important to do thorough research before investing in specific stocks."
            elif "real estate" in user_question:
                response = "Real estate can be a stable long-term investment option, especially if you choose " \
                           "properties in growing areas with high demand."
            elif "diversify" in user_question:
                response = "Diversifying your investment portfolio is a smart strategy to minimize risk. " \
                           "Consider investing in different asset classes, such as stocks, bonds, and real estate."
            elif "mutual funds" in user_question:
                response = "Mutual funds are investment vehicles that pool money from multiple investors to invest " \
                           "in a diversified portfolio of stocks, bonds, or other assets."
            elif "risk tolerance" in user_question:
                response = "Risk tolerance refers to an individual's ability to handle the potential loss of an investment. " \
                           "Assessing your risk tolerance is important in determining suitable investment options."
            elif "ETFs" in user_question:
                response = "ETFs (Exchange-Traded Funds) are investment funds traded on stock exchanges, " \
                           "similar to individual stocks. They offer diversification and are passively managed."
            elif "401(k)" in user_question:
                response = "A 401(k) is a retirement savings plan offered by employers. " \
                           "Contributions are made from pre-tax income, and investment growth is tax-deferred."
            elif "IRA" in user_question:
                response = "An IRA (Individual Retirement Account) is a personal retirement savings account that provides " \
                           "tax advantages. There are different types of IRAs, such as Traditional and Roth IRAs."
            elif "investment horizon" in user_question:
                response = "Investment horizon refers to the length of time an investor plans to hold an investment " \
                           "before needing the funds. It helps determine appropriate investment strategies."
            elif "dividends" in user_question:
                response = "Dividends are payments made by companies to their shareholders from their profits. " \
                           "They are often distributed quarterly and can be a source of regular income for investors."
            elif "asset allocation" in user_question:
                response = "Asset allocation refers to the distribution of investments across different asset classes " \
                           "like stocks, bonds, and cash. It helps balance risk and return based on investor goals."
            elif "investment strategy" in user_question:
                response = "An investment strategy is a plan or approach used to make investment decisions. " \
                           "It can be based on factors like risk tolerance, time horizon, and financial goals."
            elif "market volatility" in user_question:
                response = "Market volatility refers to the fluctuation in prices or values of financial assets. " \
                           "It can present both risks and opportunities for investors."
            elif "dividend yield" in user_question:
                response = "Dividend yield is a financial ratio that shows the annual dividend income of an investment " \
                           "as a percentage of its current price. It indicates the return from dividends."
            elif "fundamental analysis" in user_question:
                response = "Fundamental analysis involves evaluating the financial health and performance of a company " \
                           "to determine its intrinsic value and make investment decisions."
                # Sample questions and answers for the Investing AI

            elif "bond" in user_question:
                response = "Bonds are fixed-income securities that represent a loan made by an investor to a borrower, " \
                           "typically a government or corporation. They provide regular interest payments and return of principal."
            elif "commodities" in user_question:
                response = "Commodities are raw materials or primary agricultural products that can be bought and sold, " \
                           "such as gold, oil, or wheat. They offer diversification and can act as a hedge against inflation."
            elif "initial public offering" in user_question:
                response = "An initial public offering (IPO) is the first sale of a company's shares to the public. " \
                           "It allows the company to raise capital and become publicly traded."
            elif "market order" in user_question:
                response = "A market order is an order to buy or sell a security at the current market price. " \
                           "It guarantees execution but may not guarantee a specific price."
            elif "limit order" in user_question:
                response = "A limit order is an order to buy or sell a security at a specific price or better. " \
                           "It ensures a desired price but may not guarantee immediate execution."
            elif "stop-loss order" in user_question:
                response = "A stop-loss order is an order to sell a security when its price reaches a specified level. " \
                           "It is used to limit losses and manage risk in case the market moves against the investor."
            elif "return on investment" in user_question:
                response = "Return on investment (ROI) is a measure of the profitability of an investment. " \
                           "It is calculated as the gain or loss from an investment relative to its cost."
            elif "capital gains" in user_question:
                response = "Capital gains are the profits realized from the sale of an investment or asset. " \
                           "They are subject to capital gains tax, which varies based on the holding period and tax laws."
            elif "diversification" in user_question:
                response = "Diversification is the strategy of spreading investments across different assets or asset classes " \
                           "to reduce risk. It helps protect against the potential decline of any single investment."
            elif "risk management" in user_question:
                response = "Risk management refers to the process of identifying, assessing, and prioritizing risks " \
                           "to minimize potential losses. It involves strategies like diversification and asset allocation."
            elif "market index" in user_question:
                response = "A market index is a benchmark that measures the performance of a specific " \
                           "segment of the stock market, such as the S&P 500 or Dow Jones Industrial Average."
            elif "dollar-cost averaging" in user_question:
                response = "Dollar-cost averaging is an investment strategy where an investor regularly invests a fixed " \
                           "amount of money at predetermined intervals, regardless of market conditions. It reduces the impact " \
                           "of short-term market volatility."
            elif "volatility index" in user_question:
                response = "The volatility index, commonly known as the VIX, measures the market's expectation of future " \
                           "volatility. It is often used as a gauge of investor sentiment and market risk."
            elif "exchange rate" in user_question:
                response = "Exchange rate is the rate at which one currency can be exchanged for another. " \
                           "Fluctuations in exchange rates can impact investments in international markets."
                # Sample questions and answers for 401(k) plans

            elif "contribution limits" in user_question:
                response = "For 2023, the annual contribution limit for a 401(k) is $20,500 for individuals under 50 " \
                           "and $27,000 for individuals aged 50 and above (including catch-up contributions)."
            elif "employer match" in user_question:
                response = "Many employers offer a 401(k) match, where they contribute a certain percentage of an employee's " \
                           "salary to their 401(k) account. It's important to take full advantage of employer matching contributions."
            elif "vesting period" in user_question:
                response = "The vesting period refers to the amount of time an employee must work for an employer " \
                           "to become eligible for the employer's contributions to their 401(k) account. Vesting schedules vary."
            elif "rollover" in user_question:
                response = "A 401(k) rollover is the process of transferring funds from a previous employer's 401(k) " \
                           "to an individual retirement account (IRA) or a new employer's 401(k) plan. It helps maintain " \
                           "tax advantages and consolidates retirement savings."
            elif "loan options" in user_question:
                response = "Some 401(k) plans allow participants to take out loans from their accounts. " \
                           "However, there are restrictions and potential consequences, such as taxes and penalties, if not repaid."
            elif "early withdrawal penalty" in user_question:
                response = "If you withdraw funds from your 401(k) before the age of 59 ½, you may be subject to an early " \
                           "withdrawal penalty of 10% in addition to regular income taxes, unless an exception applies."
            elif "required minimum distributions" in user_question:
                response = "Required minimum distributions (RMDs) are the minimum amounts that individuals must withdraw " \
                           "from their 401(k) or traditional IRA accounts after reaching the age of 72 (or 70 ½ if born before " \
                           "July 1, 1949). Failure to take RMDs can result in penalties."
            elif "Roth 401(k)" in user_question:
                response = "A Roth 401(k) is a retirement savings plan that allows participants to make after-tax contributions. " \
                           "Qualified withdrawals from a Roth 401(k) are tax-free in retirement."
            elif "traditional 401(k)" in user_question:
                response = "A traditional 401(k) is a retirement savings plan where contributions are made on a pre-tax basis. " \
                           "Withdrawals in retirement are subject to ordinary income tax."
            elif "self-employed 401(k)" in user_question:
                response = "A self-employed 401(k), also known as a solo 401(k) or individual 401(k), is a retirement plan " \
                           "designed for self-employed individuals or small business owners with no employees, " \
                           "except for a spouse in some cases."
            elif "maximum deductible contribution" in user_question:
                response = "For 2023, the maximum deductible contribution limit for a self-employed 401(k) " \
                           "is $64,000 for individuals under 50 and $70,000 for individuals aged 50 and above."
            elif "profit-sharing" in user_question:
                response = "Some employers may offer profit-sharing contributions to their employees' 401(k) accounts. " \
                           "These contributions are based on the company's profits and are determined by the employer's "
        self.conversation_display.insert(tk.END, "Investing Chatbot: " + response + "\n")
        self.conversation_display.configure(state='disabled')


# Create the main window
window = tk.Tk()
app = InvestingChatbot(window)

# Start the main loop
window.mainloop()
