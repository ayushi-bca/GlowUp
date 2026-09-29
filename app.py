import streamlit as st
from supabase import create_client, Client


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="GlowUp",
    page_icon="🌷",
    layout="wide"
)


# =========================================================
# SUPABASE CONNECTION
# =========================================================

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


# =========================================================
# DESIGN
# =========================================================

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


# =========================================================
# SESSION STATE
# =========================================================

if "user" not in st.session_state:
    st.session_state.user = None

if "data_loaded" not in st.session_state:
    st.session_state.data_loaded = False

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


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_user_id():
    return st.session_state.user.id


def load_user_data():

    user_id = get_user_id()

    # ---------------- PROFILE ----------------
    result = (
        supabase
        .table("profile")
        .select("*")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )

    if result.data:
        row = result.data[0]

        st.session_state.profile = {
            "name": row.get("name", "") or "",
            "age": row.get("age", "") or "",
            "height": row.get("height", "") or "",
            "weight": row.get("weight", "") or "",
            "goal": row.get("goal", "") or ""
        }

    # ---------------- SKINCARE ----------------
    result = (
        supabase
        .table("skincare")
        .select("*")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )

    if result.data:
        row = result.data[0]

        st.session_state.skincare = {
            "cleanser": bool(row.get("cleanser", False)),
            "moisturizer": bool(row.get("moisturizer", False)),
            "sunscreen": bool(row.get("sunscreen", False)),
            "serum": bool(row.get("serum", False))
        }

    # ---------------- HAIRCARE ----------------
    result = (
        supabase
        .table("haircare")
        .select("*")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )

    if result.data:
        row = result.data[0]

        st.session_state.haircare = {
            "hair_oil": bool(row.get("hair_oil", False)),
            "hair_wash": bool(row.get("hair_wash", False)),
            "shampoo": bool(row.get("shampoo", False)),
            "conditioner": bool(row.get("conditioner", False))
        }

    # ---------------- WATER ----------------
    result = (
        supabase
        .table("water")
        .select("*")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )

    if result.data:
        st.session_state.water = int(
            result.data[0].get("glasses", 0) or 0
        )

    # ---------------- EXERCISE ----------------
    result = (
        supabase
        .table("exercise")
        .select("*")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )

    if result.data:
        row = result.data[0]

        st.session_state.exercise = {
            "type": row.get("exercise_type", "") or "",
            "duration": int(row.get("duration", 0) or 0),
            "calories": int(row.get("calories", 0) or 0)
        }

    # ---------------- SLEEP ----------------
    result = (
        supabase
        .table("sleep")
        .select("*")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )

    if result.data:
        row = result.data[0]

        st.session_state.sleep = {
            "hours": float(row.get("hours", 0) or 0),
            "quality": row.get("quality", "") or ""
        }

    # ---------------- MOOD ----------------
    result = (
        supabase
        .table("mood")
        .select("*")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )

    if result.data:
        row = result.data[0]

        st.session_state.mood = {
            "mood": row.get("mood", "") or "",
            "note": row.get("note", "") or ""
        }

    st.session_state.data_loaded = True


# =========================================================
# LOGIN / SIGNUP
# =========================================================

if st.session_state.user is None:

    st.markdown(
        '<div class="glow-title">🌷 GlowUp</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Your personal self-care & wellness space ✨</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    login_tab, signup_tab = st.tabs(
        ["🔑 Login", "🌸 Create Account"]
    )

    # =====================================================
    # LOGIN
    # =====================================================

    with login_tab:

        st.subheader("Welcome back 🌷")

        email = st.text_input(
            "Email",
            placeholder="Enter your email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            key="login_password"
        )

        if st.button("💗 Login", key="login_button"):

            if not email or not password:
                st.warning("Please enter your email and password.")

            else:

                try:

                    response = supabase.auth.sign_in_with_password({
                        "email": email,
                        "password": password
                    })

                    if response.user:

                        st.session_state.user = response.user
                        st.session_state.data_loaded = False

                        load_user_data()

                        st.success("Welcome back! 🌷")

                        st.rerun()

                except Exception as e:

                    st.error(
                        "Login failed. Please check your email and password."
                    )

    # =====================================================
    # SIGN UP
    # =====================================================

    with signup_tab:

        st.subheader("Create your GlowUp account 🌸")

        new_email = st.text_input(
            "Email",
            placeholder="Enter your email",
            key="signup_email"
        )

        new_password = st.text_input(
            "Password",
            type="password",
            placeholder="Create a password",
            key="signup_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Enter password again",
            key="confirm_password"
        )

        if st.button("🌷 Create Account", key="signup_button"):

            if not new_email or not new_password:

                st.warning(
                    "Please enter an email and password."
                )

            elif new_password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            elif len(new_password) < 6:

                st.error(
                    "Password should contain at least 6 characters."
                )

            else:

                try:

                    response = supabase.auth.sign_up({
                        "email": new_email,
                        "password": new_password
                    })

                    if response.user:

                        # If email confirmation is disabled,
                        # Supabase gives us a session immediately.
                        if response.session:

                            st.session_state.user = response.user
                            st.session_state.data_loaded = False

                            load_user_data()

                            st.success(
                                "Account created successfully! 🌷"
                            )

                            st.rerun()

                        else:

                            st.success(
                                "Account created! Please check your email "
                                "to confirm your account, then login. 💗"
                            )

                except Exception as e:

                    st.error(
                        "Could not create account. "
                        "The email may already be registered."
                    )


    st.stop()


