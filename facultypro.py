import streamlit as st


def main():
    st.set_page_config(page_title="Faculty Profile Website", layout="wide")

    # Sidebar navigation
    page = st.sidebar.radio("Navigation", ["Profile"])

    if page == "Home":
        home_page()
    elif page == "Profile":
        profile_page()

# def home_page():
#     st.title("Welcome to my Faculty Profile page")
#     st.write("This website showcases my profiel.")

def profile_page():
    faculty_info = {
        'name': 'Dr. Niduthavolu Saikiran Kumar',
        'title': 'Assistant Professor of Marketing',
        'education': 'Ph.D. in Marketing Analytics, National Institute of Technology,Tiruchirapalli',
        'research_interests': ['Text Analytics', 'Information System Theories', 'Machine Learning','Ecommerce','Online Consumer Behavior'],
        'courses': ['MGT 3987: Machine Learning using Python ', 'MGT3912: Ecommerce Management','MGT3995: Machine Learning Applications in Marketing','MGT3992: Marketing Research Analytics and Methods','MGT3099: Retail Analytics'],
        'publications': [
            'P, S., Niduthavolu, S. and Vedanthachari, L.N. (2021), "Analysis of content strategies of selected brand tweets and its influence on information diffusion", Journal of Advances in Management Research, Vol. 18 No. 2, pp. 227-249. https://doi.org/10.1108/JAMR-06-2020-0107',
            'An analysis of the brand content characteristics across high and low involvement product categories and their influence on information diffusion on TwittP. Sridevi, N. Saikiran Kumar, and Lakshmi Narasimhan Vedanthachari,International Journal of Business Innovation and Research 2024 33:2, 168-191,https://doi.org/10.1504/IJBIR.2024.136440',
        'Niduthavolu, S. and Airani, R. (2024), "Impact of values on the continual intention of mobile health apps: a text mining perspective", Global Knowledge, Memory and Communication, Vol. ahead-of-print No. ahead-of-print. https://doi.org/10.1108/GKMC-01-2024-0038']
    }

    st.title(faculty_info['name'])
    st.subheader(faculty_info['title'])

    st.write(f"**Education:** {faculty_info['education']}")

    st.header("Research Interests")
    for interest in faculty_info['research_interests']:
        st.write(f"- {interest}")

    st.header("Courses Taught")
    for course in faculty_info['courses']:
        st.write(f"- {course}")

    st.header("Selected Publications")
    for publication in faculty_info['publications']:
        st.write(f"- {publication}")

if __name__ == "__main__":
    main()
    