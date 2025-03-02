import streamlit as st
import datetime
# Page configuration
st.set_page_config(page_title="Ramadan Tracker 2025", page_icon="🌙", layout="wide")

# Beautiful Header
st.markdown(
    """
    <h1 style='text-align: center; color: #FFD700;'>🌙 Ramadan Tracker 2025 🌙</h1>
    <h3 style='text-align: center; color: #FFD700;;'>Get Sehri & Iftar timings for Karachi</h3>
    """,
    unsafe_allow_html=True,
)

# Karachi Ramadan Calendar 2025
ramadan_calendar = {
    datetime.date(2025, 3, 2): ("05:37 AM", "6:36 PM"),
    datetime.date(2025, 3, 3): ("05:36 AM", "6:36 PM"),
    datetime.date(2025, 3, 4): ("05:35 AM", "6:37 PM"),
    datetime.date(2025, 3, 5): ("05:34 AM", "6:37 PM"),
    datetime.date(2025, 3, 6): ("05:33 AM", "6:38 PM"),
    datetime.date(2025, 3, 7): ("05:32 AM", "6:38 PM"),
    datetime.date(2025, 3, 8): ("05:31 AM", "6:39 PM"),
    datetime.date(2025, 3, 9): ("05:30 AM", "6:39 PM"),
    datetime.date(2025, 3, 10): ("05:29 AM", "6:39 PM"),
    datetime.date(2025, 3, 11): ("05:28 AM", "6:40 PM"),
    datetime.date(2025, 3, 12): ("05:27 AM", "6:40 PM"),
    datetime.date(2025, 3, 13): ("05:26 AM", "6:41 PM"),
    datetime.date(2025, 3, 14): ("05:25 AM", "6:41 PM"),
    datetime.date(2025, 3, 15): ("05:24 AM", "6:42 PM"),
    datetime.date(2025, 3, 16): ("05:23 AM", "6:42 PM"),
    datetime.date(2025, 3, 17): ("05:22 AM", "6:43 PM"),
    datetime.date(2025, 3, 18): ("05:21 AM", "6:43 PM"),
    datetime.date(2025, 3, 19): ("05:20 AM", "6:44 PM"),
    datetime.date(2025, 3, 20): ("05:19 AM", "6:44 PM"),
    datetime.date(2025, 3, 21): ("05:18 AM", "6:44 PM"),
    datetime.date(2025, 3, 22): ("05:17 AM", "6:45 PM"),
    datetime.date(2025, 3, 23): ("05:16 AM", "6:45 PM"),
    datetime.date(2025, 3, 24): ("05:15 AM", "6:46 PM"),
    datetime.date(2025, 3, 25): ("05:14 AM", "6:46 PM"),
    datetime.date(2025, 3, 26): ("05:12 AM", "6:47 PM"),
    datetime.date(2025, 3, 27): ("05:11 AM", "6:47 PM"),
    datetime.date(2025, 3, 28): ("05:10 AM", "6:47 PM"),
    datetime.date(2025, 3, 29): ("05:09 AM", "6:48 PM"),
    datetime.date(2025, 3, 30): ("05:08 AM", "6:48 PM"),
    datetime.date(2025, 3, 31): ("05:07 AM", "6:49 PM"),
}

# User input for name and date selection
user_name = st.text_input("📌 Enter Your Name:")
selected_date = st.date_input("📅 Select Date:", datetime.date.today())

if st.button("📜 Get Ramadan Details"):
    # Determine fasting day
    ramadan_start = datetime.date(2025, 3, 2)
    if selected_date >= ramadan_start:
        fasting_day = (selected_date - ramadan_start).days + 1
        if fasting_day > 30 or selected_date > datetime.date(2025, 3, 31):
            fasting_day = "Eid Mubarak! 🎉"
            eid_message = f"May this Eid bring happiness, prosperity, and countless blessings to you, {user_name}! 🕌✨"
            dua = f"""
            <div style='text-align: center; font-size: 20px; font-weight: bold; color: #FFD700;'>
            🎉 Eid Mubarak, {user_name}! 🎉<br>
            May Allah accept our prayers and grant us endless joy on this blessed occasion.<br>
            اللّٰهُمَّ تَقَبَّلْ مِنَّا وَاجْعَلْ هٰذَا الْعِيْدَ بَرَكَةً وَسَعَادَةً لِلنَّاسِ جَمِيْعًا
            </div>
            """
        else:
            eid_message = ""
            dua = f"""
            <div style='text-align: center; font-size: 20px; font-weight: bold; color: #FFD700;'>
            🤲 O Allah, accept the fasts of {user_name}, forgive their sins, and grant Your mercy in this sacred month. 🤲<br>
            اللّٰهُمَّ تَقَبَّلْ صِيَامَ {user_name} وَاغْفِرْ ذُنُوبَهُ وَارْزُقْهُ رَحْمَتَكَ فِيْ هٰذَا الشَّهْرِ الْمُبَارَكِ
            </div>
            """
    
    # Display Sehri & Iftar timings
    sehri_time, aftar_time = ramadan_calendar.get(selected_date, (None, None))
    st.write(f"📆 **Today's Date:** {selected_date.strftime('%A, %d %B %Y')}")
    st.write(f"🌙 **Fasting Day:** {fasting_day}")
    if eid_message:
        st.success(eid_message)
    if sehri_time and aftar_time:
        st.success(f"⏳ **Sehri Time:** {sehri_time}")
        st.success(f"🌅 **Iftar Time:** {aftar_time}")
    else:
        st.warning("⚠ Date is outside Ramadan period.")
    
    st.markdown(dua, unsafe_allow_html=True)

# Footer with developer name
st.markdown("---")
st.markdown("<h4 style='text-align: center;'>🔹 Developed by <span style='color: #FFD700;'>Farhad Gul</span> ✨</h4>", unsafe_allow_html=True)
