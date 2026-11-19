import pandas as pd, numpy as np
rows = [
# year, film, imdb, hair(1-5), conf, note
(2010,"Band Baaja Baaraat",7.2,2,"medium","short spiky"),
(2011,"Ladies vs Ricky Bahl",6.0,2,"medium","short styled"),
(2013,"Lootera",7.3,2,"high","short period cut"),
(2013,"Goliyon Ki Raasleela Ram-Leela",6.4,3,"medium","tousled mid-length + stubble"),
(2014,"Gunday",2.4,3,"low","medium waves"),
(2014,"Kill Dil",4.3,3,"low","short-medium"),
(2015,"Dil Dhadakne Do",6.9,2,"medium","short"),
(2015,"Bajirao Mastani",7.2,4,"high","long, near shoulder"),
(2016,"Befikre",4.0,2,"medium","short quiff"),
(2018,"Padmaavat",7.0,4,"high","long + beard"),
(2018,"Simmba",5.6,2,"medium","cop crop"),
(2019,"Gully Boy",7.9,3,"medium","tousled mid-length"),
(2022,"Cirkus",4.2,2,"low","short retro"),
(2023,"Rocky Aur Rani Kii Prem Kahaani",6.5,3,"medium","wavy medium"),
(2024,"Singham Again",4.3,2,"medium","short cop"),
(2025,"Dhurandhar",8.3,4,"high","long + beard"),
]
df = pd.DataFrame(rows, columns=["year","film","imdb","hair_length_1to5","hair_confidence","hair_note"])
df["good_film"] = (df.imdb>=7.0).astype(int)
df.to_csv("ranveer_hair_vs_imdb.csv", index=False)
print(df[["imdb","hair_length_1to5"]].corr(method="pearson").iloc[0,1])
print(df[["imdb","hair_length_1to5"]].corr(method="spearman").iloc[0,1])
print(df.groupby("hair_length_1to5").imdb.agg(["mean","count"]))
# permutation test on spearman
rng=np.random.default_rng(0)
obs=df.imdb.rank().corr(df.hair_length_1to5.rank())
perm=[df.imdb.rank().corr(pd.Series(rng.permutation(df.hair_length_1to5.values)).rank()) for _ in range(20000)]
print("obs",obs,"p",np.mean(np.abs(perm)>=abs(obs)), "n",len(df))
hi=df[df.confidence if False else df.hair_confidence=="high"]
print(len(hi), hi.imdb.corr(hi.hair_length_1to5,method="spearman"))
try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(8,5.5))
    j=df.hair_length_1to5+np.random.default_rng(1).uniform(-.08,.08,len(df))
    ax.scatter(j,df.imdb,s=70)
    for x,y,t in zip(j,df.imdb,df.film): ax.annotate(t.split(" Ki")[0][:22],(x,y),fontsize=7,xytext=(4,3),textcoords="offset points")
    m,b=np.polyfit(df.hair_length_1to5,df.imdb,1); xs=np.array([1.8,4.2]); ax.plot(xs,m*xs+b,"--",color="gray")
    ax.set_xlabel("Hair length (1 = crop, 5 = very long)"); ax.set_ylabel("IMDb rating"); ax.set_title("Ranveer Singh: hair length vs IMDb rating (lead films)")
    ax.set_xticks([1,2,3,4,5]); plt.tight_layout(); plt.savefig("ranveer_hair_scatter.png",dpi=160); print("png ok")
except Exception as e: print("noplot",e)
