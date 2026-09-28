import streamlit as st

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="GlowUp",
    page_icon="🌷",
    layout="wide"
)

# ==========================================
# CUSTOM STYLE
# ==========================================

st.markdown("""
<style>

body {
    background-color: #FDF7F5;
}

.main {
    background-color: #FDF7F5;
}

h1, h2, h3 {
    color: #6B4A4A;
}

.glow-title {
    font-size: 42px;
    font-weight: bold;
    color: #6B4A4A;
}

.subtitle {
    font-size: 18px;
    color: #9B7B7B;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 22px;
    margin-bottom: 20px;
    border: 1px solid #E5C8CC;
}

.small-card {
    background-color: white;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #E5C8CC;
    text-align: center;
}

.stButton > button {
    background-color: #D9A7B0;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 22px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #C98F9A;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SESSION DATA
# ==========================================

if "profile" not in st.session_state:
    st.session_state.profile = {
        "name": "",
        "age": "",
        "height": "",
        "weight": "",
        "goal": ""
    }

if "skincare" not in st.session_state:
    st.session_state.skincare = {
        "cleanser": False,
        "moisturizer": False,
        "sunscreen": False,
        "serum": False
    }

if "haircare" not in st.session_state:
    st.session_state.haircare = {
        "hair_oil": False,
        "hair_wash": False,
        "shampoo": False,
        "conditioner": False
    }

if "water" not in st.session_state:
    st.session_state.water = 0

if "exercise" not in st.session_state:
    st.session_state.exercise = {
        "type": "",
        "duration": 0,
        "calories": 0
    }

if "sleep" not in st.session_state:
    st.session_state.sleep = {
        "hours": 0.0,
        "quality": ""
    }

if "mood" not in st.session_state:
    st.session_state.mood = {
        "mood": "",
        "note": ""
    }


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown("# 🌷 GlowUp")

st.sidebar.caption("self-care • wellness • you")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "MY SPACE",
    [
        "🏠 Home",
        "👤 My Profile",
        "🧴 Skincare",
        "💆 Haircare",
        "💧 Hydration",
        "🏋️ Exercise",
        "🌙 Sleep",
        "😊 Mood",
        "📊 My Progress"
    ]
)


# ==========================================
# HOME
# ==========================================

if page == "🏠 Home":

    name = st.session_state.profile["name"]

    if name:
        greeting = f"Good morning, {name} 🌷"
    else:
        greeting = "Good morning, Beautiful 🌷"

    st.markdown(
        f'<div class="glow-title">{greeting}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">A little self-care goes a long way ✨</div>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div class="card">
                <h2>💧 Hydration</h2>
                <h3>{st.session_state.water} / 8 glasses</h3>
                <p>Keep your body hydrated 💗</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        skincare_done = any(
            st.session_state.skincare.values()
        )

        haircare_done = any(
            st.session_state.haircare.values()
        )

        exercise_done = (
            st.session_state.exercise["type"] != ""
        )

        st.markdown(
            f"""
            <div class="card">
                <h2>🌸 Today's Self-Care</h2>
                <p>🧴 Skincare — {"Completed ✓" if skincare_done else "Not completed"}</p>
                <p>💆 Haircare — {"Completed ✓" if haircare_done else "Not completed"}</p>
                <p>🏋️ Exercise — {"Completed ✓" if exercise_done else "Not completed"}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        sleep_hours = st.session_state.sleep["hours"]

        if sleep_hours > 0:
            sleep_text = f"{sleep_hours} hours"
        else:
            sleep_text = "No sleep recorded yet"

        st.markdown(
            f"""
            <div class="card">
                <h2>🌙 Sleep</h2>
                <p>{sleep_text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        mood = st.session_state.mood["mood"]

        if mood:
            mood_text = mood
        else:
            mood_text = "No mood recorded yet"

        st.markdown(
            f"""
            <div class="card">
                <h2>😊 Today's Mood</h2>
                <p>{mood_text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
                <h2>✨ Little Reminder</h2>
                <p>You deserve the same care you give to everyone else. 🌷</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==========================================
# PROFILE
# ==========================================

elif page == "👤 My Profile":

    st.title("🌷 My GlowUp Profile")

    st.write(
        "Your little space for wellness & self-care ✨"
    )

    st.markdown("---")

    st.subheader("👤 Personal Information")

    profile = st.session_state.profile

    name = st.text_input(
        "Name",
        value=profile["name"],
        placeholder="Enter your name"
    )

    age = st.text_input(
        "Age",
        value=profile["age"],
        placeholder="Enter your age"
    )

    height = st.text_input(
        "Height",
        value=profile["height"],
        placeholder="e.g. 5'3"
    )

    weight = st.text_input(
        "Weight",
        value=profile["weight"],
        placeholder="e.g. 56.6 kg"
    )

    goal = st.text_input(
        "Personal Goal",
        value=profile["goal"],
        placeholder="e.g. Stay healthy & active"
    )

    if st.button("💗 Save My Profile"):

        st.session_state.profile = {
            "name": name,
            "age": age,
            "height": height,
            "weight": weight,
            "goal": goal
        }

        st.success("♡ Profile saved successfully!")


# ==========================================
# SKINCARE
# ==========================================

elif page == "🧴 Skincare":

    st.title("🧴 My Skincare Ritual")

    st.write(
        "A little care for your skin, every day ✨"
    )

    st.markdown("---")

    st.subheader("🌸 Today's Skincare")

    skincare = st.session_state.skincare

    cleanser = st.checkbox(
        "🫧 Cleanser",
        value=skincare["cleanser"]
    )

    moisturizer = st.checkbox(
        "💧 Moisturizer",
        value=skincare["moisturizer"]
    )

    sunscreen = st.checkbox(
        "☀️ Sunscreen",
        value=skincare["sunscreen"]
    )

    serum = st.checkbox(
        "✨ Serum",
        value=skincare["serum"]
    )

    if st.button("💗 Save Skincare"):

        st.session_state.skincare = {
            "cleanser": cleanser,
            "moisturizer": moisturizer,
            "sunscreen": sunscreen,
            "serum": serum
        }

        st.success("♡ Skincare routine saved!")


# ==========================================
# HAIRCARE
# ==========================================

elif page == "💆 Haircare":

    st.title("💆 My Haircare Ritual")

    st.write(
        "Healthy hair starts with little routines 🌸"
    )

    st.markdown("---")

    st.subheader("🌷 Today's Haircare")

    haircare = st.session_state.haircare

    hair_oil = st.checkbox(
        "🪻 Hair Oil",
        value=haircare["hair_oil"]
    )

    hair_wash = st.checkbox(
        "🚿 Hair Wash",
        value=haircare["hair_wash"]
    )

    shampoo = st.checkbox(
        "🫧 Shampoo",
        value=haircare["shampoo"]
    )

    conditioner = st.checkbox(
        "💧 Conditioner",
        value=haircare["conditioner"]
    )

    if st.button("💗 Save Haircare"):

        st.session_state.haircare = {
            "hair_oil": hair_oil,
            "hair_wash": hair_wash,
            "shampoo": shampoo,
            "conditioner": conditioner
        }

        st.success("♡ Haircare routine saved!")


# ==========================================
# HYDRATION
# ==========================================

elif page == "💧 Hydration":

    st.title("💧 Hydration")

    st.write(
        "Small sips, happy body ✨"
    )

    st.markdown("---")

    st.subheader("💧 Today's Water")

    water = st.session_state.water

    st.markdown(
        f"""
        <div class="card">
            <h2>💧 {water} / 8 glasses</h2>
            <p>Daily hydration goal</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("💧 Add 1 Glass"):

            if st.session_state.water < 8:
                st.session_state.water += 1

            st.rerun()

    with col2:

        if st.button("↩️ Remove 1 Glass"):

            if st.session_state.water > 0:
                st.session_state.water -= 1

            st.rerun()

    if st.session_state.water >= 8:
        st.success("🎉 Daily water goal completed!")


# ==========================================
# EXERCISE
# ==========================================

elif page == "🏋️ Exercise":

    st.title("🏋️ My Movement")

    st.write(
        "Move your body, boost your mood ✨"
    )

    st.markdown("---")

    st.subheader("🏋️ Today's Exercise")

    exercise = st.session_state.exercise

    exercise_type = st.selectbox(
        "Exercise Type",
        [
            "Walking",
            "Running",
            "Gym",
            "Yoga",
            "Cycling",
            "Dancing"
        ],
        index=(
            [
                "Walking",
                "Running",
                "Gym",
                "Yoga",
                "Cycling",
                "Dancing"
            ].index(exercise["type"])
            if exercise["type"] in [
                "Walking",
                "Running",
                "Gym",
                "Yoga",
                "Cycling",
                "Dancing"
            ]
            else 0
        )
    )

    duration = st.number_input(
        "Duration (minutes)",
        min_value=0,
        max_value=300,
        value=exercise["duration"]
    )

    calories = st.number_input(
        "Calories Burned",
        min_value=0,
        max_value=2000,
        value=exercise["calories"]
    )

    if st.button("💗 Save Exercise"):

        st.session_state.exercise = {
            "type": exercise_type,
            "duration": duration,
            "calories": calories
        }

        st.success("♡ Exercise saved successfully!")


# ==========================================
# SLEEP
# ==========================================

elif page == "🌙 Sleep":

    st.title("🌙 My Sleep")

    st.write(
        "Rest well, wake up refreshed ✨"
    )

    st.markdown("---")

    st.subheader("🌙 Today's Sleep")

    sleep = st.session_state.sleep

    hours = st.number_input(
        "Hours of Sleep",
        min_value=0.0,
        max_value=24.0,
        value=sleep["hours"],
        step=0.5
    )

    quality_options = [
        "Excellent",
        "Good",
        "Average",
        "Poor"
    ]

    if sleep["quality"] in quality_options:
        quality_index = quality_options.index(
            sleep["quality"]
        )
    else:
        quality_index = 0

    quality = st.selectbox(
        "Sleep Quality",
        quality_options,
        index=quality_index
    )

    if st.button("💗 Save Sleep"):

        st.session_state.sleep = {
            "hours": hours,
            "quality": quality
        }

        st.success("♡ Sleep saved successfully!")


# ==========================================
# MOOD
# ==========================================

elif page == "😊 Mood":

    st.title("😊 My Mood")

    st.write(
        "Check in with yourself today 🌸"
    )

    st.markdown("---")

    st.subheader("💗 How are you feeling?")

    mood = st.session_state.mood

    mood_options = [
        "😊 Happy",
        "🥰 Loved",
        "😌 Calm",
        "😐 Okay",
        "😔 Sad",
        "😫 Stressed",
        "😴 Tired",
        "🤩 Excited"
    ]

    if mood["mood"] in mood_options:
        mood_index = mood_options.index(
            mood["mood"]
        )
    else:
        mood_index = 0

    selected_mood = st.selectbox(
        "Today's Mood",
        mood_options,
        index=mood_index
    )

    note = st.text_area(
        "Write a little note",
        value=mood["note"],
        placeholder="How was your day?"
    )

    if st.button("💗 Save Mood"):

        st.session_state.mood = {
            "mood": selected_mood,
            "note": note
        }

        st.success("♡ Mood saved successfully!")


# ==========================================
# PROGRESS
# ==========================================

elif page == "📊 My Progress":

    st.title("📊 My Progress")

    st.write(
        "See your self-care journey at a glance 🌷"
    )

    st.markdown("---")

    # Calculate completed activities

    hydration_done = (
        st.session_state.water >= 8
    )

    skincare_done = any(
        st.session_state.skincare.values()
    )

    haircare_done = any(
        st.session_state.haircare.values()
    )

    exercise_done = (
        st.session_state.exercise["type"] != ""
    )

    sleep_done = (
        st.session_state.sleep["hours"] > 0
    )

    mood_done = (
        st.session_state.mood["mood"] != ""
    )

    completed = sum([
        hydration_done,
        skincare_done,
        haircare_done,
        exercise_done,
        sleep_done,
        mood_done
    ])

    total = 6

    percentage = int(
        (completed / total) * 100
    )

    # ======================================
    # SCORE
    # ======================================

    st.markdown(
        f"""
        <div class="card">
            <h2>🌷 Today's Self-Care Score</h2>
            <h1>{completed} / {total}</h1>
            <p>{percentage}% completed today</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(
        percentage / 100
    )

    st.write("")

    # ======================================
    # ACTIVITY CARDS
    # ======================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="small-card">
                <h3>💧 Hydration</h3>
                <p>{"✓ Completed" if hydration_done else "Not completed"}</p>
                <p>{st.session_state.water}/8 glasses</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="small-card">
                <h3>🧴 Skincare</h3>
                <p>{"✓ Completed" if skincare_done else "Not completed"}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="small-card">
                <h3>💆 Haircare</h3>
                <p>{"✓ Completed" if haircare_done else "Not completed"}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="small-card">
                <h3>🏋️ Exercise</h3>
                <p>{"✓ Completed" if exercise_done else "Not completed"}</p>
                <p>{st.session_state.exercise["duration"]} minutes</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="small-card">
                <h3>🌙 Sleep</h3>
                <p>{"✓ Completed" if sleep_done else "Not completed"}</p>
                <p>{st.session_state.sleep["hours"]} hours</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="small-card">
                <h3>😊 Mood</h3>
                <p>{"✓ Completed" if mood_done else "Not completed"}</p>
                <p>{st.session_state.mood["mood"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # ======================================
    # SUMMARY
    # ======================================

    st.markdown(
        """
        <div class="card">
            <h2>✨ Keep Going</h2>
            <p>
            Every small step counts. Take care of yourself,
            one day at a time. 🌷
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )