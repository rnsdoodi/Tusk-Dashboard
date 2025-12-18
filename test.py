import streamlit as st
import pandas as pd 
from numpy.random import default_rng as rng
import temp
import matplotlib.pyplot as plt
import importlib
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv('male-elephant-tusk-size.csv')

importlib.reload(temp)

st.header("Tusk Length Analysis (Interactive Dashboard)🐘")
st.markdown("The Tusk length Average")

print()
print()


a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Pre Poaching average", f"{temp.pre_poaching_average}", "9", border=True)
b.metric("Post Recovery average", f"{temp.post_recovery_average}", "-10", border=True)

# c.metric("Humidity", "77%", "5%", border=True)
# d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)
    
##############################################################################

# # 1. إنشاء "Figure" جديد
# fig, ax = plt.subplots()

# # 2. رسم البيانات (تأكد أن pre_poaching و post_recovery معرفة في الكود)
# ax.scatter(temp.pre_poaching['shoulder_height'], temp.pre_poaching['tusk_length'], marker='^', label='Pre Poaching')
# ax.scatter(temp.post_recovery['shoulder_height'], temp.post_recovery['tusk_length'], marker='s', label='Post Recovery')

# # 3. إضافة التسميات
# ax.set_xlabel('Shoulder Height (cm)')
# ax.set_ylabel('Tusk Length (cm)')

# # إضافة النصوص التوضيحية
# ax.text(x=200, y=120, s='Pre_poaching', color='C0')
# ax.text(x=220, y=35, s='Post_recovery', color='C1')

# # 4. عرض الرسم في Streamlit
# st.pyplot(fig)

################################################################################



# # 1. دمج البيانات في DataFrame واحد لسهولة الرسم (اختياري لكن أفضل)
# # أو يمكنك الرسم مباشرة من القوائم
# fig = px.scatter(
#     x=temp.pre_poaching['shoulder_height'], 
#     y=temp.pre_poaching['tusk_length'],
#     labels={'x': 'Shoulder Height (cm)', 'y': 'Tusk Length (cm)'},
#     title="Comparison of Tusk Length",
#     symbol_sequence=['triangle-up'], # تغيير شكل العلامة لـ Pre Poaching
#     color_discrete_sequence=['#c0fa63'],   # لون محدد
    

# )

# # 2. إضافة البيانات الثانية (Post Recovery) للمخطط
# fig.add_scatter(
#     x=temp.post_recovery['shoulder_height'], 
#     y=temp.post_recovery['tusk_length'],
#     mode='markers',
#     marker_symbol='square', # تغيير شكل العلامة لـ Post Recovery
#     name='Post Recovery' ,
    
# )

# # 3. تحديث مظهر المخطط (Layout)
# fig.update_layout(
#     legend_title="Category",
#     hovermode="closest"
# )

# # 4. عرض المخطط في Streamlit
# st.plotly_chart(fig, use_container_width=True)


#################################################################################

# 1. إنشاء مخطط التشتت الأساسي (Scatter Plot)
fig = px.scatter(
    temp.pre_poaching, 
    x='shoulder_height', 
    y='tusk_length',
    color_discrete_sequence=['#27AE60'],
)

# إضافة بيانات Post Recovery
fig.add_trace(go.Scatter(
    x=temp.post_recovery['shoulder_height'], 
    y=temp.post_recovery['tusk_length'],
    mode='markers',
    marker=dict(symbol='square', color='#5D6D7E'),
))

# 2. رسم خطوط الانحدار (Regression Lines)
# سنقوم بحساب نقطتين لكل خط (بداية ونهاية) بناءً على موديلك
x_range = [140, 250]

# خط Pre-Poaching
y_pre = [temp.pre_model.predict(x) for x in x_range]
fig.add_trace(go.Scatter(
    x=x_range, y=y_pre, 
    mode='lines', 
    line=dict(color='#636EFA', width=3)
))

# خط Post-Recovery
y_post = [temp.post_model.predict(x) for x in x_range]
fig.add_trace(go.Scatter(
    x=x_range, y=y_post, 
    mode='lines', 
    line=dict(color='#5D6D7E', width=3) # خط متقطع للتمييز
))

# 3. تحسين المظهر
fig.update_layout(
    xaxis_title='Shoulder Height (cm)',
    yaxis_title='Tusk Length (cm)',
    hovermode='x unified'
)

st.plotly_chart(fig, use_container_width=True)

#############################################################################



# الصف الثاني: تفاصيل النماذج الإحصائية
col1, col2 = st.columns(2)

with col1:
    st.info("**Pre Poaching Model Info**")
    st.markdown(f"""
    * **Equation:** $y = {temp.pre_model.slope:.2f}x + {temp.pre_model.intercept:.2f}$
    * **Goodness of Fit  (R²):** `{temp.pre_model.rsquared:.3f}`
     * Slope = {temp.pre_model.slope:.2f}x
     * intercept = {temp.pre_model.intercept:.2f}
    """)

with col2:
    st.info("**Post Recovery Model Info**")
    st.markdown(f"""
    * **Equation:** $y = {temp.post_model.slope:.2f}x + {temp.post_model.intercept:.2f}$
    * **Goodness of Fit (R²):** `{temp.post_model.rsquared:.3f}`
    * Slope = {temp.post_model.slope:.2f}x
    * intercept = {temp.post_model.intercept:.2f}
    """)

##############################################################################


st.markdown(
    """
    <style>
    .stApp {
        background-color: #00010f;
    }
    </style>
    """,
    unsafe_allow_html=True
)



#############################################################################




