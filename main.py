import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("ngo_data.xlsx")
total_donation = df["Donation_Amount"].sum()
total_donors = len(df)
total_cities = df["City"].nunique()
average_donation = df["Donation_Amount"].mean()
plt.style.use("dark_background")
fig = plt.figure(figsize=(16, 10))
fig.patch.set_facecolor("#121212")
plt.suptitle(
    "NGO DONATION ANALYTICS DASHBOARD\nPython | Pandas | Matplotlib",
    fontsize=20,
    fontweight="bold",
    color="white"
)
plt.figtext(
    0.5,
    0.92,
    f"Total Donations: Rs.{total_donation:,.0f} | "
    f"Total Donors: {total_donors} | "
    f"Cities: {total_cities} | "
    f"Avg Donation: Rs.{average_donation:,.0f}",
    ha="center",
    fontsize=11,
    color="white",
    bbox=dict(
        facecolor="#1E1E1E",
        edgecolor="#00E676",
        boxstyle="round,pad=0.6"
    )
)
ax1 = plt.subplot(2, 2, 1)
ax1.set_facecolor("#1E1E1E")
city = df.groupby("City")["Donation_Amount"].sum()
bars = ax1.bar(city.index, city.values, color="#00E676")
ax1.set_title("Donations by City", color="white")
ax1.set_ylabel("Donation (Rs.)", color="white")
ax1.tick_params(colors="white")
for bar in bars:
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{int(bar.get_height())}",
        ha="center",
        va="bottom",
        fontsize=8,
        color="white"
    )

ax2 = plt.subplot(2, 2, 2)
ax2.set_facecolor("#1E1E1E")
campaign = df["Campaign"].value_counts()
colors = ["#00E676", "#03A9F4", "#FF9800", "#AB47BC"]
ax2.pie(
    campaign,
    labels=campaign.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors[:len(campaign)],
    textprops={"color": "white"}
)
ax2.set_title("Campaign Distribution", color="white")
ax3 = plt.subplot(2, 2, 3)
ax3.set_facecolor("#1E1E1E")
hours = df.groupby("City")["Volunteer_Hours"].sum()
bars = ax3.bar(hours.index, hours.values, color="#FF9800")
ax3.set_title("Volunteer Hours by City", color="white")
ax3.set_ylabel("Hours", color="white")
ax3.tick_params(colors="white")
for bar in bars:
    ax3.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{int(bar.get_height())}",
        ha="center",
        va="bottom",
        fontsize=8,
        color="white"
    )
ax4 = plt.subplot(2, 2, 4)
ax4.set_facecolor("#1E1E1E")
avg = df.groupby("Campaign")["Donation_Amount"].mean()
bars = ax4.bar(avg.index, avg.values, color="#AB47BC")
ax4.set_title("Average Donation by Campaign", color="white")
ax4.set_ylabel("Average Donation (Rs.)", color="white")
ax4.tick_params(axis="x", rotation=15, colors="white")
ax4.tick_params(axis="y", colors="white")
for bar in bars:
    ax4.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{int(bar.get_height())}",
        ha="center",
        va="bottom",
        fontsize=8,
        color="white"
    )
plt.tight_layout(rect=[0, 0, 1, 0.88])
plt.figtext(
    0.5,
    0.02,
    "Developed by Lessly K.J.",
    ha="center",
    fontsize=10,
    color="lightgray"
)
plt.savefig(
    "NGO_Dashboard_Dark.png",
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)
plt.show()
print("Dashboard created successfully!")
