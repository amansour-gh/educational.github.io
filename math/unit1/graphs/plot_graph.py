import plotly.graph_objects as go

# بيانات للرسم البياني
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4, 5], y=[2, 4, 6, 8, 10], mode='lines+markers'))

# حفظ الرسم البياني كملف HTML
fig.write_html("interactive_graph.html")