# =========================================================
# LOAD DATA AFTER LOGIN
# =========================================================

if not st.session_state.data_loaded:

    try:
        load_user_data()

    except Exception as e:

        st.error(
            "Could not load your data from Supabase."
        )


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("# 🌷 GlowUp")
st.sidebar.caption("self-care • wellness • you")

st.sidebar.markdown("---")

user_email = st.session_state.user.email

st.sidebar.caption(f"Logged in as:")
st.sidebar.write(user_email)

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

st.sidebar.markdown("---")

if st.sidebar.button("🚪 Logout"):

    try:
        supabase.auth.sign_out()
    except:
        pass

    st.session_state.user = None
    st.session_state.data_loaded = False

    st.rerun()


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    name = st.session_state.profile["name"]

    greeting = (
        f"Good morning, {name} 🌷"
        if name
        else "Good morning, Beautiful 🌷"
    )

    st.markdown(
        '<div class="glow-title">' +
        greeting +
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'A little self-care goes a long way ✨'
        '</div>',
        unsafe_allow_html=True
    )

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

                <p>
                🧴 Skincare —
                {"Completed ✓" if skincare_done else "Not completed"}
                </p>

                <p>
                💆 Haircare —
                {"Completed ✓" if haircare_done else "Not completed"}
                </p>

                <p>
                🏋️ Exercise —
                {"Completed ✓" if exercise_done else "Not completed"}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        sleep_hours = st.session_state.sleep["hours"]

        sleep_text = (
            f"{sleep_hours} hours"
            if sleep_hours > 0
            else "No sleep recorded yet"
        )

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

        mood_text = (
            mood
            if mood
            else "No mood recorded yet"
        )

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
                <p>
                You deserve the same care you give to everyone else. 🌷
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# PROFILE
# =========================================================

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

        try:

            user_id = get_user_id()

            supabase.table("profile").upsert(
                {
                    "user_id": user_id,
                    "name": name,
                    "age": age,
                    "height": height,
                    "weight": weight,
                    "goal": goal
                },
                on_conflict="user_id"
            ).execute()

            st.session_state.profile = {
                "name": name,
                "age": age,
                "height": height,
                "weight": weight,
                "goal": goal
            }

            st.success(
                "♡ Profile saved permanently!"
            )

        except Exception as e:

            st.error(
                "Could not save profile."
            )


# =========================================================
# SKINCARE
# =========================================================

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

        try:

            user_id = get_user_id()

            supabase.table("skincare").upsert(
                {
                    "user_id": user_id,
                    "cleanser": cleanser,
                    "moisturizer": moisturizer,
                    "sunscreen": sunscreen,
                    "serum": serum
                },
                on_conflict="user_id"
            ).execute()

            st.session_state.skincare = {
                "cleanser": cleanser,
                "moisturizer": moisturizer,
                "sunscreen": sunscreen,
                "serum": serum
            }

            st.success(
                "♡ Skincare routine saved permanently!"
            )

        except Exception as e:

            st.error(
                "Could not save skincare."
            )


# =========================================================
# HAIRCARE
# =========================================================

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

        try:

            user_id = get_user_id()

            supabase.table("haircare").upsert(
                {
                    "user_id": user_id,
                    "hair_oil": hair_oil,
                    "hair_wash": hair_wash,
                    "shampoo": shampoo,
                    "conditioner": conditioner
                },
                on_conflict="user_id"
            ).execute()

            st.session_state.haircare = {
                "hair_oil": hair_oil,
                "hair_wash": hair_wash,
                "shampoo": shampoo,
                "conditioner": conditioner
            }

            st.success(
                "♡ Haircare routine saved permanently!"
            )

        except Exception as e:

            st.error(
                "Could not save haircare."
            )


