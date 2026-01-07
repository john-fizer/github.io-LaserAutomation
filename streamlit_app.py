import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime, timedelta

# Page Config
st.set_page_config(
    page_title="LaserFlow Automation",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Mock Data Services (Direct integration, no API calls needed) ---

def get_dashboard_summary():
    return {
        "jobs_queued": 24,
        "jobs_running": 3,
        "jobs_done_today": 18,
        "lasers_active": 2
    }

def get_machines():
    return [
        {"id": 1, "name": "Laser 1 (Fiber 4kW)", "status": "RUNNING", "program": "L1-027.MIN", "progress": 82},
        {"id": 2, "name": "Laser 2 (CO2 2kW)", "status": "IDLE", "program": None, "progress": 0},
        {"id": 3, "name": "Laser 3 (Fiber 6kW)", "status": "STOPPED", "program": "ALARM: 404", "progress": 0},
    ]

def get_jobs(status=None):
    data = [
        {"job": "10452", "cust": "ACME Parts", "part": "PART-AX123", "status": "RUNNING", "qty": 250, "material": "A36 0.500"},
        {"job": "10453", "cust": "Cyberdyne", "part": "SKY-NET-01", "status": "RUNNING", "qty": 80, "material": "SS304 0.125"},
        {"job": "10460", "cust": "Wayne Ent", "part": "BAT-WING-07", "status": "NESTING", "qty": 40, "material": "AL5052 0.063"},
        {"job": "10461", "cust": "Stark Ind", "part": "MK3-CHEST", "status": "QUEUED", "qty": 10, "material": "Ti-6Al-4V"},
        {"job": "10422", "cust": "General Motors", "part": "BRACKET-L", "status": "DONE", "qty": 5000, "material": "MS 1.00"},
    ]
    if status and status != 'ALL':
        return [j for j in data if j['status'] == status]
    return data

# --- Sidebar ---
st.sidebar.title("⚡ LaserFlow")
st.sidebar.markdown(f"**User**: John (Admin)")
page = st.sidebar.radio("Navigate", ["Dashboard", "Machines", "Jobs"])
st.sidebar.divider()
st.sidebar.caption(f"Last sync: {datetime.now().strftime('%H:%M:%S')}")

# --- Dashboard Page ---
if page == "Dashboard":
    st.title("Shop Floor Dashboard")
    
    # 1. KPI Tiles
    stats = get_dashboard_summary()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Jobs Queued", stats['jobs_queued'], "+2")
    col2.metric("Active Lasers", f"{stats['lasers_active']} / 3", "85% Util")
    col3.metric("Jobs Running", stats['jobs_running'])
    col4.metric("Completed Today", -stats['jobs_done_today'], "12% vs Avg") 
    
    st.divider()

    # 2. Activity & Preview
    col_main, col_feed = st.columns([2, 1])
    
    with col_main:
        st.subheader("Active Production")
        active_jobs = pd.DataFrame(get_jobs('RUNNING'))
        st.dataframe(active_jobs, use_container_width=True, hide_index=True)
        
        st.subheader("Nesting Queue")
        nesting_jobs = pd.DataFrame(get_jobs('NESTING'))
        st.dataframe(nesting_jobs, use_container_width=True, hide_index=True)

    with col_feed:
        st.subheader("Live Feed")
        st.info("🕙 10:21 - Laser 1 completed Sheet S-027")
        st.success("🕙 10:15 - Job 10452 posted to JobBOSS2 ($142.50)")
        st.warning("🕙 09:44 - Laser 3 Alarm: Beam Off")

# --- Machines Page ---
elif page == "Machines":
    st.title("Machine Status")
    
    machines = get_machines()
    
    cols = st.columns(3)
    for idx, m in enumerate(machines):
        with cols[idx]:
            status_color = "green" if m['status'] == "RUNNING" else "red" if m['status'] == "STOPPED" else "grey"
            st.markdown(f"### :{status_color}[●] {m['name']}")
            
            st.markdown(f"**Status**: {m['status']}")
            st.markdown(f"**Program**: `{m['program'] or '---'}`")
            
            if m['status'] == 'RUNNING':
                st.progress(m['progress'])
                st.caption(f"Progress: {m['progress']}%")
            else:
                st.info("Machine Idle")

    st.divider()
    st.subheader("MTConnect Stream")
    st.code("""
<Streams>
  <DeviceStream name="Laser1" uuid="L1">
    <ComponentStream component="Path" name="path">
      <Events>
        <Execution dataItemId="e1">ACTIVE</Execution>
        <Program dataItemId="p1">L1-027.MIN</Program>
      </Events>
    </ComponentStream>
  </DeviceStream>
</Streams>
    """, language="xml")

# --- Jobs Page ---
elif page == "Jobs":
    st.title("Job Management")
    
    # Filter
    filter_status = st.selectbox("Status Filter", ["ALL", "QUEUED", "NESTING", "RUNNING", "DONE"])
    
    # Data
    jobs_data = get_jobs(filter_status)
    df = pd.DataFrame(jobs_data)
    
    st.dataframe(
        df, 
        use_container_width=True, 
        column_config={
            "status": st.column_config.SelectboxColumn(
                "Status",
                options=["QUEUED", "NESTING", "RUNNING", "DONE"],
                required=True,
            ),
            "progress": st.column_config.ProgressColumn(
                "Progress",
                format="%d%%",
                min_value=0,
                max_value=100,
            ),
        },
        hide_index=True
    )
    
    if st.button("Refresh from JobBOSS2"):
        st.toast("Syncing with ERP...", icon="🔄")
        time.sleep(1)
        st.toast("Sync Complete!", icon="✅")
