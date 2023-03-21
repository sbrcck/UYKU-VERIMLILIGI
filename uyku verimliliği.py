#!/usr/bin/env python
# coding: utf-8

#  ## UYKU VERİMLİLİĞİ (Sleep Efficiency)

#   Uyku verimliliği, uyku sırasında harcanan zamanın toplam uyku süresine oranıdır ve % olarak ifade edilir. Bu, bir kişinin uyku kalitesini ve uyku düzenini değerlendirmek için önemli bir ölçüttür. Uyku verimliliği yüksek olan bir kişi, daha az uyku süresiyle daha fazla dinlenmiş hisseder ve daha düzenli bir uyku alışkanlığına sahiptir.
#   Bunun yanı sıra uyku verimliğini etkileyen birçok sebep bulunmaktadır. Bu veri analizi örneğinde uyku kalıtesi ve verimliliğine etki eden faktörlerin farklı yaş gruplarının ve cinsiyetlerin etkilenme biçimlerini inceleyeceğiz. hadi başlayalım... 
# 

# #### 1 Gerekli Kütüphaneler 
# İlk aşamada gerekli küphanedeleri ekleyerek başlıyoruz burada python'a ait birçok kütüphane bulunmakta ve python' entegre olarak çalışan birçok kütüphane vardır bu kütüphanelerin nsıl kullanıldığını ufak bir araştırma ile bulabilirsiniz    

# In[8]:


import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import missingno as msno
import plotly.graph_objs as go
import plotly.express as px
plt.style.use('seaborn-dark')
plt.style.context('grayscale')
get_ipython().run_line_magic('matplotlib', 'inline')
from wordcloud import WordCloud, STOPWORDS


# #### 2 Veri setini okumak

# In[9]:


df=pd.read_csv("/home/sbricck/Masaüstü/verianalizi/Sleep_Efficiency.csv")


# #### 3 Veri seti hakkında kısa bir bilgi edinme
# 

# Bu aşamada verimizi inceliyoruz ve gerekli duzenlemeri yapıp öyle devam etmemiz gerekli

# df.head()

# In[11]:


df.isnull().sum()


# In[13]:


df.rename(columns = {'Wakeup time':'Wakeup_time', 'Sleep duration':'Sleep_duration ',"Sleep efficiency":"Sleep_efficiency",
                     "REM sleep percentage":"REM_sleep_percentage","Deep sleep percentage":"Deep_sleep_percentage",
                     "Light sleep percentage":"Light_sleep_percentage","Caffeine consumption":"Caffeine_consumption",
                     "Alcohol consumption":"Alcohol_consumption","Smoking status":"Smoking_status","Exercise frequency":"Exercise_frequency"}, inplace = True)


# In[14]:


df.info()


# In[15]:


df.head()


# #### 4 Veri görselleştirme

# In[17]:


df.Age.value_counts()


# In[18]:


sns.kdeplot(data=df, x="Age",color="black",fill=True)
plt.xlabel("Age", color="black", fontsize=10)
plt.ylabel("count", color="black", fontsize=10)
plt.title("Age kdeplot", color="black",fontsize=10)
plt.show()


# ####  Yaşın ve cinsiyetin Uyku kalitesine etkileri

# In[20]:


sns.relplot(
    data=df, kind="line",
    x="Age", y="Sleep_efficiency", style="Gender", color="black"
)
plt.title("Kadınların 50'li, erkeklerin ise 60'lı yaşlarında uyku verimliliğinin arttığını gözlemliyoruz.", color="black",fontsize=10)
plt.show()


# In[21]:


df.Gender.value_counts()


# In[22]:


sns.countplot(data=df,x="Gender", color="red")
plt.xlabel("Female or Male", color="red",fontsize=10)
plt.ylabel("Count", color="red",fontsize=10)
plt.title("Male and Female", color="red",fontsize=10)
plt.show()


# In[23]:


df.Smoking_status.value_counts()


# In[24]:


sns.countplot(data=df,x="Smoking_status", color="green")
plt.xlabel("Yes or No", color="green",fontsize=10)
plt.ylabel("Count", color="green",fontsize=10)
plt.title("number of smokers and non-smokers", color="green",fontsize=10)
plt.show()


# #### Peki sigara uyku düzenini etkiler mi?

# In[26]:


sns.boxplot(data=df,x="Smoking_status",y="Sleep_efficiency", color="green")
plt.xlabel("Yes or No", color="green",fontsize=10)
plt.ylabel("Count", color="green",fontsize=10)
plt.title("number of smokers and non-smokers", color="green",fontsize=10)
plt.show()


# In[27]:


sns.relplot(
    data=df,
    x="Gender", y="Sleep_efficiency", col="Smoking_status",
    hue="REM_sleep_percentage", size="Smoking_status",
)
plt.show()


# Yukarıda, sigara içmeyenlerin daha iyi uyku kalitesine sahip olduğunu gösteren kutu çizimi yer almaktadır

# In[28]:


sns.kdeplot(data=df, x="REM_sleep_percentage",color="blue",fill=True)
plt.xlabel("Sleep Duration", color="blue", fontsize=10)
plt.ylabel("frequency", color="blue", fontsize=10)
plt.title("Sleep duration kdeplot", color="blue",fontsize=10)
plt.show()


# In[29]:


df.Exercise_frequency.value_counts()


# In[30]:


sns.kdeplot(data=df, x="Exercise_frequency",color="brown",fill=True)
plt.xlabel("Exercise Frequency", color="brown", fontsize=10)
plt.ylabel("frequency", color="brown", fontsize=10)
plt.title("Exercise Frequency Kdeplot", color="brown",fontsize=10)
plt.show()


# In[31]:


df.Alcohol_consumption.value_counts()


# In[32]:


