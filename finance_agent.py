from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_company_sumbol(company: str) -> str:
    """Use this function to get the symbol for a company

    Args: 
        company (str): The name of the company.
    """
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN"
    }
    return symbols.get(company, 'Unknown')

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, stock_fundamentals=True), get_company_sumbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data", 
    "If you don't know the company symbol, please use use_get_company_symbol tool, even if it is not a public company"],
    debug_mode=True,
)

agent.print_response("Summarize & compare analyst recommendations & fundamentals for TSLA & Phidata")