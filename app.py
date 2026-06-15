import streamlit as st
from datetime import datetime

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="TripWise AI",
    page_icon="✈️",
    layout="wide"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
.hero{
    background: linear-gradient(135deg,#0ea5e9,#2563eb);
    padding:2rem;
    border-radius:15px;
    color:white;
    text-align:center;
    margin-bottom:20px;
}
.metric-card{
    background:#f8fafc;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #2563eb;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Hero Section
# -------------------------
st.markdown("""
<div class="hero">
    <h1>✈️ TripWise AI</h1>
    <h3>AI-Powered Smart Travel Planner</h3>
    <p>Create personalized itineraries in seconds.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Sidebar Inputs
# -------------------------
st.sidebar.header("Travel Preferences")

destination = st.sidebar.text_input(
    "Destination",
    placeholder="Goa, Paris, Tokyo..."
)

days = st.sidebar.slider(
    "Trip Duration (Days)",
    1,
    14,
    3
)

budget = st.sidebar.selectbox(
    "Budget Level",
    ["Budget", "Mid-Range", "Luxury"]
)

travel_style = st.sidebar.selectbox(
    "Travel Style",
    [
        "Adventure",
        "Culture",
        "Relaxation",
        "Food & Dining",
        "Family",
        "Business"
    ]
)

interests = st.sidebar.multiselect(
    "Interests",
    [
        "Beaches",
        "Museums",
        "Nature",
        "Shopping",
        "Nightlife",
        "Local Food",
        "Historic Sites"
    ]
)

generate = st.sidebar.button(
    "Generate Itinerary",
    use_container_width=True
)

# -------------------------
# Budget Estimates
# -------------------------
budget_data = {
    "Budget": {
        "hotel": 1500,
        "food": 600,
        "transport": 400
    },
    "Mid-Range": {
        "hotel": 3500,
        "food": 1200,
        "transport": 800
    },
    "Luxury": {
        "hotel": 8000,
        "food": 2500,
        "transport": 2000
    }
}

# -------------------------
# Itinerary Generator
# -------------------------
def generate_day_plan(day, style):

    plans = {
        "Adventure": {
            "Morning": "Outdoor adventure activity",
            "Afternoon": "Nature exploration",
            "Evening": "Local market visit"
        },
        "Culture": {
            "Morning": "Museum visit",
            "Afternoon": "Historic site exploration",
            "Evening": "Cultural performance"
        },
        "Relaxation": {
            "Morning": "Resort breakfast",
            "Afternoon": "Spa and leisure",
            "Evening": "Sunset relaxation"
        },
        "Food & Dining": {
            "Morning": "Local breakfast tour",
            "Afternoon": "Street food exploration",
            "Evening": "Fine dining experience"
        },
        "Family": {
            "Morning": "Family attraction",
            "Afternoon": "Theme park or zoo",
            "Evening": "Family dinner"
        },
        "Business": {
            "Morning": "Work commitments",
            "Afternoon": "City exploration",
            "Evening": "Networking dinner"
        }
    }

    return plans.get(style)

# -------------------------
# Main Content
# -------------------------
if generate:

    if destination.strip() == "":
        st.error("Please enter a destination.")
        st.stop()

    st.success(
        f"Personalized itinerary generated for {destination}"
    )

    st.header("📍 Travel Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Destination", destination)

    with col2:
        st.metric("Duration", f"{days} Days")

    with col3:
        st.metric("Budget", budget)

    # ---------------------
    # Cost Calculation
    # ---------------------
    hotel_cost = budget_data[budget]["hotel"] * days
    food_cost = budget_data[budget]["food"] * days
    transport_cost = budget_data[budget]["transport"] * days

    total_cost = (
        hotel_cost +
        food_cost +
        transport_cost
    )

    st.header("💰 Estimated Cost Breakdown")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Hotel", f"₹{hotel_cost:,}")
    c2.metric("Food", f"₹{food_cost:,}")
    c3.metric("Transport", f"₹{transport_cost:,}")
    c4.metric("Total", f"₹{total_cost:,}")

    # ---------------------
    # Daily Itinerary
    # ---------------------
    st.header("🗓️ Day-by-Day Itinerary")

    for day in range(1, days + 1):

        plan = generate_day_plan(
            day,
            travel_style
        )

        with st.expander(f"Day {day}"):

            st.write(
                f"### Morning\n✅ {plan['Morning']}"
            )

            st.write(
                f"### Afternoon\n✅ {plan['Afternoon']}"
            )

            st.write(
                f"### Evening\n✅ {plan['Evening']}"
            )

    # ---------------------
    # Weather Insight
    # ---------------------
    st.header("🌦️ Travel Insights")

    st.info(
        "Check local weather before departure. "
        "Carry essentials and verify attraction timings."
    )

    # ---------------------
    # Crowd Insight
    # ---------------------
    st.warning(
        "Visit major attractions early morning "
        "to avoid peak crowds."
    )

    # ---------------------
    # Interest Summary
    # ---------------------
    if interests:

        st.header("🎯 Selected Interests")

        for item in interests:
            st.write(f"• {item}")

    # ---------------------
    # Export Section
    # ---------------------
    itinerary_text = f"""
TripWise AI Travel Plan

Destination: {destination}
Duration: {days} Days
Budget: {budget}
Travel Style: {travel_style}

Estimated Total Cost: ₹{total_cost:,}
"""

    st.download_button(
        "📥 Download Itinerary",
        itinerary_text,
        file_name="tripwise_itinerary.txt",
        mime="text/plain"
    )

else:

    st.header("Welcome to TripWise AI")

    st.write("""
    Generate personalized travel plans based on:

    • Destination

    • Budget

    • Trip Duration

    • Travel Style

    • Personal Interests

    Click **Generate Itinerary** to begin.
    """)

    st.image(
        "https://images.unsplash.com/photo-1488646953014-85cb44e25828",
        use_container_width=True
    )