# =========================================================
# HYDRATION
# =========================================================

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

                try:

                    supabase.table("water").upsert(
                        {
                            "user_id": get_user_id(),
                            "glasses": st.session_state.water
                        },
                        on_conflict="user_id"
                    ).execute()

                except Exception:

                    st.error(
                        "Could not save hydration."
                    )

            st.rerun()

    with col2:

        if st.button("↩️ Remove 1 Glass"):

            if st.session_state.water > 0:

                st.session_state.water -= 1

                try:

                    supabase.table("water").upsert(
                        {
                            "user_id": get_user_id(),
                            "glasses": st.session_state.water
                        },
                        on_conflict="user_id"
                    ).execute()

                except Exception:

                    st.error(
                        "Could not save hydration."
                    )

            st.rerun()

    if st.session_state.water >= 8:

        st.success(
            "🎉 Daily water goal completed!"
        )


# =========================================================
# EXERCISE
# =========================================================

elif page == "🏋️ Exercise":

    st.title("🏋️ My Movement")

    st.write(
        "Move your body, boost your mood ✨"
    )

    st.markdown("---")

    st.subheader("🏋️ Today's Exercise")

    exercise = st.session_state.exercise

    options = [
        "Walking",
        "Running",
        "Gym",
        "Yoga",
        "Cycling",
        "Dancing"
    ]

    exercise_type = st.selectbox(
        "Exercise Type",
        options,
        index=(
            options.index(exercise["type"])
            if exercise["type"] in options
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

        try:

            user_id = get_user_id()

            supabase.table("exercise").upsert(
                {
                    "user_id": user_id,
                    "exercise_type": exercise_type,
                    "duration": duration,
                    "calories": calories
                },
                on_conflict="user_id"
            ).execute()

            st.session_state.exercise = {
                "type": exercise_type,
                "duration": duration,
                "calories": calories
            }

            st.success(
                "♡ Exercise saved permanently!"
            )

        except Exception as e:

            st.error(
                "Could not save exercise."
            )


# =========================================================
# SLEEP
# =========================================================

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

    quality_index = (
        quality_options.index(sleep["quality"])
        if sleep["quality"] in quality_options
        else 0
    )

    quality = st.selectbox(
        "Sleep Quality",
        quality_options,
        index=quality_index
    )

    if st.button("💗 Save Sleep"):

        try:

            user_id = get_user_id()

            supabase.table("sleep").upsert(
                {
                    "user_id": user_id,
                    "hours": hours,
                    "quality": quality
                },
                on_conflict="user_id"
            ).execute()

            st.session_state.sleep = {
                "hours": hours,
                "quality": quality
            }

            st.success(
                "♡ Sleep saved permanently!"
            )

        except Exception as e:

            st.error(
                "Could not save sleep."
            )


# =========================================================
# MOOD
# =========================================================

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

    mood_index = (
        mood_options.index(mood["mood"])
        if mood["mood"] in mood_options
        else 0
    )

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

        try:

            user_id = get_user_id()

            supabase.table("mood").upsert(
                {
                    "user_id": user_id,
                    "mood": selected_mood,
                    "note": note
                },
                on_conflict="user_id"
            ).execute()

            st.session_state.mood = {
                "mood": selected_mood,
                "note": note
            }

            st.success(
                "♡ Mood saved permanently!"
            )

        except Exception as e:

            st.error(
                "Could not save mood."
            )


# =========================================================
# PROGRESS
# =========================================================

elif page == "📊 My Progress":

    st.title("📊 My Progress")

    st.write(
        "See your self-care journey at a glance 🌷"
    )

    st.markdown("---")

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

    col1, col2, col3 = st.columns(3)

    cards = [
        (
            "💧",
            "Hydration",
            hydration_done,
            f"{st.session_state.water}/8 glasses"
        ),
        (
            "🧴",
            "Skincare",
            skincare_done,
            ""
        ),
        (
            "💆",
            "Haircare",
            haircare_done,
            ""
        ),
        (
            "🏋️",
            "Exercise",
            exercise_done,
            f'{st.session_state.exercise["duration"]} minutes'
        ),
        (
            "🌙",
            "Sleep",
            sleep_done,
            f'{st.session_state.sleep["hours"]} hours'
        ),
        (
            "😊",
            "Mood",
            mood_done,
            st.session_state.mood["mood"]
        )
    ]

    for i, (icon, title, done, detail) in enumerate(cards):

        col = [
            col1,
            col2,
            col3
        ][i % 3]

        with col:

            status = (
                "✓ Completed"
                if done
                else "Not completed"
            )

            st.markdown(
                f"""
                <div class="small-card">

                    <h3>
                    {icon} {title}
                    </h3>

                    <p>
                    {status}
                    </p>

                    <p>
                    {detail}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )