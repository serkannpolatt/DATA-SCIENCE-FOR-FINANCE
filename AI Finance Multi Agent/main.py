import dotenv
import os
import streamlit as st
from llama_index.llms.groq import Groq
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import ReActAgent
from datetime import date
import yfinance as yf

# Load environment variables
dotenv.load_dotenv("dotenv")
groq_api_key = os.environ["GROQ_API_KEY"]

# Initialize Llama Model
llama3 = Groq(model="llama-3.1-70b-versatile", api_key=groq_api_key, temperature=0)


def flatten_dict(mapping: dict, prefix="") -> str:
    total_txt = ""
    for key, val in mapping.items():
        if type(val) in [str, float, int]:
            total_txt += f"{prefix}{key} - {val}\n"
        elif isinstance(val, dict):
            total_txt += f"{key}\n"
            total_txt += flatten_dict(val, prefix="\t")
        elif isinstance(val, list):
            if isinstance(val[0], dict):
                total_txt += f"{key}\n"
                for v in val:
                    total_txt += flatten_dict(v, prefix="\t")
            else:
                total_txt += f"{key} - {val}\n"
    return total_txt


# Existing Functions


def company_information(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    ticker_info = ticker_obj.get_info()
    return flatten_dict(ticker_info)


def summary_of_mutual_fund_holders(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    mf_holders = ticker_obj.get_mutualfund_holders()
    return "\n\n".join(
        [flatten_dict(record) for record in mf_holders.to_dict(orient="records")]
    )


def summary_of_institutional_holders(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    inst_holders = ticker_obj.get_institutional_holders()
    return "\n\n".join(
        [flatten_dict(record) for record in inst_holders.to_dict(orient="records")]
    )


def stock_grade_updrages_downgrades(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    curr_year = date.today().year
    upgrades_downgrades = ticker_obj.get_upgrades_downgrades()
    upgrades_downgrades = upgrades_downgrades.loc[
        upgrades_downgrades.index > f"{curr_year}-01-01"
    ]
    upgrades_downgrades = upgrades_downgrades[
        upgrades_downgrades["Action"].isin(["up", "down"])
    ]
    return "\n\n".join(
        [
            flatten_dict(record)
            for record in upgrades_downgrades.to_dict(orient="records")
        ]
    )


def stock_splits_history(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    hist_splits = ticker_obj.get_splits()
    return flatten_dict(hist_splits.to_dict())


def stock_news(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    news_links = ticker_obj.get_news()
    for news in news_links:
        if "thumbnail" in news:
            news.pop("thumbnail")
        if "uuid" in news:
            news.pop("uuid")
    return "\n\n".join([flatten_dict(news) for news in news_links])


# New Functions


def stock_price_history(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    hist_price = ticker_obj.history(period="1y")  # Son 1 yıl
    return flatten_dict(hist_price.tail(10).to_dict())  # Son 10 kayıt


def stock_dividends(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    dividends = ticker_obj.dividends
    return flatten_dict(dividends.to_dict())


def income_statement(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    income_stmt = ticker_obj.financials
    return flatten_dict(income_stmt.to_dict())


def balance_sheet(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    balance_sheet = ticker_obj.balance_sheet
    return flatten_dict(balance_sheet.to_dict())


def cash_flow_statement(ticker: str) -> dict:
    ticker_obj = yf.Ticker(ticker)
    cash_flow = ticker_obj.cashflow
    return flatten_dict(cash_flow.to_dict())


def pe_ratio(ticker: str) -> str:
    ticker_obj = yf.Ticker(ticker)
    pe_ratio = ticker_obj.info.get("trailingPE", "Mevcut değil")
    return f"P/E Oranı: {pe_ratio}"


def stock_price_on_date(ticker: str, query_date: str) -> str:
    ticker_obj = yf.Ticker(ticker)
    hist = ticker_obj.history(start=query_date, end=query_date)
    if hist.empty:
        return "Belirtilen tarihte hisse senedi fiyatı bulunamadı."
    else:
        return f"{query_date} tarihinde hisse senedi fiyatı: {hist['Close'][0]}"


# Existing Tools
company_information_tool = FunctionTool.from_defaults(fn=company_information)
summary_of_mutual_fund_holders_tool = FunctionTool.from_defaults(
    fn=summary_of_mutual_fund_holders
)
summary_of_institutional_holders_tool = FunctionTool.from_defaults(
    fn=summary_of_institutional_holders
)
stock_grade_updrages_downgrades_tool = FunctionTool.from_defaults(
    fn=stock_grade_updrages_downgrades
)
stock_splits_history_tool = FunctionTool.from_defaults(fn=stock_splits_history)
stock_news_tool = FunctionTool.from_defaults(fn=stock_news)

# New Tools
stock_price_history_tool = FunctionTool.from_defaults(fn=stock_price_history)
stock_dividends_tool = FunctionTool.from_defaults(fn=stock_dividends)
income_statement_tool = FunctionTool.from_defaults(fn=income_statement)
balance_sheet_tool = FunctionTool.from_defaults(fn=balance_sheet)
cash_flow_statement_tool = FunctionTool.from_defaults(fn=cash_flow_statement)
pe_ratio_tool = FunctionTool.from_defaults(fn=pe_ratio)
stock_price_on_date_tool = FunctionTool.from_defaults(fn=stock_price_on_date)

# Extend the tool list with the new tools
tools = [
    company_information_tool,
    summary_of_mutual_fund_holders_tool,
    summary_of_institutional_holders_tool,
    stock_grade_updrages_downgrades_tool,
    stock_splits_history_tool,
    stock_news_tool,
    stock_price_history_tool,
    stock_dividends_tool,
    income_statement_tool,
    balance_sheet_tool,
    cash_flow_statement_tool,
    pe_ratio_tool,
    stock_price_on_date_tool,
]

finance_agent = ReActAgent.from_tools(
    tools=tools, llm=llama3, verbose=True, max_iterations=5
)

# Streamlit app
st.title("Finance Agent")
st.write("Aşağıya hisse senedi hakkında sorularınızı girin:")

query = st.text_input("Soru", "")

if query:
    try:
        response = finance_agent.query(query)
        # response içinden sadece yanıtı yazdır
        st.write(response.response)
    except ValueError as e:
        st.error(f"Error: {str(e)}. Lütfen soruyu netleştirin veya yeniden deneyin.")
