import streamlit as st
from openai import OpenAI

client = OpenAI(api_key='my-api-key-here') 

# Create the main page
st.title("Foot Traffic Intelligence: Optimize Visits and Empower Businesses")
st.write("Upload your foot traffic data to get insights tailored for businesses.")

# Input for business name
business_name = st.text_input("Enter your business name:")

# Input for location
location = st.text_input("Enter the location for foot traffic data (e.g., 'New York, NY'):")

# Input for Yelp business ID
yelp_url = st.text_input("Enter the Yelp business URL (find it on your business's Yelp page):")

# Wrapper function to interact with OpenAI
def get_completion(prompt, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system",
             "content": "Your role is to provide specific, data-driven recommendations tailored to each business for improvement. Based on the provided problem, research the business's current online presence, customer reviews, financial data (if available), industry trends, and any relevant market data from the internet. Use this information to create actionable insights in the following areas:\
                        Financial Health: Offer strategies to optimize costs and increase revenue tailored to the business type and industry, informed by recent financial data or industry benchmarks. Consider cost-cutting measures, upselling or cross-selling opportunities, and any specific financial advice based on market data.\
                        Employee Management: Provide suggestions for efficient staff management that improves customer service and productivity. Use data on peak hours, customer reviews, and industry standards to recommend scheduling adjustments, employee training, or performance incentives that align with the business’s needs.\
                        Advertising: Recommend advertising strategies tailored to the business and its audience, based on their online presence, customer demographics, and social media activity. Include targeted social media marketing, local promotions, and partnerships aligned with the business’s customer base and peak times to enhance visibility and attract foot traffic."},
            {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content

# Define a function to generate summary and insights
def generate_summary_and_insights(business_name, location, yelp_url, insight_topic):
    prompt = (f"Provide a brief summary of the business named {business_name} located in {location}. "
              f"Using details from {yelp_url}, summarize foot traffic trends and customer reviews. "
              f"Then, generate insights specifically focused on {insight_topic}.")
    insights = get_completion(prompt)
    return insights

st.button("Submit")

# Display business summary and insights
if business_name and location and yelp_url:
    # Generate and display summary
    st.subheader("Business Summary")
    summary_prompt = (f"Provide a brief summary of the business named {business_name} located in {location}, "
                      f"based on information from its Yelp page at {yelp_url}.")
    summary = get_completion(summary_prompt)
    st.write(summary)

    # Display buttons for insight areas after showing summary
    st.write("### Select an Insight Area:")
    if st.button("Financial Health"):
        financial_health_insights = generate_summary_and_insights(business_name, location, yelp_url, "Financial Health")
        st.subheader("Financial Health Insights")
        st.write(financial_health_insights)

    if st.button("Employee Management"):
        employee_management_insights = generate_summary_and_insights(business_name, location, yelp_url, "Employee Management")
        st.subheader("Employee Management Insights")
        st.write(employee_management_insights)

    if st.button("Advertising Strategies"):
        advertising_insights = generate_summary_and_insights(business_name, location, yelp_url, "Advertising Strategies")
        st.subheader("Advertising Strategies Insights")
        st.write(advertising_insights)