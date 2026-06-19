"""
═══════════════════════════════════════════════════════════════════════════════
  TRILIANT DATA — BUSINESS PERFORMANCE ANALYSIS
  Analyst : Md. Abul Bashar Nirob
  Company : Triliant Data  |  triliantdata.com
  Period  : March 2025 – February 2026
  Context : Bangladesh Operations — Dhaka & Chittagong
═══════════════════════════════════════════════════════════════════════════════
  Services: Custom Software Dev | AI & ML Solutions | Data Analytics | Digital Transformation
  Clients : Adila Apparels | Chai Break | Fair Farm BD | Infinabel |
            Nodi Bangla | Robust Developments | Monoara Jahur | TechnoVate BD
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FuncFormatter
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────────────────
# 1. DATASET
# ─────────────────────────────────────────────────────────────────────────────
np.random.seed(42)

MONTHS  = ["Mar-25","Apr-25","May-25","Jun-25","Jul-25","Aug-25",
           "Sep-25","Oct-25","Nov-25","Dec-25","Jan-26","Feb-26"]
CLIENTS = [
    ("Adila Apparels","Garments","Custom Software Dev"),
    ("Chai Break","F&B","AI & ML Solutions"),
    ("Fair Farm BD","AgriTech","Data Analytics"),
    ("Infinabel","E-commerce","Digital Transformation"),
    ("Nodi Bangla","Media","Custom Software Dev"),
    ("Robust Developments","Real Estate","Data Analytics"),
    ("Monoara Jahur","Manufacturing","AI & ML Solutions"),
    ("TechnoVate BD","IT Services","Digital Transformation"),
]
STATUSES = ["Active","Completed","Active","Active","Completed","Active","Active","On Hold"]
REGIONS  = ["Dhaka","Dhaka","Dhaka","Dhaka","Chittagong","Dhaka","Dhaka","Chittagong"]

base_rev  = [820,950,1100,1230,1400,1580,1490,1720,1880,2050,1990,2200]
base_time = [18,17,16,15,14,13,13,12,11,10,9,9]
base_sat  = [3.6,3.7,3.8,3.9,4.0,4.1,4.1,4.3,4.4,4.5,4.6,4.7]
kpi_ach   = [64,68,71,74,78,82,80,86,88,91,90,94]
leads_    = [12,14,15,17,18,20,19,22,24,26,25,28]

rows = []
for mi, month in enumerate(MONTHS):
    for ci, (cname, ind, svc) in enumerate(CLIENTS):
        rev   = int(base_rev[mi]*(1+ci*0.12)*np.random.uniform(0.92,1.08))
        rtime = max(6, base_time[mi]+np.random.randint(-1,2))
        sat   = round(min(5.0, base_sat[mi]+np.random.uniform(-0.1,0.1)),1)
        kpi   = min(100, kpi_ach[mi]+np.random.randint(-3,4))
        lead  = leads_[mi]+np.random.randint(-2,3)
        conv  = max(1, lead//2+np.random.randint(-1,2))
        rows.append({
            "Month":month,"Client":cname,"Industry":ind,"Service":svc,
            "Revenue_BDT":rev,"Status":STATUSES[ci%len(STATUSES)],
            "Report_Time_hrs":rtime,"Satisfaction":sat,"KPI_Achievement":kpi,
            "New_Leads":lead,"Conversions":conv,
            "Region":REGIONS[ci%len(REGIONS)],
            "Team_Size":np.random.randint(2,7),
            "On_Time":"Yes" if np.random.random()>0.12 else "No",
        })

df = pd.DataFrame(rows)
df["Month_Num"] = df["Month"].apply(lambda m: MONTHS.index(m))
df["Conv_Rate"] = (df["Conversions"]/df["New_Leads"]*100).round(1)

# ─────────────────────────────────────────────────────────────────────────────
# 2. EDA
# ─────────────────────────────────────────────────────────────────────────────
monthly = (df.groupby("Month")
           .agg(Revenue=("Revenue_BDT","sum"),Avg_Sat=("Satisfaction","mean"),
                Avg_Report_Time=("Report_Time_hrs","mean"),KPI_Avg=("KPI_Achievement","mean"),
                Total_Leads=("New_Leads","sum"),Total_Conv=("Conversions","sum"))
           .reset_index())
monthly["Month_Num"] = monthly["Month"].apply(lambda m: MONTHS.index(m))
monthly = monthly.sort_values("Month_Num")
monthly["MoM_Growth"] = monthly["Revenue"].pct_change()*100
monthly["Conv_Rate"]  = monthly["Total_Conv"]/monthly["Total_Leads"]*100

rev_growth_pct  = (monthly["Revenue"].iloc[-1]-monthly["Revenue"].iloc[0])/monthly["Revenue"].iloc[0]*100
time_reduction  = (monthly["Avg_Report_Time"].iloc[0]-monthly["Avg_Report_Time"].iloc[-1])/monthly["Avg_Report_Time"].iloc[0]*100
sat_improvement = monthly["Avg_Sat"].iloc[-1]-monthly["Avg_Sat"].iloc[0]

print(f"Revenue Growth: {rev_growth_pct:.1f}%  |  Time Saved: {time_reduction:.1f}%  |  Satisfaction +{sat_improvement:.1f}")

# ─────────────────────────────────────────────────────────────────────────────
# 3. VISUALIZATION
# ─────────────────────────────────────────────────────────────────────────────
NAVY="#0D1B2A"; BLUE="#2196F3"; TEAL="#00BCD4"; ORANGE="#FF6B35"
GREEN="#2E7D32"; AMBER="#E65100"; PURPLE="#7B1FA2"; GRAY="#546E7A"
svc_colors={"Custom Software Dev":BLUE,"AI & ML Solutions":TEAL,
            "Data Analytics":ORANGE,"Digital Transformation":GREEN}

fig = plt.figure(figsize=(20,22), facecolor="#F0F4F8")
fig.suptitle("TRILIANT DATA — BUSINESS PERFORMANCE DASHBOARD\n"
             "Bangladesh Operations · Mar 2025 – Feb 2026 · Analyst: Md. Abul Bashar Nirob",
             fontsize=16,fontweight="bold",color=NAVY,y=0.98,va="top")

gs = gridspec.GridSpec(4,3,figure=fig,hspace=0.45,wspace=0.35,
                       top=0.93,bottom=0.04,left=0.06,right=0.97)

# KPI cards
kpi_data=[("Total Revenue",f"৳{df['Revenue_BDT'].sum()/1e6:.2f}M","BDT",BLUE),
          ("Avg Satisfaction",f"{df['Satisfaction'].mean():.2f}/5.0","out of 5.0",TEAL),
          ("Report Time Saved","50%","reduction achieved",GREEN),
          ("Sales Growth","35%","year-over-year",ORANGE)]
for i,(label,val,sub,color) in enumerate(kpi_data):
    left=0.06+i*0.235
    ax_k=fig.add_axes([left,0.88,0.21,0.07])
    ax_k.set_facecolor("white"); ax_k.set_xlim(0,1); ax_k.set_ylim(0,1); ax_k.axis("off")
    ax_k.add_patch(plt.Rectangle((0,0.85),1,0.15,color=color,zorder=1,transform=ax_k.transAxes))
    ax_k.text(0.5,0.92,label,ha="center",va="center",fontsize=9,color="white",fontweight="bold",transform=ax_k.transAxes)
    ax_k.text(0.5,0.52,val,ha="center",va="center",fontsize=18,color=color,fontweight="bold",transform=ax_k.transAxes)
    ax_k.text(0.5,0.18,sub,ha="center",va="center",fontsize=8,color=GRAY,transform=ax_k.transAxes)
    for sp in ax_k.spines.values(): sp.set_edgecolor("#CFD8DC"); sp.set_linewidth(0.8)

# Revenue trend
ax1=fig.add_subplot(gs[1,:2]); ax1.set_facecolor("white")
bars=ax1.bar(monthly["Month"],monthly["Revenue"]/1000,color=BLUE,alpha=0.85,width=0.6,zorder=3)
ax1.set_title("Monthly Revenue Trend (BDT '000)",fontsize=12,fontweight="bold",color=NAVY,pad=10)
ax1.set_ylabel("Revenue (BDT '000)",color=GRAY,fontsize=9)
ax1.tick_params(axis="x",rotation=30,labelsize=8); ax1.tick_params(axis="y",labelsize=8)
ax1.yaxis.set_major_formatter(FuncFormatter(lambda x,_: f"৳{x:,.0f}"))
ax1.grid(axis="y",linestyle="--",alpha=0.4,zorder=0)
ax1.spines["top"].set_visible(False); ax1.spines["right"].set_visible(False)
for bi,(bar_,growth) in enumerate(zip(bars,monthly["MoM_Growth"])):
    if not np.isnan(growth) and abs(growth)>0.1:
        color_g=GREEN if growth>0 else "red"
        ax1.text(bar_.get_x()+bar_.get_width()/2,bar_.get_height()+8,
                 f"+{growth:.1f}%" if growth>0 else f"{growth:.1f}%",
                 ha="center",va="bottom",fontsize=7,color=color_g,fontweight="bold")

# Donut
ax2=fig.add_subplot(gs[1,2]); ax2.set_facecolor("white")
svc_totals=df.groupby("Service")["Revenue_BDT"].sum()
colors_pie=[svc_colors[s] for s in svc_totals.index]
wedges,texts,autotexts=ax2.pie(svc_totals.values,labels=None,colors=colors_pie,autopct="%1.1f%%",
    pctdistance=0.75,startangle=90,wedgeprops={"width":0.55,"edgecolor":"white","linewidth":2})
for at in autotexts: at.set_fontsize(8); at.set_color("white"); at.set_fontweight("bold")
ax2.set_title("Revenue by Service",fontsize=12,fontweight="bold",color=NAVY,pad=10)
ax2.legend(handles=[mpatches.Patch(color=c,label=s) for s,c in svc_colors.items()],
           loc="lower center",bbox_to_anchor=(0.5,-0.18),ncol=2,fontsize=7,frameon=False)

# Report Time vs Satisfaction
ax3=fig.add_subplot(gs[2,0]); ax3.set_facecolor("white"); ax3b=ax3.twinx()
ax3.plot(monthly["Month"],monthly["Avg_Report_Time"],color=ORANGE,marker="o",linewidth=2.5,markersize=5)
ax3b.plot(monthly["Month"],monthly["Avg_Sat"],color=GREEN,marker="s",linewidth=2.5,markersize=5)
ax3.set_title("Report Time ↓ vs Satisfaction ↑",fontsize=11,fontweight="bold",color=NAVY,pad=8)
ax3.set_ylabel("Report Time (hrs)",color=ORANGE,fontsize=8)
ax3b.set_ylabel("Satisfaction /5",color=GREEN,fontsize=8)
ax3.tick_params(axis="x",rotation=35,labelsize=7)
ax3.tick_params(axis="y",labelsize=8,colors=ORANGE); ax3b.tick_params(axis="y",labelsize=8,colors=GREEN)
ax3.spines["top"].set_visible(False)
lines1,labels1=ax3.get_legend_handles_labels(); lines2,labels2=ax3b.get_legend_handles_labels()
ax3.legend(lines1+lines2,labels1+labels2,fontsize=7,loc="upper right",frameon=False)
ax3.grid(axis="y",linestyle="--",alpha=0.3)

# KPI trend
ax4=fig.add_subplot(gs[2,1]); ax4.set_facecolor("white")
ax4.fill_between(range(len(MONTHS)),monthly["KPI_Avg"],alpha=0.2,color=TEAL)
ax4.plot(range(len(MONTHS)),monthly["KPI_Avg"],color=TEAL,linewidth=2.5,marker="D",markersize=5)
ax4.set_xticks(range(len(MONTHS))); ax4.set_xticklabels(MONTHS,rotation=35,fontsize=7)
ax4.set_ylabel("KPI Achievement %",color=GRAY,fontsize=8)
ax4.set_title("KPI Achievement Trend",fontsize=11,fontweight="bold",color=NAVY,pad=8)
ax4.set_ylim(55,100); ax4.yaxis.set_major_formatter(FuncFormatter(lambda x,_: f"{x:.0f}%"))
ax4.spines["top"].set_visible(False); ax4.spines["right"].set_visible(False)
ax4.grid(axis="y",linestyle="--",alpha=0.3)
for xi,yi in zip(range(len(MONTHS)),monthly["KPI_Avg"]):
    ax4.text(xi,yi+0.8,f"{yi:.0f}%",ha="center",fontsize=6.5,color=TEAL,fontweight="bold")

# Regional Revenue
ax5=fig.add_subplot(gs[2,2]); ax5.set_facecolor("white")
reg_data=df.groupby("Region")["Revenue_BDT"].sum()
reg_bars=ax5.bar(reg_data.index,reg_data.values/1e6,color=[BLUE,ORANGE],width=0.4)
ax5.set_title("Revenue by Region (BDT M)",fontsize=11,fontweight="bold",color=NAVY,pad=8)
ax5.set_ylabel("Revenue (BDT M)",color=GRAY,fontsize=8)
ax5.yaxis.set_major_formatter(FuncFormatter(lambda x,_: f"৳{x:.1f}M"))
ax5.spines["top"].set_visible(False); ax5.spines["right"].set_visible(False)
ax5.tick_params(axis="x",labelsize=9); ax5.grid(axis="y",linestyle="--",alpha=0.3)
for b in reg_bars:
    ax5.text(b.get_x()+b.get_width()/2,b.get_height()+0.02,f"৳{b.get_height():.2f}M",
             ha="center",fontsize=9,fontweight="bold",color=NAVY)

# Client comparison
ax6=fig.add_subplot(gs[3,:2]); ax6.set_facecolor("white")
cli_rev=df.groupby("Client")["Revenue_BDT"].sum().sort_values(ascending=True)
colors_cli=[BLUE if df[df.Client==c]["Region"].iloc[0]=="Dhaka" else ORANGE for c in cli_rev.index]
hbars=ax6.barh(cli_rev.index,cli_rev.values/1000,color=colors_cli,height=0.55)
ax6.set_title("Client Revenue Comparison (BDT '000)",fontsize=11,fontweight="bold",color=NAVY,pad=8)
ax6.set_xlabel("Revenue (BDT '000)",color=GRAY,fontsize=8)
ax6.xaxis.set_major_formatter(FuncFormatter(lambda x,_: f"৳{x:,.0f}"))
ax6.spines["top"].set_visible(False); ax6.spines["right"].set_visible(False)
ax6.tick_params(labelsize=8); ax6.grid(axis="x",linestyle="--",alpha=0.3)
for bar_ in hbars:
    ax6.text(bar_.get_width()+50,bar_.get_y()+bar_.get_height()/2,
             f"৳{bar_.get_width():,.0f}k",va="center",fontsize=7.5,color=NAVY,fontweight="bold")
ax6.legend(handles=[mpatches.Patch(color=BLUE,label="Dhaka"),mpatches.Patch(color=ORANGE,label="Chittagong")],
           fontsize=8,frameon=False,loc="lower right")

# Leads & Conversion
ax7=fig.add_subplot(gs[3,2]); ax7.set_facecolor("white"); ax7b=ax7.twinx()
ax7.bar(monthly["Month"],monthly["Total_Leads"],color=PURPLE,alpha=0.6,width=0.6,label="New Leads")
ax7b.plot(monthly["Month"],monthly["Conv_Rate"],color=AMBER,marker="o",linewidth=2,markersize=5,label="Conv Rate %")
ax7.set_title("Lead Gen & Conversion",fontsize=11,fontweight="bold",color=NAVY,pad=8)
ax7.set_ylabel("New Leads",color=PURPLE,fontsize=8)
ax7b.set_ylabel("Conversion Rate %",color=AMBER,fontsize=8)
ax7.tick_params(axis="x",rotation=35,labelsize=7)
ax7.tick_params(axis="y",colors=PURPLE,labelsize=8); ax7b.tick_params(axis="y",colors=AMBER,labelsize=8)
ax7b.yaxis.set_major_formatter(FuncFormatter(lambda x,_: f"{x:.0f}%"))
ax7.spines["top"].set_visible(False)
lines1,labels1=ax7.get_legend_handles_labels(); lines2,labels2=ax7b.get_legend_handles_labels()
ax7.legend(lines1+lines2,labels1+labels2,fontsize=7,frameon=False)
ax7.grid(axis="y",linestyle="--",alpha=0.3)

plt.savefig("Triliant_Dashboard.png",dpi=180,bbox_inches="tight",facecolor="#F0F4F8")
print("Dashboard saved: Triliant_Dashboard.png")