sns.kdeplot(data=df, x="Alcohol_consumption",color="green",fill=True)
plt.xlabel("Alcohol Consumption", color="green", fontsize=10)
plt.ylabel("frequency", color="green", fontsize=10)
plt.title("Alcohol Consumption Kdeplot", color="green",fontsize=10)
plt.show()


# In[33]:


sns.boxplot(data=df,x="Alcohol_consumption",y="Sleep_efficiency", color="green")
plt.title("What is the effect of drinking alcohol on sleep efficiency?", color="green",fontsize=10)
plt.show()


# #### Yukarıdaki sonuçlar gösteriyor ki alkol, hafıza ve öğrenme için önemli olan REM uykusuna zarar kesinlikle verir

# In[34]:


sns.boxplot(data=df,x="REM_sleep_percentage",y="Sleep_efficiency", color="green")
plt.title("What is the effect of drinking alcohol on sleep efficiency?", color="green",fontsize=10)
plt.show()


# In[35]:


df.Caffeine_consumption.value_counts()


# In[36]:


sns.kdeplot(data=df, x="Caffeine_consumption",color="pink",fill=True)
plt.xlabel("Caffeine Consumption", color="pink", fontsize=10)
plt.ylabel("frequency", color="pink", fontsize=10)
plt.title("Caffeine Consumption Kdeplot", color="pink",fontsize=10)
plt.show()


# In[37]:


sns.boxplot(data=df,x="Caffeine_consumption",y="Sleep_efficiency", color="pink")
plt.title("Does caffeine consumption affect sleep?", color="pink",fontsize=10)
plt.show()


# Doğruluğu hala tartışma konusu olsa dahi  yukarıdaki grafikten elde ettiğimiz sonuca göreKahve tüketimi uyku kalitesine etki etmeği yönündedir

# In[38]:


df.Awakenings.value_counts()


# In[39]:


sns.kdeplot(data=df, x="Awakenings",color="orange",fill=True)
plt.xlabel("Awakenings", color="orange", fontsize=10)
plt.ylabel("frequency", color="orange", fontsize=10)
plt.title("Awakenings kdeplot", color="orange",fontsize=10)
plt.show()


# In[40]:


df.Light_sleep_percentage.value_counts()


# In[41]:


sns.kdeplot(data=df, x="Light_sleep_percentage",color="gray",fill=True)
plt.xlabel("Light sleep percentage", color="gray", fontsize=10)
plt.ylabel("frequency", color="gray", fontsize=10)
plt.title("Light sleep percentage kdeplot", color="gray",fontsize=10)
plt.show()


# In[43]:


df.Deep_sleep_percentage.value_counts()


# In[44]:


sns.kdeplot(data=df, x="Deep_sleep_percentage",color="magenta",fill=True)
plt.xlabel("Deep sleep percentage", color="magenta", fontsize=10)
plt.ylabel("frequency", color="magenta", fontsize=10)
plt.title("Deep sleep percentage kdeplot", color="magenta",fontsize=10)
plt.show()


# In[45]:


sns.boxplot(data=df,x="Awakenings",y="Deep_sleep_percentage", color="magenta")
plt.title("Does the number of times you wake up while sleeping have an effect on deep sleep?", color="magenta",fontsize=10)
plt.show()


# In[46]:


df.REM_sleep_percentage.value_counts()


# In[47]:


sns.kdeplot(data=df, x="REM_sleep_percentage",color="cyan",fill=True)
plt.xlabel("REM sleep percentage", color="cyan", fontsize=10)
plt.ylabel("frequency", color="cyan", fontsize=10)
plt.title("REM sleep percentage kdeplot", color="cyan",fontsize=10)
plt.show()


# In[48]:


df.Sleep_efficiency.value_counts()


# In[49]:


sns.kdeplot(data=df, x="Sleep_efficiency",color="purple",fill=True)
plt.xlabel("Sleep Efficiency", color="purple", fontsize=10)
plt.ylabel("frequency", color="purple", fontsize=10)
plt.title("Sleep Efficiency kdeplot", color="purple",fontsize=10)
plt.show()


# In[50]:


df.head()


# In[51]:


df['Date'] = pd.to_datetime(df['Bedtime'], errors='coerce')
df['day'] = (df['Date']).dt.day
df['month'] = (df['Date']).dt.month
df['year'] = (df['Date']).dt.year
df['hour'] = (df['Date']).dt.hour


# In[52]:


df['year'].value_counts()


# In[53]:


sns.countplot(data=df, x="year", palette="pastel")
plt.show()


# In[54]:


df['hour'].value_counts()


# In[55]:


sns.countplot(data=df, x="hour", palette="ocean")
plt.show()


# In[56]:


fig = px.pie(df, names='hour')
fig.show()


# In[57]:


df['Datew'] = pd.to_datetime(df['Wakeup_time'], errors='coerce')
df['dayw'] = (df['Datew']).dt.day
df['monthw'] = (df['Datew']).dt.month
df['yearw'] = (df['Datew']).dt.year
df['hourw'] = (df['Datew']).dt.hour


# In[58]:


df['hourw'].value_counts()


# In[59]:


sns.countplot(data=df, x="hourw", palette="ocean")
plt.show()


# In[60]:


fig = px.pie(df, names='hourw')
fig.show()


# Bu analiz bize göşteriyor ki iyi ve kaliteli bir uyku için alkol ve sigaradan uzak durmak gerek ve cok geç saatlerde uyuma alışkanlıkları terk edilmeli ve geç saatte kalkılmamalıdır. gece saat 12 de yatılması  ve sabah 5 gibi uyanılması sizi daha verimli bir uyku ile  gune merhana demeyi sağlar.           Hepinize GÜNAYDIN

# In[ ]:




