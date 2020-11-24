#!/usr/bin/env python3

import json
from dateutil.parser import parse as parse_dt
import matplotlib.pyplot as plt

#response = requests.get("https://www.berlin.de/lageso/gesundheit/infektionsepidemiologie-infektionsschutz/corona/tabelle-bezirke-gesamtuebersicht/index.php/index/all.json")
#json = response.json()

with open("processed.json", "r") as infile:
    db = json.load(infile)

dates = [parse_dt(d) for d in db["dates"]]

def average_7days(bezirk):
    entries = db[bezirk]

    s7_day_avg = [
        {"date": date, "avg": sum(entries[i - 7 : i]) / 7}
        for i, date in reversed(list(enumerate(dates)))
    ]

    x = [r["date"] for r in s7_day_avg]
    y = [r["avg"] for r in s7_day_avg]

    return x, y


bezirken = [
    "charlottenburg_wilmersdorf",
    "friedrichshain_kreuzberg",
    "lichtenberg",
    "marzahn_hellersdorf",
    "mitte",
    "neukoelln",
    "pankow",
    "reinickendorf",
    "spandau",
    "steglitz_zehlendorf",
    "tempelhof_schoeneberg",
    "treptow_koepenick",
]


avgs = [ (bezirk, *average_7days(bezirk)) for bezirk in bezirken ]

for _, _, y in avgs:
    assert len(y) == len(avgs[0][2])

my_dpi=120
figsize=(1000/my_dpi, 600/my_dpi)

print("All together now")
fig = plt.figure(figsize=figsize, dpi=my_dpi)
for bezirk, x, y in avgs:
    plt.plot(x, y)

plt.gcf().autofmt_xdate()
plt.legend(bezirken, loc="best")
fig.suptitle(f"7-Tage-Durchschnitt der neuen Fälle in Berlin")
fig.savefig(f"plots/ALL.png", bbox_inches="tight")

for bezirk, x, y in avgs:
    print(bezirk)

    fig = plt.figure(figsize=figsize, dpi=my_dpi)
    plt.plot(x, y)
    plt.gcf().autofmt_xdate()
    fig.suptitle(f"7-Tage-Durchschnitt der neuen Fälle in {bezirk}")
    fig.savefig(f"plots/{bezirk}.png", bbox_inches="tight")
